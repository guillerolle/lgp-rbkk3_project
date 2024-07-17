#!/usr/bin/env python3

# @author    Guillermo Rolle (LGP) <grolle@fceia.unr.edu.ar>

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    GroupAction,
    IncludeLaunchDescription,
    RegisterEventHandler,
)
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution, FindExecutable
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare

from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # Launch Arguments
    arg_namespace = DeclareLaunchArgument(
        'robot_namespace',
        default_value='rbkk3',
        description='Robot namespace'
    )

    # arg_use_sim_time = DeclareLaunchArgument(
    #     'use_sim_time',
    #     default_value='false',
    #     description='Use simulation (Gazebo) clock if true'
    # )

    # arg_rviz_config = DeclareLaunchArgument(
    #     name='config',
    #     default_value='ridgeback.rviz',
    # )

    # Launch Configurations
    # rviz_config = LaunchConfiguration('config')
    namespace = LaunchConfiguration('robot_namespace')
    # use_sim_time = LaunchConfiguration('use_sim_time')

    # Get Package Paths
    pkg_rbkk3_description = FindPackageShare('rbkk3_description')
    pkg_rbkk3_rviz = FindPackageShare('rbkk3_rviz')

    # Namespace
    #namespace = 'rbkk3'

    # Launch Description
    include_launch_robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            pkg_rbkk3_description,
            'launch',
            'robot_description.launch.py'])
        ),
        launch_arguments=[
            ('robot_namespace', namespace),
        ]
    ) 

    # Rviz && Joint State Publisher
    group_view_model = GroupAction([PushRosNamespace(namespace),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution([
                pkg_rbkk3_rviz,
                'launch',
                'rviz.launch.py'])
            ),
            launch_arguments=[
                #('namespace', namespace),
            ]
        ),      
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            remappings=[
                #("joint_states", "platform/joint_states")
            ],
            #namespace=namespace,
        ),                
    ])

    ld = LaunchDescription()
    # Args
    ld.add_action(include_launch_robot_description)
    ld.add_action(group_view_model)

    return ld
