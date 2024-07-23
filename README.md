# *Mobile Manipulator: Ridgeback + Kinova Kortex Gen3* 
This a repository for **ENIT/LGP** internal use only. It contains all the work related to integrating the ***Ridgeback*** mobile base with the ***Kinova Kortex Gen3*** manipulator (for short: ***rbkk3***).

## Quick introduction to the project
The main idea of this project is to integrate [Kinova Gen3](https://www.kinovarobotics.com/product/gen3-robots) manipulator on top of [Clearpath Robotics: Ridgeback](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) mobile platform, obtaining a Mobile Manipulator. A full integration is necessary in terms of mechanical, electrical, communications and control in order to do further research on mobile manipulation topics. 

**Comments on current state: **Due to external issues and time limits for effectively solving them, the real robot's integration couldn't be achieved yet but, hopefully, this repository can be a starting point to continue this project. The integration have been done only in simulation with Gazebo with little testing. There will be some comments on the perspective of implementing this on the real hardware.


## Quick introduction to the repository
This repository provides:

* *ROS2* packages relative to:
    * the mobile platform.
    * the manipulator.
    * integration packages.
* *Gazebo* packages for simulation.
* *Docker* specific files, predefined structure and helper scripts to run everything inside a Docker container.

**Note:** this repository is not meant to be open to the public as it's just a basic repository used to document and transfer progress on this specific setup for whoever may continue with this work. You might find that the codes have a lot of bugs, there are useless files around, code might not be properly documented, the organization and workflow is not be optimal, etc. This repository is just *as-is* and hopefully it will help the next person working on this project to catch-up with what's already been done and researched and can continue from there.

# Repository Structure
In this section a general description on directory and structure of the repo is given. In many subdirectories you will find more `README.md` files with more detailed information on what's inside it.

* `rbkk3-ros2ws`: this is the main ROS2 workspace for the project. It contains the `src` directory with the source code for the new custom made packages. 
* `official-repos`: it contains some "official" third party repositories (from Clearpath, Kinova, ROS, etc.) which, for some reason, need to be built from source. Maybe, there are no available packages for easily downloading them or maybe a little adaptation (might be hard-coded) was made to achieve robot's integration.
* `docker-home`: this directory is used as a mounting point for `$HOME`of the Docker container.
* `docker-sources`: contains various mounting points to the ROS files that are installed inside the Docker container as linux packages. It allows to have references to the packages shared files to allow the use of an IDE to autodetect includes, imports, function and classes definitions and declarations, etc.
* `scripts`: helper scripts for quick and automated execution of certain functionalities in Docker.
* `venvs`: not used for this project but could be useful. It contains python requirements and a helper script to create python's virtual environments. It's useful when developing a ROS node with some specific libraries: it avoids the need of recompiling the full docker image when a new python library needs to be used or tested.

# Workflow / usage guide
In the following lines, a step by step guide is provided to setup and reproduce the Docker container and quick run the simulations. This is how I use the repo. You can always see actual script codes to see what's going on. The (\*) symbol is used to indicate steps that are needed to be run only once when setting up the repository (or whenever a workspace or Docker image recompilation is needed, etc). You can take a look at the script's 

## **1. (\*) Docker Image Compilation:**
The first step is to compile the Docker image with the `compile_docker.sh` helper script.
```
cd scripts   
./compile_docker.sh
```
This should allow you to run the Docker container now.

# 2. Building third-party repositories
Everytime you need to do changes to the repositories inside `official_repos` you will need to rebuild them manually. For this, you need to go launch the docker container with the help of the `start_docker_graphics.sh`script, navigate to the repositories and build them:
```
$ cd scripts
$ ./start_docker_graphics.sh

<DOCKER STARTING...>
SOURCING .BASHRC...  # YOU SHOULD SEE THIS MESSAGE IF EVERYTHING IS WORKING FINE UNTIL NOW. THIS MESSAGE MEANS IT IS CORRECTLY READING THE .bashrc from docker-home

# A BUNCH OF UNABLE TO SOURCE FILES SHOULD COME UP. THIS ARE THE ROS2 WORKSPACES THAT WE HAVEN'T BUILD YET SO NO WAY TO SOURCE THEM. THIS ERRORS ARE OK

~/rbkk3-ros2ws$ # THE TERMINAL SHOULD BE WAITING FOR INPUT IN THIS DIRECTORY AFTER THE START PROCESS
```

Now that we are inside Docker, we need to compile the third party workspaces:

**ros2_kortex-ros2ws:**

This is the official repository for the Kinova arm. Main changes were made to allow no-gripper configurations (as per the lab's robot configuration)
```
cd ~/ros2_kortex-ros2ws
# YOU SHOULD FOLLOW INSTRUCTIONS IN src/ros2_kortex/README.md. Steps 3 and 4 mainly.
```
***Note: ***You should be able to do a `git diff` in `src/ros2_kortex` directory to see changes made to the official repository

**clearpath_mecanum_drive_controller-ros2ws**

This repository was forked from a Clearpath repository that I found on their's Github profile. It's not yet ready for public use so some changes to the code was done to get it working here. It implements a Mecanum Drive Controller in ROS2 to be used with the Ridgeback. Keep in mind that Ridgeback support is currently only in ROS1 officially.
```
cd ~/clearpath_mecanum_drive_controller-ros2ws
colcon build
```
***Note: ***You should be able to do a `git diff` in `src/ros2_controllers` directory to see changes made to the official repository.

# 3. Workspace Compilation
Whenever you need to rebuild the `rbkk3-ros2ws` you can make use of the `build_workspace.sh`helper script from HOST machine.

```
cd scripts
./build_workspace.sh
```

This will build the workspace with `--symlink-install` so that the data files (descriptions, launch files, configs, meshes, etc.) are symlinked to that of the `src`directory so you don't need to rebuild for every change you make. Only when new files are added or c++ code is modified that you need to rebuild.

# 4. Starting container and Gazebo simulation
If you already built of the needed workspaces you can exit the container (just with an `exit` command on the terminal) and login again. This will make sure to correctly source the needed workspaces. You use the `start_docker_graphics.sh` helper script again to do so:

```
cd scripts
./start_docker_graphics.sh
\# SOURCING .BASHRC... # NO ERRORS ABOUT SOURCING WORKSPACES SHOULD SHOW UP NOW
\# IN CONTAINER TERMINAL:
:~/rbkk3-ros2ws$ ros2 launch rbkk3_simulation simulation.launch.py rviz:=true world:=boxes arm_cmd_if:=effort
```
This launch command should launch Gazebo simulator in a world with just 4 boxes (useful to test working of lidar sensor), spawn the mobile manipulator with effort command interfaces and spawn all required ROS2 nodes and launch rviz visualization. 

# 5. Connect with another terminal to the current running container to control the robot
To connect to the container with another terminal, you can make use of the helper script `connect_docker.sh` **after** launching `start_docker_graphics.sh` and in **another** terminal:
```
cd scripts
./connect_docker.sh
\# SOURCING .BASHRC...
\# IN CONTAINER'S NEW TERMINAL:
:~/rbkk3-ros2ws$ ./pub_platform_vel.sh # this will publish velocity commands to the platform.
:~/rbkk3-ros2ws$ ./pub_joint_trajectory.sh # this will publish position commands to the arm
```
The `pub_*.sh` files just provide a quick way to publish a single message to test the robot's controllers. The command topics and reference values are hardcoded inside scripts, so some modification might be required.

# 6. Launch rqt
You can also connect another terminal and launch `rqt` to have some information about topics, controllers, tf trees, node trees, etc.
```
cd scripts
./connect_docker.sh
\# SOURCING .BASHRC...
\# IN CONTAINER'S NEW TERMINAL:
:~/rbkk3-ros2ws$ rqt
```





