# Docker Workflow for MoveIt2 Containers

This guide outlines the steps to check the status of containers and run a MoveIt2 container using Docker Compose.

## 1. Navigate to the Project Directory

First, open your terminal and navigate to the directory where your `docker-compose.yml` file is located.

```cd /home/oliver/workspaces```

## 2. Check Container Status

To view the status of all Docker containers, use the following command:

```docker ps -a```

* If you do not see any information or containers listed, it may mean that no containers have been started yet(pls continue to step 3.).
* If `moveit2_container` is Up, you can simply enter using `docker exec -it moveit2_container /bin/bash` and then run packages below(skip 3-6). 
* If `moveit2_container` is Exited, you need to firstly `docker start moveit2_container` and then `docker exec -it moveit2_container /bin/bash` and then run packages below(skip 3-6). 

## 3. Run the MoveIt2 Container

If no containers are running, or you are running it for the first time, you can start a MoveIt2 container using the following command:

```docker compose run --name moveit2_container cpu```

This will start the container with the name `moveit2_container` and use the `cpu` configuration.
The image we used in docker-compose.yml is based on moveit/moveit2:jazzy-source. I upgraded it and built ur_ros2_driver and ur_gz_simulation from source.

## 4. Enter the Default Workspace

Once the container starts, you will enter the default workspace, typically named `ws_moveit`.

## 5. Navigate to Parent Directory

To go back to the upper-level directory (where the `ws_moveit` workspace is located), use the `cd ..` command:

## 6. Verify Available Workspaces

Once you are back in the upper-level directory, use `ls` to list all available workspaces, you should see all workspaces listed.

# Test ur_ros2_driver
```
cd /root/ros_ur_driver/
source install/setup.bash
ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur10e robot_ip:=yyy.yyy.yyy.yyy use_mock_hardware:=true
```
now u can see ur10e in Rviz, next open another terminal and enter the same container
```
docker exec -it moveit2_container /bin/bash
cd /root/ros_ur_driver/
source install/setup.bash
ros2 launch ur_robot_driver test_scaled_joint_trajectory_controller.launch.py
```
now u should see the robot moves


# Test ur_simulation_gz
```cd /root/ur_gz/
source install/setup.bash
ros2 launch ur_simulation_gz ur_sim_moveit.launch.py ur_type:=ur10e
```
now u can use moveIt

# Move the real robot
- start the robot
- the mode on upper right corner set to local control
- inside container
```
cd /root/ros_ur_driver/
source install/setup.bash
ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur10e robot_ip:=169.254.17.61
```
- you can now see the real robot in Rviz, the ip can be found in teach-pendant.
- on the teach-pendant, run Robot Program External Control
- open another terminal and run following commands:
```
docker exec -it moveit2_container /bin/bash
cd /root/ros_ur_driver/
source install/setup.bash
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur10e launch_rviz:=true
```
Now you can use moveIt to control the real robot, BE CAREFUL !!!LOWER the Speed on teach-pendant.


