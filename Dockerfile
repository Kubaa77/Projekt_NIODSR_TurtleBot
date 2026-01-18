FROM osrf/ros:humble-desktop

ARG USERNAME=Jakub
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME


RUN apt-get update && apt-get install -y \
    python3-opencv \
    ros-humble-turtlebot3-msgs \
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/$USERNAME/projekt_robot_ws

COPY --chown=$USERNAME:$USER_GID . src/sterowanie_robotem

RUN . /opt/ros/humble/setup.sh && colcon build --packages-select sterowanie_robotem

RUN echo "source /opt/ros/humble/setup.bash" >> /home/$USERNAME/.bashrc \
    && echo "source /home/$USERNAME/projekt_robot_ws/install/setup.bash" >> /home/$USERNAME/.bashrc \
    && echo "export TURTLEBOT3_MODEL=burger" >> /home/$USERNAME/.bashrc

ENV SHELL /bin/bash
USER $USERNAME
CMD ["/bin/bash"]