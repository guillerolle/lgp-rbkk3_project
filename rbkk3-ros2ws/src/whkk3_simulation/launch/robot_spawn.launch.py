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
    PathJoinSubstitution
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

import os

from ament_index_python.packages import get_package_share_directory


ARGUMENTS = [
    DeclareLaunchArgument('rviz', default_value='false',
                          choices=['true', 'false'],
                          description='Start rviz.'),
    DeclareLaunchArgument('use_sim_time', default_value='true',
                          choices=['true', 'false'],
                          description='use_sim_time'),
    DeclareLaunchArgument('world', default_value='warehouse',
                          description='Gazebo World'),
]

for pose_element in ['x', 'y', 'yaw']:
    ARGUMENTS.append(DeclareLaunchArgument(pose_element, default_value='0.0',
                     description=f'{pose_element} component of the robot pose.'))

ARGUMENTS.append(DeclareLaunchArgument('z', default_value='0.15',
                 description='z component of the robot pose.'))


def launch_setup(context, *args, **kwargs):
    setup_path = os.path.expanduser(os.path.join('~', 'rbkk3-ros2ws','setup_path'))
    world = LaunchConfiguration('world')
    use_sim_time = LaunchConfiguration('use_sim_time')
    x, y, z = LaunchConfiguration('x'), LaunchConfiguration('y'), LaunchConfiguration('z')
    yaw = LaunchConfiguration('yaw')

    # # Parse robot YAML into config
    # clearpath_config = ClearpathConfig(os.path.join(
    #     str(setup_path), 'robot.yaml'))
    #
    # namespace = clearpath_config.system.namespace
    # if namespace in ('', '/'):
    #     robot_name = 'robot'
    # else:
    #     robot_name = namespace + '/robot'

    namespace = 'whkk3_ns'
    robot_name = 'whkk3'

    # Directories
    pkg_clearpath_viz = FindPackageShare('clearpath_viz')
    pkg_whkk3_simulation = get_package_share_directory(
        'whkk3_simulation')

    # Paths
    rviz_launch = PathJoinSubstitution(
        [pkg_clearpath_viz, 'launch', 'view_robot.launch.py'])
    launch_file_platform_service = PathJoinSubstitution([
        pkg_whkk3_simulation, 'platform/launch', 'platform-service.launch.py'])
    launch_file_sensors_service = PathJoinSubstitution([
        pkg_whkk3_simulation, 'sensors/launch', 'sensors-service.launch.py'])

    group_action_spawn_robot = GroupAction([
        # TODO:
        # UNCOMMENT ALL OF THIS LATER
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_file_platform_service]),
            launch_arguments=[
                ('prefix', ['/world/', world, '/model/', robot_name, '/link/base_link/sensor/']),
                ('namespace', namespace),
            ]
        ),
        #
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([launch_file_sensors_service]),
        #     launch_arguments=[
        #       ('prefix', ['/world/', world, '/model/', robot_name, '/link/base_link/sensor/'])]
        # ),

        # Spawn robot
        Node(
            package='ros_gz_sim',
            executable='create',
            namespace=namespace,
            arguments=['-name', robot_name,
                       '-x', x,
                       '-y', y,
                       '-z', z,
                       '-Y', yaw,
                       '-topic', 'robot_description'],
            output='screen'
        ),
    ])


    # event_generate_param = RegisterEventHandler(
    #     event_handler=OnProcessExit(
    #         target_action=node_generate_param,
    #         on_exit=[group_action_spawn_robot]
    #     )
    # )

    # RViz
    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([rviz_launch]),
        launch_arguments=[
            ('namespace', namespace),
            ('use_sim_time', use_sim_time)],
        condition=IfCondition(LaunchConfiguration('rviz')),
    )

    return [
        group_action_spawn_robot,
        rviz
    ]


def generate_launch_description():
    # Define LaunchDescription variable
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(OpaqueFunction(function=launch_setup))
    return ld
