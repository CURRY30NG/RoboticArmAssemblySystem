REF: https://moveit.picknik.ai/humble/doc/how_to_guides/how_to_setup_docker_containers_in_ubuntu.html

1. docker pull moveit/moveit2:jazzy-source
2. wget https://raw.githubusercontent.com/ros-planning/moveit2_tutorials/main/.docker/docker-compose.yml
3. DOCKER_IMAGE=jazzy-source docker compose run --rm --name moveit2_container gpu
4. apt update && apt upgrade

REF: https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_robot_driver/ur_robot_driver/doc/installation/installation.html#build-from-source

1. under root create new ws ros_ur_driver using mkdir
2. cd ros_ur_driver and mkdir src
3. git clone -b jazzy https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver.git src/Universal_Robots_ROS2_Driver
  - u should see 2 sterr
4. rosdep update &&
rosdep install --ignore-src --from-paths src -y
5. source /opt/ros/jazzy/setup.bash
6. colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
7. source install/setup.bash

before Test, make sure u source /opt/ros/jazzy/setup.bash and source install/setup.bash under ws: 
1. ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur5e robot_ip:=yyy.yyy.yyy.yyy use_mock_hardware:=true
2. open another terminal for the same container using docker exec -it moveit2_container /bin/bash
3. cd /root/ros_ur_driver/ and then source /opt/ros/jazzy/setup.bash && source install/setup.bash
4. ros2 launch ur_robot_driver test_scaled_joint_trajectory_controller.launch.py
5. when robot in RViz moves, Done !!! 

Then:

ur_gz is similar
after successfully set
source all
and ros2 launch ur_simulation_gz ur_sim_moveit.launch.py ur_type:=ur10e
MoveIt should be functional
