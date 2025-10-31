# FAPS Robotic Arm Cabinet Assembly System
## Important Requirements:
```
sudo apt update
sudo apt install ros-jazzy-moveit-*
sudo apt install ros-jazzy-ur-*
```
## Workspace Structure Example
```text
src/
├── ramses/               # namespace for self-development packages
│   ├── ramses_hello/     # for test
│   ├── ramses_package2/
│   ├── ...
│
├── image_pipeline/       # for camera intrinsic calibration
│   ├── 3rd-party package1/
│   ├── 3rd-party package2/
│   ├── ...
│
├── camera_aravis2/      # ros2 camera driver
│   ├── 3rd-party package1/
│   ├── 3rd-party package2/
|  
├── 3rd-party packages/
│
├── ...
└──
```
## Locally workflow
- Entrance
```bash
cd /home/shared_ws/
code .
```
- [Guide](documentation/package_dev_workflow.md) for custom package development


## Moveit for real robot control
- check [here](documentation/moveit_control_real_robot.md)

## Third party packages git & build
### image_pipeline
- REF: <a href="https://docs.nav2.org/tutorials/docs/camera_calibration.html">ROS2 Camera Calibration</a>
- check [here](documentation/camera_usage.md) for build from source and usage
### camera_aravis2
- REF: <a href="https://github.com/FraunhoferIOSB/camera_aravis2/tree/main?tab=readme-ov-file">Camera Driver</a>
- check [here](documentation/camera_usage.md) for build from source and usage

## TODOs: 
- [x] make documentation clear for current uasge
- [x] make development env clear without Docker, git push what? example workflow (work together)   









