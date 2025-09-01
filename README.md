# FAPS Robotic Arm Cabinet Assembly System

## Requirements
- <a href="https://releases.ubuntu.com/jammy/">Ubuntu 22.04</a>
- <a href="https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html">ROS2 Humble</a>

## Resources
- <a href="https://moveit.picknik.ai/main/index.html">MoveIt 2 Documentation</a>
- <a href="https://control.ros.org/humble/doc/getting_started/getting_started.html">ros2_control</a>
- <a href="https://control.ros.org/humble/doc/gazebo_ros2_control/doc/index.html">gazebo_ros2_control</a>
- <a href="https://github.com/UniversalRobots">UniversalRobots Repo</a>
- <a href="https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver/tree/humble">Universal_Robots_ROS2_Driver-humble-repo</a>
- <a href="https://docs.ros.org/en/ros2_packages/humble/api/ur_robot_driver/doc/overview.html">Universal_Robots_ROS2_Driver-doc</a>


## Tutorial - UR10e in Gazebo

Remember to install these packages in your system:

sudo apt install ros-humble-ros2-control
sudo apt install ros-humble-ros2-controllers
sudo apt install ros-humble-gripper-controllers
sudo apt install gazebo
sudo apt install ros-humble-gazebo-ros2-control
sudo apt install ros-humble-gazebo-ros-pkgs
sudo apt install ros-humble-xacro
sudo apt install ros-humble-rmw-cyclonedds-cpp
sudo apt install ros-humble-sensor-msgs

1. build workspace and source
2. under src/ ```git clone -b humble https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git```, these are ROS2 URDFs for Universal Robots. 
3. under src/ ```git clone -b humble https://github.com/UniversalRobots/Universal_Robots_ROS2_Gazebo_Simulation.git```, this is for Gazebo simulation.
4. using ```rosdep update && rosdep install --ignore-src --from-paths . -y``` for install dependencies for Universal_Robots_ROS2_Gazebo_Simulation.
meet error: unable to locate package ros-humble-gazebo-ros2-control


