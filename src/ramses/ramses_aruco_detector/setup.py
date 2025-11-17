from setuptools import setup

package_name = 'ramses_aruco_detector'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    py_modules=[],
    install_requires=[
        'setuptools',
        'opencv-python',
        'numpy',
        'tf-transformations',
        # cv_bridge Python依赖一般通过ROS系统安装，不用写pip
    ],
    zip_safe=True,
    author='Your Name',
    author_email='your.email@example.com',
    description='ROS2 Python package for ArUco marker detection',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 节点命令行名 = Python模块路径:main函数
            'aruco_detection_node = ramses_aruco_detector.aruco_detection_node:main',
        ],
    },
)
