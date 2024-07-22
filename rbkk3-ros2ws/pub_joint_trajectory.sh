#!/usr/bin/bash

ros2 topic pub /rbkk3/arm_joint_trajectory_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
    joint_names: [
        rbkk3/arm/joint_1, 
        rbkk3/arm/joint_2, 
        rbkk3/arm/joint_3, 
        rbkk3/arm/joint_4, 
        rbkk3/arm/joint_5, 
        rbkk3/arm/joint_6, 
        rbkk3/arm/joint_7, 
        ],
    points: [{
        positions: [
            -1,
            1,
            1,
            1,
            -1,
            1,
            1,
        ],
        time_from_start: {
            sec: 1,
            nanosec: 0
        }
    },]
}" -1