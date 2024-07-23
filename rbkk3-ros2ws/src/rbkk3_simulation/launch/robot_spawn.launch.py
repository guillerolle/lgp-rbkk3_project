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
    PythonExpression
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node, PushRosNamespace

import os

from ament_index_python.packages import get_package_share_directory


ARGUMENTS = [
    DeclareLaunchArgument('rviz', default_value='false',
                          choices=['true', 'false'],
                          description='Start rviz.'),
    DeclareLaunchArgument('use_sim_time', default_value='true',
                          choices=['true', 'false'],
                          description='use_sim_time'),
    DeclareLaunchArgument('world', default_value='empty',
                          description='Gazebo World'),
    DeclareLaunchArgument('robot_name', default_value='rbkk3',
                          description='Robot name'),
    DeclareLaunchArgument('arm_cmd_if', default_value='position',
                          choices=['position', 'effort'],
                          description='Arm command interface type'),
]

for pose_element in ['x', 'y', 'yaw']:
    ARGUMENTS.append(DeclareLaunchArgument(pose_element, default_value='0.0',
                     description=f'{pose_element} component of the robot pose.'))

ARGUMENTS.append(DeclareLaunchArgument('z', default_value='0.15',
                 description='z component of the robot pose.'))


def launch_setup(context, *args, **kwargs):
    # setup_path = os.path.expanduser(os.path.join('~', 'rbkk3-ros2ws','setup_path'))
    world = LaunchConfiguration('world')
    use_sim_time = LaunchConfiguration('use_sim_time')
    x, y, z = LaunchConfiguration('x'), LaunchConfiguration('y'), LaunchConfiguration('z')
    yaw = LaunchConfiguration('yaw')

    arm_cmd_if = LaunchConfiguration('arm_cmd_if')

    robot_name = LaunchConfiguration('robot_name')
    namespace = robot_name

    # Directories
    # pkg_clearpath_viz = FindPackageShare('clearpath_viz')
    pkg_rbkk3_simulation = get_package_share_directory('rbkk3_simulation')
    pkg_rbkk3_description = FindPackageShare('rbkk3_description')
    pkg_rbkk3_rviz = FindPackageShare('rbkk3_rviz')
    pkg_ridgeback_simulation = get_package_share_directory('ridgeback_simulation')

    # Paths
    rviz_launch = PathJoinSubstitution(
        [pkg_rbkk3_rviz, 'launch', 'rviz.launch.py'])
    # launch_file_platform_service = PathJoinSubstitution([
    #     pkg_rbkk3_simulation, 'platform/launch', 'platform-service.launch.py'])
    # launch_file_sensors_service = PathJoinSubstitution([
    #     pkg_rbkk3_simulation, 'sensors/launch', 'sensors-service.launch.py'])


    # Launch Description
    include_launch_robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            pkg_rbkk3_description,
            'launch',
            'robot_description.launch.py'])
        ),
        launch_arguments=[
            ('robot_name', robot_name),
            ('sim_ignition', 'true'),
            ('rsp_ns', namespace),
            ('use_effort_command_interfaces', 'true' if arm_cmd_if.perform(context)=='effort' else 'false'),
        ]
    ) 

    # LIDAR BRIDGE
    gz_topic_lidar = '/'.join(["/world", 
            world.perform(context),
            'model',
            robot_name.perform(context),
            'link',
            robot_name.perform(context=context) + '/platform/base_link',
            'sensor',
            robot_name.perform(context=context) + '/platform/front_laser_sensor',
            'scan'])

    group_action_spawn_robot = GroupAction([PushRosNamespace(namespace),
        # Spawn robot
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-name', robot_name,
                       '-x', x,
                       '-y', y,
                       '-z', z,
                       '-Y', yaw,
                       '-topic', 'robot_description'],
            output='screen'
        ),
        
        # Joint State Broadcasters
        Node(package='controller_manager', executable='spawner',
            arguments=[
                robot_name.perform(context) + '_arm_joint_state_broadcaster',
                '-c', 'controller_manager',
            ],
        ),
        Node(package='controller_manager', executable='spawner',
            arguments=[
                robot_name.perform(context) + '_platform_joint_state_broadcaster',
                '-c', 'controller_manager',
            ],
        ),

        # Ridgeback Velocity Controller
        Node(package='controller_manager', executable='spawner',
            arguments=[
                robot_name.perform(context) + '_platform_velocity_controller',
                '-c', 'controller_manager',
                #'-p', PathJoinSubstitution([pkg_rbkk3_description, 'config', 'platform_velocity_controller.yaml'])
            ],
        ),

        # Arm trajectory controller
        Node(package='controller_manager', executable='spawner',
            arguments=[
                robot_name.perform(context) + '_arm_joint_trajectory_controller_' + arm_cmd_if.perform(context),
                '-c', 'controller_manager',
                #'-p', PathJoinSubstitution([pkg_rbkk3_description, 'config', 'platform_velocity_controller.yaml'])
            ],
        ),

        # Ridgeback IMU Bridge
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution([
                pkg_ridgeback_simulation,
                'launch',
                'imu_bridge.launch.py'])
            ),
            launch_arguments=[
                ('robot_name', robot_name),
                ('world_name', world),
                ('link_name', robot_name.perform(context=context) + '/platform/base_link'),
                ('sensor_name', 'imu_sensor'),
                ('ros_topic', 'ridgeback/sensors/imu'),
            ]
        ),

         # Lidar Bridge 
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='lidar_bridge',
            arguments=[gz_topic_lidar + '@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan'],
            output='screen',
            remappings=[
                (gz_topic_lidar, 'ridgeback/sensors/lidar/scan')
            ],
            parameters=[{
                'use_sim_time': use_sim_time,
            }]
        ),


        # Robot Localization
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[PathJoinSubstitution([pkg_rbkk3_description, 'config', 'ekf.yaml']),
                        {
                            'use_sim_time': use_sim_time,
                        }]
        ),

        # RViz
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([rviz_launch]),
            # namespace=namespace,
            launch_arguments=[
                ('use_sim_time', use_sim_time),
                ('config', 'view_robot')],
            condition=IfCondition(LaunchConfiguration('rviz')),
        ),
    ])


    # event_generate_param = RegisterEventHandler(
    #     event_handler=OnProcessExit(
    #         target_action=node_generate_param,
    #         on_exit=[group_action_spawn_robot]
    #     )
    # )



    return [
        include_launch_robot_description,
        group_action_spawn_robot,
        #rviz,
    ]


def generate_launch_description():
    # Define LaunchDescription variable
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(OpaqueFunction(function=launch_setup))
    return ld
