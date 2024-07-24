#!/usr/bin/env bash

xhost +local:root &&\
docker run --rm -it --net=host --privileged --env="DISPLAY" --env="QT_X11_NO_MITSHM=1"\
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --volume="$(pwd)/../docker-home:/home/duser:rw" \
  --volume="$(pwd)/../rbkk3-ros2ws:/home/duser/rbkk3-ros2ws:rw" \
  --volume="$(pwd)/../venvs:/home/duser/venvs:rw" \
  --volume="/etc/localtime:/etc/localtime:ro" \
  lgp/rbkk3:ros-humble-simulation bash -c "source ~/.bashrc; colcon build --symlink-install" &&\

# Detiene el contenedor
xhost -local:root
