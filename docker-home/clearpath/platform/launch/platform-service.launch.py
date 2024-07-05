from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import EnvironmentVariable, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    launch_arg_prefix = DeclareLaunchArgument(
        'prefix',
        default_value='/world/warehouse/model/robot/link/base_link/sensor/',
        description='Ignition sensor topic prefix')

    prefix = LaunchConfiguration('prefix')

    launch_arg_imu_filter = DeclareLaunchArgument(
        'imu_filter',
        default_value='/home/duser/clearpath/platform/config/imu_filter.yaml',
        description='')

    imu_filter = LaunchConfiguration('imu_filter')

    # Include Packages
    pkg_clearpath_platform = FindPackageShare('clearpath_platform')

    # Declare launch files
    launch_file_platform = PathJoinSubstitution([
        pkg_clearpath_platform, 'launch', 'platform.launch.py'])

    # Include launch files
    launch_platform = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launch_file_platform]),
        launch_arguments=
            [
                (
                    'setup_path'
                    ,
                    '/home/duser/clearpath/'
                )
                ,
                (
                    'use_sim_time'
                    ,
                    'true'
                )
                ,
                (
                    'namespace'
                    ,
                    'w200_0000'
                )
                ,
            ]
    )

    # Nodes
    node_cmd_vel_bridge = Node(
        name='cmd_vel_bridge',
        executable='parameter_bridge',
        package='ros_gz_bridge',
        namespace='w200_0000',
        output='screen',
        arguments=
            [
                'w200_0000/cmd_vel@geometry_msgs/msg/Twist[ignition.msgs.Twist'
                ,
                '/model/w200_0000/robot/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist'
                ,
            ]
        ,
        remappings=
            [
                (
                    'w200_0000/cmd_vel'
                    ,
                    'cmd_vel'
                )
                ,
                (
                    '/model/w200_0000/robot/cmd_vel'
                    ,
                    'platform/cmd_vel_unstamped'
                )
                ,
            ]
        ,
        parameters=
            [
                {
                    'use_sim_time': True
                    ,
                }
                ,
            ]
        ,
    )

    node_odom_base_tf_bridge = Node(
        name='odom_base_tf_bridge',
        executable='parameter_bridge',
        package='ros_gz_bridge',
        namespace='w200_0000',
        output='screen',
        arguments=
            [
                '/model/w200_0000/robot/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V'
                ,
            ]
        ,
        remappings=
            [
                (
                    '/model/w200_0000/robot/tf'
                    ,
                    'tf'
                )
                ,
            ]
        ,
        parameters=
            [
                {
                    'use_sim_time': True
                    ,
                }
                ,
            ]
        ,
    )

    node_imu_0_gz_bridge = Node(
        name='imu_0_gz_bridge',
        executable='parameter_bridge',
        package='ros_gz_bridge',
        namespace='w200_0000',
        output='screen',
        arguments=
            [
                [
                    prefix
                    ,
                    'imu_0/imu@sensor_msgs/msg/Imu[ignition.msgs.IMU'
                    ,
                ]
                ,
            ]
        ,
        remappings=
            [
                (
                    [
                        prefix
                        ,
                        'imu_0/imu'
                        ,
                    ]
                    ,
                    'sensors/imu_0/data_raw'
                )
                ,
            ]
        ,
        parameters=
            [
                {
                    'use_sim_time': True
                    ,
                }
                ,
            ]
        ,
    )

    node_imu_filter_node = Node(
        name='imu_filter_node',
        executable='imu_filter_madgwick_node',
        package='imu_filter_madgwick',
        namespace='w200_0000',
        output='screen',
        remappings=
            [
                (
                    'imu/data_raw'
                    ,
                    'sensors/imu_0/data_raw'
                )
                ,
                (
                    'imu/mag'
                    ,
                    'sensors/imu_0/magnetic_field'
                )
                ,
                (
                    'imu/data'
                    ,
                    'sensors/imu_0/data'
                )
                ,
                (
                    '/tf'
                    ,
                    'tf'
                )
                ,
            ]
        ,
        parameters=
            [
                imu_filter
                ,
            ]
        ,
    )

    # Create LaunchDescription
    ld = LaunchDescription()
    ld.add_action(launch_arg_prefix)
    ld.add_action(launch_arg_imu_filter)
    ld.add_action(launch_platform)
    ld.add_action(node_cmd_vel_bridge)
    ld.add_action(node_odom_base_tf_bridge)
    ld.add_action(node_imu_0_gz_bridge)
    ld.add_action(node_imu_filter_node)
    return ld
