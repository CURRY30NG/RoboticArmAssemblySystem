# Move the real robot
- start the robot
- the mode on upper right corner set to local control
- open a terminal
```
ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur10e robot_ip:=169.254.17.61
```
- the ip can be found in teach-pendant.
- you can now see the real robot in Rviz.
- on the teach-pendant, run Robot Program External Control
- open another terminal and run following commands:
```
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur10e launch_rviz:=true
```
BE CAREFUL !!!LOWER the Speed on teach-pendant.
Now you can use moveIt to control the real robot.


