# usage of IDS imaging sdk
open any terminal and run `ids_peak_cockpit`
---
# usage of locally built packages
ref: https://github.com/FraunhoferIOSB/camera_aravis2?tab=readme-ov-file#running-the-camera-driver
## for the normal usage
open any terminal
```bash
cd /home/oliver/workspaces/camera_aravis2
source install/setup.bash
ros2 launch camera_aravis2 ueye_ros2_driver_uv_song.launch.py
```
## for the first time
after successfully building the packages, 
firstly 
then the guid of camera is shown: `IDS Imaging Development Systems GmbH-1409f4e6b698-4108760728`.
run command below when only one camera connected, 
`ros2 run camera_aravis2 camera_xml_exporter`
Camera-specific GenICam XML file obtained, the xml file will be saved in current working directory with the 'guid' as filename.
now the default launch file `camera_driver_uv_example.launch.py` for usb3cam needed to be modified with the real cam info.

copy the original file and create new launch file for customize config
