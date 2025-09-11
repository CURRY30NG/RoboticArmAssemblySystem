#!/bin/bash
set -e

# 创建和宿主机相同 UID/GID 的用户，避免权限问题
if ! id -u devuser &>/dev/null; then
    groupadd -g $HOST_GID devuser
    useradd -m -u $HOST_UID -g $HOST_GID devuser
fi

# 切换到该用户执行
export HOME=/home/devuser
chown -R devuser:devuser $HOME

# ROS 环境
source /opt/ros/jazzy/setup.bash

# 切换到用户并执行命令
exec gosu devuser "$@"

