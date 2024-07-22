#!/usr/bin/bash

ros2 topic pub /rbkk3_0001/platform_velocity_controller/cmd_vel_unstamped geometry_msgs/msg/Twist "{
    linear: {
        x: 0, 
        y: 0
    },
    angular: {
        z: 10}
    }" -1