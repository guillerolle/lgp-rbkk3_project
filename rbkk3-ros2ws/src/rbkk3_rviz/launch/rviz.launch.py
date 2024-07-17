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
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution, FindExecutable, TextSubstitution, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare

from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():    
    # Launch Arguments
    # arg_namespace = DeclareLaunchArgument(
    #     'namespace',
    #     default_value='/',
    #     description='Robot namespace'
    # )
    arg_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true'
    )
    arg_rviz_config = DeclareLaunchArgument(
        name='config',
        default_value='view_model',
    )

    # Launch Configurations
    rviz_config = PythonExpression(["'", LaunchConfiguration('config'), ".rviz'"])
    # namespace = LaunchConfiguration('namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Get Package Paths
    pkg_rbkk3_rviz = FindPackageShare('rbkk3_rviz')

    # RViz Config Argument
    #rviz2_config_arg = ['-d', PathJoinSubstitution([pkg_rbkk3_rviz, 'rviz', rviz_config])] if (rviz_config != '') else ''

    # ROS Namespace
    # ros_namespace = PushRosNamespace(namespace)

    # RViz 2
    rviz_node = Node(package='rviz2', executable='rviz2', name='rviz2',
            arguments=['-d', PathJoinSubstitution([pkg_rbkk3_rviz, 'rviz', rviz_config])],
            parameters=[{'use_sim_time': use_sim_time}],
            remappings=[
            #('/tf', 'tf'),
            #('/tf_static', 'tf_static')
            ],
            output='screen')
    
    # Launch Description
    ld = LaunchDescription()
    # ld.add_action(arg_namespace)
    ld.add_action(arg_rviz_config)
    ld.add_action(arg_use_sim_time)
    # ld.add_action(ros_namespace)
    ld.add_action(rviz_node)
    return ld
