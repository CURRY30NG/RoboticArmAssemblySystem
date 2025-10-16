# Camera Driver Installation and Intrinsic Calibration Guide

**Reference Link:** [https://docs.nav2.org/tutorials/docs/camera\_calibration.html](https://docs.nav2.org/tutorials/docs/camera_calibration.html)

This document guides you through using the camera driver and performing intrinsic calibration. Please follow the steps in order.

**Prerequisite:** Open a terminal.

## Installation of Calibration-Related Packages

### 1\. Install system dependencies

```bash
sudo apt install ros-jazzy-camera-calibration-parsers
sudo apt install ros-jazzy-camera-info-manager
sudo apt install ros-jazzy-launch-testing-ament-cmake
```

> **Note:** `ros-jazzy-camera-info-manager` is crucial for the camera driver package.

### 2\. Build `image_pipeline`

```bash
cd /home/oliver/song_ws/src
git clone -b jazzy git@github.com:ros-perception/image_pipeline.git
cd ..
colcon build
```

## Camera Driver Installation

**Reference Link:** [https://github.com/FraunhoferIOSB/camera\_aravis2?tab=readme-ov-file\#running-the-camera-driver](https://github.com/FraunhoferIOSB/camera_aravis2?tab=readme-ov-file#running-the-camera-driver)

### 1\. Install system dependencies

```bash
sudo apt install libaravis-dev
```

### 2\. Clone and install `camera_aravis2`

```bash
cd /home/oliver/song_ws/src
git clone https://github.com/FraunhoferIOSB/camera_aravis2.git
cd ..
```

### 3\. Install dependencies using rosdep

```bash
rosdep update
rosdep install --from-paths src -y --ignore-src
```

### 4\. Build from source

```bash
colcon build --symlink-install --packages-up-to camera_aravis2
```

## Using the Camera

### For the first time: Get camera GUID

1.  Make sure the camera is well connected. If the `ids_sdk` has been installed, simply run `ids_peak_cockpit`, you should be able to see the image.

2.  Output the camera GUID:

    ```bash
    cd /home/oliver/song_ws/
    source install/setup.bash
    ros2 run camera_aravis2 camera_finder
    ```

    You should then see the GUID of the camera (in our case, it is 'IDS ... 728').

3.  Create a new launch file using the GUID to start the camera.

      * Simply copy the original `uv_example` launch file and modify it (the example I created is **here**).
      * Then build and launch:

    <!-- end list -->

    ```bash
    colcon build --symlink-install --packages-select camera_aravis2
    source install/setup.bash
    ros2 launch camera_aravis2 ueye_ros2_driver_uv_song.launch.py
    ```

4.  For validation:

      * Please open a new terminal and run `ros2 topic list`. You should be able to see the camera topics.
      * Additionally, run `rviz2`, click Add -\> By topic, expand the dropdown for `/image_raw` and select Image, then click OK. The image should be shown.

### For normal usage

Make sure the workspace has been sourced and run:

```bash
ros2 launch camera_aravis2 ueye_ros2_driver_uv_song.launch.py
```

You can also create different launch files for different configurations.

> **Note:** Run `ros2 run camera_aravis2 camera_xml_exporter`. A camera-specific GenICam XML file will be obtained. Check this file to get info on what features the camera supports for configuration.

## Intrinsic Calibration
