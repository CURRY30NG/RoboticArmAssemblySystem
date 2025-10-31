# Example: Developing a Custom ROS2 Package

First, navigate to:
```bash
cd /home/shared_ws/src/ramses
````

---

## Create a Minimal ROS2 Package

Use the following command (C++ example):

```bash
ros2 pkg create --build-type ament_cmake ramses_hello --dependencies rclcpp
```

This will automatically generate:

```
ramses_hello/
├── CMakeLists.txt
├── package.xml
├── src/
└── include/
```

---

## 🧩 Add a Simple C++ Node

```bash
cd /home/shared_ws/src/ramses/ramses_hello/src/
touch hello_node.cpp
```

Copy the following code into `hello_node.cpp`:

```cpp
#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("hello_node");
  RCLCPP_INFO(node->get_logger(), "Hello, ROS2 from Ramses!");
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
```

---

## 🔧 Modify `CMakeLists.txt`

Open `CMakeLists.txt`
Add the following lines at the end (or replace the example if not present):

```cmake
add_executable(hello_node src/hello_node.cpp)
ament_target_dependencies(hello_node rclcpp)
install(TARGETS hello_node DESTINATION lib/${PROJECT_NAME})
```

---

## 🛠️ Build the Package

Return to the workspace root directory:

```bash
cd /home/shared_ws
colcon build --packages-select ramses_hello
```

---

## 🧠 Run the Node

After a successful build, source the environment:

```bash
source install/setup.bash
```

Then run the node:

```bash
ros2 run ramses_hello hello_node
```

You should see the following output:

```
[INFO] [hello_node]: Hello, ROS2 from Ramses!
```
