#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image, CameraInfo
from geometry_msgs.msg import Pose, PoseArray, TransformStamped, Vector3, Quaternion
from cv_bridge import CvBridge
import tf2_ros
from tf2_ros import TransformBroadcaster
from ros2_aruco_interfaces.msg import ArucoMarkers
import tf_transformations as tf_trans

class ArucoDetectorNode(Node):
    def __init__(self):
        super().__init__('aruco_node')

        # --- 参数 ---
        self.declare_parameter('marker_size', 0.04)
        self.declare_parameter('aruco_dictionary_id', 'DICT_4X4_1000')
        self.declare_parameter('camera_frame', 'camera')
        self.declare_parameter('publish_debug_image', True)

        self.marker_size_ = self.get_parameter('marker_size').get_parameter_value().double_value
        dict_id_str = self.get_parameter('aruco_dictionary_id').get_parameter_value().string_value
        self.camera_frame_ = self.get_parameter('camera_frame').get_parameter_value().string_value
        self.publish_debug_image_ = self.get_parameter('publish_debug_image').get_parameter_value().bool_value

        self.get_logger().info(f"Marker size: {self.marker_size_}")
        self.get_logger().info(f"Camera frame: {self.camera_frame_}")
        self.get_logger().info(f"Publishing debug image: {self.publish_debug_image_}")

        # --- 加载 ArUco 字典 ---
        try:
            dict_id = cv2.aruco.__dict__[dict_id_str]
            self.dictionary_ = cv2.aruco.getPredefinedDictionary(dict_id)
            self.detector_params_ = cv2.aruco.DetectorParameters_create()
        except KeyError:
            self.get_logger().fatal(f"Invaild ArUco Dict ID: {dict_id_str}")
            rclpy.shutdown()
            return

        # --- ROS 工具 ---
        self.bridge_ = CvBridge()
        self.camera_matrix_ = None
        self.dist_coeffs_ = None

        # --- 发布器 ---
        self.tf_broadcaster_ = TransformBroadcaster(self)
        self.markers_pub_ = self.create_publisher(ArucoMarkers, '/aruco_markers', 10)
        self.poses_pub_ = self.create_publisher(PoseArray, '/aruco_poses', 10)
        if self.publish_debug_image_:
            self.debug_image_pub_ = self.create_publisher(Image, '/debug_image', 10)
        else:
            self.debug_image_pub_ = None

        # --- 订阅器 ---
        self.info_sub_ = self.create_subscription(
            CameraInfo, '/camera_driver_uv_example/vis/camera_info', self.camera_info_callback, 10
        )
        self.image_sub_ = self.create_subscription(
            Image, '/camera_driver_uv_example/vis/image_mono', self.image_callback, 10
        )

        self.get_logger().info("ArUco Detection Node running，Waiting CameraInfo...")

    def camera_info_callback(self, msg: CameraInfo):
        if self.camera_matrix_ is None:
            self.get_logger().info("Received CameraInfo!")
            self.camera_matrix_ = np.array(msg.k).reshape((3, 3))
            self.dist_coeffs_ = np.array(msg.d)
            # 收到一次 CameraInfo 后取消订阅
            self.destroy_subscription(self.info_sub_)

    def _tvec_rvec_to_quaternion(self, tvec: np.ndarray, rvec: np.ndarray):
        """统一生成四元数，保证 Pose 与 TF 一致"""
        rot_matrix, _ = cv2.Rodrigues(rvec)
        T = np.eye(4)
        T[:3, :3] = rot_matrix
        q = tf_trans.quaternion_from_matrix(T)  # [x, y, z, w]
        return q

    def _tvec_rvec_to_pose(self, tvec: np.ndarray, rvec: np.ndarray) -> Pose:
        pose_msg = Pose()
        pose_msg.position.x = tvec[0]
        pose_msg.position.y = tvec[1]
        pose_msg.position.z = tvec[2]
        q = self._tvec_rvec_to_quaternion(tvec, rvec)
        pose_msg.orientation.x = q[0]
        pose_msg.orientation.y = q[1]
        pose_msg.orientation.z = q[2]
        pose_msg.orientation.w = q[3]
        return pose_msg

    def _tvec_rvec_to_transform(self, tvec: np.ndarray, rvec: np.ndarray) -> (Vector3, Quaternion):
        trans = Vector3(x=tvec[0], y=tvec[1], z=tvec[2])
        q = self._tvec_rvec_to_quaternion(tvec, rvec)
        quat = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
        return trans, quat

    def image_callback(self, msg: Image):
        if self.camera_matrix_ is None:
            self.get_logger().warn("Waiting CameraInfo...", throttle_duration_sec=5.0)
            return

        try:
            cv_image = self.bridge_.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            self.get_logger().error(f"CvBridge Trans Error: {e}")
            return

        corners, ids, _ = cv2.aruco.detectMarkers(gray, self.dictionary_, parameters=self.detector_params_)

        markers_msg = ArucoMarkers()
        poses_msg = PoseArray()
        markers_msg.header.frame_id = self.camera_frame_
        poses_msg.header.frame_id = self.camera_frame_

        transforms_to_send = []
        t_now = self.get_clock().now().to_msg()  # 使用当前 ROS 时间

        markers_msg.header.stamp = t_now
        poses_msg.header.stamp = t_now

        if ids is not None and len(ids) > 0:
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                corners, self.marker_size_, self.camera_matrix_, self.dist_coeffs_
            )

            for i, marker_id in enumerate(ids.flatten()):
                rvec = rvecs[i].flatten()
                tvec = tvecs[i].flatten()

                pose = self._tvec_rvec_to_pose(tvec, rvec)
                poses_msg.poses.append(pose)
                markers_msg.poses.append(pose)
                markers_msg.marker_ids.append(int(marker_id))

                tf_msg = TransformStamped()
                tf_msg.header.stamp = t_now
                tf_msg.header.frame_id = self.camera_frame_
                tf_msg.child_frame_id = f"marker_{marker_id}"

                trans, quat = self._tvec_rvec_to_transform(tvec, rvec)
                tf_msg.transform.translation = trans
                tf_msg.transform.rotation = quat

                transforms_to_send.append(tf_msg)

            # 调试图像绘制
            if self.publish_debug_image_:
                cv2.aruco.drawDetectedMarkers(cv_image, corners, ids)
                for i in range(len(rvecs)):
                    try:
                        cv2.drawFrameAxes(
                            cv_image,
                            self.camera_matrix_, self.dist_coeffs_,
                            rvecs[i], tvecs[i],
                            self.marker_size_ * 0.5
                        )
                    except AttributeError:
                        try:
                            cv2.aruco.drawAxis(
                                cv_image,
                                self.camera_matrix_, self.dist_coeffs_,
                                rvecs[i], tvecs[i],
                                self.marker_size_ * 0.5
                            )
                        except AttributeError:
                            self.get_logger().warn("Current OpenCV version doesn't support drawing axis")

        if transforms_to_send:
            self.tf_broadcaster_.sendTransform(transforms_to_send)

        self.poses_pub_.publish(poses_msg)
        self.markers_pub_.publish(markers_msg)

        if self.publish_debug_image_ and self.debug_image_pub_ is not None:
            try:
                debug_img_msg = self.bridge_.cv2_to_imgmsg(cv_image, encoding='bgr8')
                debug_img_msg.header = msg.header
                self.debug_image_pub_.publish(debug_img_msg)
            except Exception as e:
                self.get_logger().error(f"Pub debug image failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = ArucoDetectorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
