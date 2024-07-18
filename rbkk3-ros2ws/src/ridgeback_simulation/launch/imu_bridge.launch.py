# Copyright 2021 Clearpath Robotics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Roni Kreinin (rkreinin@clearpathrobotics.com)

from clearpath_config.clearpath_config import ClearpathConfig

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    GroupAction,
    IncludeLaunchDescription,
    RegisterEventHandler,
    OpaqueFunction
)
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    EnvironmentVariable,
    LaunchConfiguration,
    PathJoinSubstitution,
    Command,
    FindExecutable,
    PythonExpression,
    TextSubstitution,
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node, PushRosNamespace

import os

from ament_index_python.packages import get_package_share_directory


ARGUMENTS = [
    DeclareLaunchArgument('sensor_name', default_value='imu_sensor',
                          description='Sensor name'),
    DeclareLaunchArgument('link_name', default_value='base_link',
                          description='Imu link name (for fixed frames, the top level name frame is used'),
    DeclareLaunchArgument('world_name', default_value='empty',
                          description='Gazebo World'),
    DeclareLaunchArgument('robot_name', default_value='ridgeback',
                          description='Robot name'),
    DeclareLaunchArgument('ros_topic', default_value='imu',
                          description='ROS2 remapped topic')
]


def launch_setup(context, *args, **kwargs):
    # setup_path = os.path.expanduser(os.path.join('~', 'rbkk3-ros2ws','setup_path'))
    world_name = LaunchConfiguration('world_name')
    #namespace = PythonExpression(["'", LaunchConfiguration('robot_name'), "'"])
    #namespace = LaunchConfiguration('robot_name')
    robot_name = LaunchConfiguration('robot_name')
    link_name = LaunchConfiguration('link_name')
    sensor_name = LaunchConfiguration('sensor_name')
    ros_topic = LaunchConfiguration('ros_topic')

    # Directories
    # pkg_clearpath_viz = FindPackageShare('clearpath_viz')
    pkg_rbkk3_simulation = get_package_share_directory(
        'rbkk3_simulation')

    pkg_ridgeback_description = FindPackageShare('ridgeback_description')


    # Bridge (taken from https://github.com/gazebosim/ros_gz/blob/ros2/ros_gz_sim_demos/launch/imu.launch.py)
    gz_topic = '/'.join(["/world", 
                world_name.perform(context),
                'model',
                robot_name.perform(context),
                'link',
                link_name.perform(context),
                'sensor',
                sensor_name.perform(context),
                "imu"])
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[gz_topic + '@sensor_msgs/msg/Imu@gz.msgs.IMU'],
        output='screen',
        remappings=[
            (gz_topic, ros_topic)
        ]
    )

    return [bridge]

def generate_launch_description():
    # Define LaunchDescription variable
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(OpaqueFunction(function=launch_setup))
    return ld
