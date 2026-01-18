#!/bin/bash

xhost +local:docker

echo "Budowanie obrazu Dockera..."
docker build -t projekt_robot_img .

echo "Uruchamianie projektu..."
docker run -it \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --network host \
    projekt_robot_img \
    ros2 launch sterowanie_robotem sterowanie.launch.py