#!/usr/bin/env bash

docker exec -it "$(docker ps | awk '/lgp\/rbkk3:ros-humble-simulation/ { print $1 }')" bash
