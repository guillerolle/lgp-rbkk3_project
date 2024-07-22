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
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution, FindExecutable, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare

from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():    
    # Launch Arguments
    arg_rsp_ns = DeclareLaunchArgument(
        'rsp_ns',
        default_value='',
        description='Robot\'s state publisher namespace'
    )
    arg_robot_name = DeclareLaunchArgument(
        'robot_name',
        default_value='rbkk3',
        description='Robot name'
    )
    arg_sim_ignition = DeclareLaunchArgument(
        'sim_ignition',
        default_value='false',
        description='Robot is Ignition Simulation'
    )
    # arg_urdf_spawn_controller_manager = DeclareLaunchArgument(
    #     'urdf_spawn_controller_manager',
    #     default_value='true',
    #     description='Flag for not adding ridgeback\'s controller manager on final urdf when integrating both bots'
    # )

    # Launch Configurations
    robot_name = LaunchConfiguration('robot_name')
    sim_ignition = LaunchConfiguration('sim_ignition')
    rsp_ns = LaunchConfiguration('rsp_ns')

    use_sim_time = False
    if sim_ignition: # Do it this way to add other simulators in the if statement
        use_sim_time = True

    # Get Package Paths
    pkg_rbkk3_description = FindPackageShare('rbkk3_description')

    # Robot Description
    robot_description_content = ParameterValue(Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution([pkg_rbkk3_description, 'urdf', 'rbkk3.xacro']),
            ' ',
            'name:=', robot_name,
            ' ',
            'use_prefix:=', 'true',
            ' ',
            'sim_ignition:=', sim_ignition,
            # ' ',
            # 'spawn_controller_manager:=', urdf_spawn_controller_manager,
            # ' ',
            # 'controllers_config:=',
            # config_control,
            #' ',
            #'namespace:=', robot_namespace,
        ]
        ),
        value_type=str
    )

    # ROS Namespace
    # ros_namespace = PushRosNamespace(namespace)

    # Robot State Publisher
    robot_state_publisher_node = Node(package='robot_state_publisher', executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description_content,
            'use_sim_time': use_sim_time,
            # 'frame_prefix': PythonExpression(["'", robot_namespace, "/'"]), # DEPRECATED
        }],
        remappings=[ # ALL THIS REMAPPINGS SEEM TO BE DEPREACTED. EVEN FOR MULTIROBOT SIMULATIONS I THINK WE SHOULD PUBLISH TRANSFORM TO /tf AND /tf_static WITH PREFIXES FROM URDF
            #('/tf', 'tf'),
            #('/tf_static', 'tf_static'),
            #('joint_states', 'joint_states')
        ],
        namespace=rsp_ns,
    )
    
    # Launch Description
    ld = LaunchDescription()
    #ld.add_action(arg_robot_namespace)
    ld.add_action(arg_robot_name)
    ld.add_action(arg_rsp_ns)
    ld.add_action(arg_sim_ignition)
    ld.add_action(robot_state_publisher_node)
    return ld
