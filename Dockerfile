FROM moveit/moveit2:jazzy-source

# 更新系统
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    gosu \
    && rm -rf /var/lib/apt/lists/*

# 拷贝入口脚本
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
