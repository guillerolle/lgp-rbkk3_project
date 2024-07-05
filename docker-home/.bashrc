#!/bin/bash
echo SOURCEANDO .BASHRC...
source ~/venvs/$(hostname)/$(id --user --name)-python310.venv/bin/activate
source /opt/ros/humble/setup.bash;
source ~/ros2_kortex-ros2ws/install/local_setup.bash
cd ~/rbkk3-ros2ws;
source install/local_setup.bash;
export ROS_LOG_DIR=~/rbkk3-ros2ws/log
export PYTHONWARNINGS='ignore:::setuptools.command.install,ignore:::setuptools.command.easy_install,ignore:::pkg_resources'
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
