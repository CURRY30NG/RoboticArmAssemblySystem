# FAPS Robotic Arm Cabinet Assembly System

## Requirements
- <a href="https://releases.ubuntu.com/noble/">Ubuntu 24.04</a>
- <a href="https://docs.ros.org/en/jazzy/Installation.html">ROS2 Jazzy</a>
- <a href="https://moveit.ai/install-moveit2/binary/">MoveIt2 </a>
- <a href="https://control.ros.org/jazzy/doc/getting_started/getting_started.html">ros2_control</a>

## Resources
- <a href="https://picknik.ai/hardware-ecosystem/">ROS 2 Compatible Hardwares</a>
- <a href="https://github.com/UniversalRobots">Universal_Robots Repo</a>
- <a href="https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver/tree/jazzy">Universal_Robots_ROS2_Driver-jazzy</a>
- <a href="https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_robot_driver/ur_robot_driver/doc/index.html">Universal Robots ROS 2 driver Documentation</a>


## Tutorials
- <a href="https://automaticaddison.com/the-complete-guide-to-docker-for-ros-2-jazzy-projects/">The Complete Guide to Docker for ROS 2 Jazzy Projects</a>
- <a href="https://automaticaddison.com/tutorials/#Manipulation">ROS2 Manipulation Tutorials</a>

## Working on:
- building development env using Docker
    - Sep3-Log: already updated via Teams
    - What's next: 
      - keep learning and trying
      - when things went not well, just use local env (Ubuntu 24.04 + ROS2 jazzy)
    - Sep6-Log: finally ur_ros_driver and ur_gz_simulation work on docker
    - What's next: 
      - Sep10 make it run on Halle5-computer
      - try to make real robot move
      - documentation
    - Sep11-Log: successfully run real UR10e with moveIt MotionPlanning Plugin in RViz
    - What's next:
      - learn moveIt, knowing what's there for our usage:
        - write a moveIt control node and implement home-pose
      - Integrate the camera into the system：
        - ros2 wrapper
        - add cam in urdf
        - calibration







