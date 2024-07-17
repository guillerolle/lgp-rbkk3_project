#!/usr/bin/env python3

# @author    Guillermo Rolle (LGP) <grolle@fceia.unr.edu.ar>
# Based on ROS2 Clearpath Platform Description Launch Files

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
        'namespace',
        default_value='',
        description='Robot namespace'
    )

    arg_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true'
    )

    arg_rviz_config = DeclareLaunchArgument(
        name='config',
        default_value='ridgeback.rviz',
    )

    # Launch Configurations
    rviz_config = LaunchConfiguration('config')
    namespace = LaunchConfiguration('namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Get Package Paths
    # pkg_clearpath_platform_description = FindPackageShare('clearpath_platform_description')
    # pkg_clearpath_viz = FindPackageShare('clearpath_viz')
    pkg_ridgeback_description = FindPackageShare('ridgeback_description')

    config_rviz = PathJoinSubstitution(
        [pkg_ridgeback_description, 'rviz', rviz_config]
    )

    # Robot Description
    robot_description_content = ParameterValue(Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution([pkg_ridgeback_description, 'urdf', 'ridgeback.urdf.xacro']),
            ' ',
            'is_sim:=',
            use_sim_time,
            # ' ',
            # 'gazebo_controllers:=',
            # config_control,
            ' ',
            'namespace:=',
            namespace,
        ]
        ),
        value_type=str
    )

    group_view_model = GroupAction([PushRosNamespace(namespace),
        # RViz 2
        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', config_rviz],
             parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
             remappings=[
               ('/tf', 'tf'),
               ('/tf_static', 'tf_static')
             ],
             output='screen'),

        # Joint State Publisher GUI
        Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui',
            remappings=[
                # ("joint_states", "platform/joint_states")
            ]
        ),

        # Robot State Publisher
        Node(package='robot_state_publisher', executable='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description_content,
                'use_sim_time': use_sim_time,
            }],
            remappings=[
                ('/tf', 'tf'),
                ('/tf_static', 'tf_static'),
                ('joint_states', 'joint_states')]
        ),
    ])

    ld = LaunchDescription()
    # Args
    # ld.add_action(arg_setup_path)
    ld.add_action(arg_namespace)
    ld.add_action(arg_rviz_config)
    ld.add_action(arg_use_sim_time)
    ld.add_action(group_view_model)
    # Nodes
    #ld.add_action(node_generate_description)
    #ld.add_action(event_generate_description)

    return ld
