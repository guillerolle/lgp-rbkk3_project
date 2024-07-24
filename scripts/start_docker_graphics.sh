#!/usr/bin/env bash

mkdir "$(pwd)/../docker-sources/site-packages" "$(pwd)/../docker-sources/dist-packages" "$(pwd)/../docker-sources/share" # CREATE DIRS FOR MOUNTS

docker volume create --driver local --opt type=none --opt device="$(pwd)/../docker-sources/site-packages" --opt o=bind rbkk3-docker-site &&\
docker volume create --driver local --opt type=none --opt device="$(pwd)/../docker-sources/dist-packages" --opt o=bind rbkk3-docker-dist &&\
docker volume create --driver local --opt type=none --opt device="$(pwd)/../docker-sources/share" --opt o=bind rbkk3-docker-share &&\
xhost +local:root &&\
docker run --rm -it --net=host --privileged --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"  \
  --volume="$(pwd)/../docker-home:/home/duser:rw" \
  --volume="$(pwd)/../rbkk3-ros2ws:/home/duser/rbkk3-ros2ws:rw" \
  --volume="$(pwd)/../official-repos/ros2_kortex-ros2ws:/home/duser/ros2_kortex-ros2ws:rw" \
  --volume="$(pwd)/../official-repos/clearpath_mecanum_drive_controller-ros2ws:/home/duser/clearpath_mecanum_drive_controller-ros2ws:rw" \
  --volume="$(pwd)/../venvs:/home/duser/venvs:rw" \
  --volume="/etc/localtime:/etc/localtime:ro" \
  --volume="rbkk3-docker-site:/opt/ros/humble/lib/python3.10/site-packages" \
  --volume="rbkk3-docker-dist:/opt/ros/humble/local/lib/python3.10/dist-packages" \
  --volume="rbkk3-docker-share:/opt/ros/humble/share" \
  lgp/rbkk3:ros-humble-simulation &&\
xhost -local:root

docker volume rm rbkk3-docker-site
docker volume rm rbkk3-docker-dist
docker volume rm rbkk3-docker-share

# --volume="`pwd`/../tbot-ros2ws:/home/duser/tbot-ros2ws:rw" --volume="`pwd`/../venvs/requirements.txt:/home/duser/requirements.txt:rw"
# --volume="`pwd`/../docker-home:/home/duser:rw"


  # --volume="`pwd`/../docker-home/.bashrc:/home/duser/.bashrc:rw" \
  # --volume="`pwd`/../docker-home/.bash_history:/home/duser/.bash_history:rw" \
  # --volume="$(pwd)/../docker-home/venvs:/home/duser/venvs:rw" \
