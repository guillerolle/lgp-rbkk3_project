#!/bin/bash
# Este archivo compila el docker file

cd ..
docker build --build-arg USER_ID=$(id -u ${USER}) --build-arg GROUP_ID=$(id -g ${USER}) --rm -t "lgp/rbkk3:ros-humble-simulation" .
cd -
