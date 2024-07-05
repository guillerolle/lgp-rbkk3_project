# CMake generated Testfile for 
# Source directory: /home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager
# Build directory: /home/duser/ros2_kortex-ros2ws/build/controller_manager
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_controller_manager "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_controller_manager.txt" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager.gtest.xml")
set_tests_properties(test_controller_manager PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;92;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_controller_manager_with_namespace.cpp "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager_with_namespace.cpp.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_controller_manager_with_namespace.cpp.txt" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager_with_namespace.cpp" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager_with_namespace.cpp.gtest.xml")
set_tests_properties(test_controller_manager_with_namespace.cpp PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager_with_namespace.cpp" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;100;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_load_controller "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_load_controller.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_load_controller.txt" "--append-env" "AMENT_PREFIX_PATH=_Release" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_load_controller" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_load_controller.gtest.xml")
set_tests_properties(test_load_controller PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_load_controller" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;108;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_controllers_chaining_with_controller_manager "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controllers_chaining_with_controller_manager.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_controllers_chaining_with_controller_manager.txt" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controllers_chaining_with_controller_manager" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controllers_chaining_with_controller_manager.gtest.xml")
set_tests_properties(test_controllers_chaining_with_controller_manager PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controllers_chaining_with_controller_manager" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;117;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_controller_manager_srvs "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager_srvs.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_controller_manager_srvs.txt" "--append-env" "AMENT_PREFIX_PATH=_Release" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager_srvs" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager_srvs.gtest.xml")
set_tests_properties(test_controller_manager_srvs PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager_srvs" TIMEOUT "120" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;125;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_controller_manager_urdf_passing "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager_urdf_passing.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_controller_manager_urdf_passing.txt" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager_urdf_passing" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_controller_manager_urdf_passing.gtest.xml")
set_tests_properties(test_controller_manager_urdf_passing PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_controller_manager_urdf_passing" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;138;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_release_interfaces "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_release_interfaces.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_release_interfaces.txt" "--append-env" "AMENT_PREFIX_PATH=_Release" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_release_interfaces" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_release_interfaces.gtest.xml")
set_tests_properties(test_release_interfaces PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_release_interfaces" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;160;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_spawner_unspawner "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_spawner_unspawner.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_spawner_unspawner.txt" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_spawner_unspawner" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_spawner_unspawner.gtest.xml")
set_tests_properties(test_spawner_unspawner PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_spawner_unspawner" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;169;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
add_test(test_hardware_management_srvs "/usr/bin/python3" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_hardware_management_srvs.gtest.xml" "--package-name" "controller_manager" "--output-file" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/ament_cmake_gmock/test_hardware_management_srvs.txt" "--command" "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_hardware_management_srvs" "--gtest_output=xml:/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_results/controller_manager/test_hardware_management_srvs.gtest.xml")
set_tests_properties(test_hardware_management_srvs PROPERTIES  LABELS "gmock" REQUIRED_FILES "/home/duser/ros2_kortex-ros2ws/build/controller_manager/test_hardware_management_srvs" TIMEOUT "60" WORKING_DIRECTORY "/home/duser/ros2_kortex-ros2ws/build/controller_manager" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;106;ament_add_test;/opt/ros/humble/share/ament_cmake_gmock/cmake/ament_add_gmock.cmake;52;_ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;177;ament_add_gmock;/home/duser/ros2_kortex-ros2ws/src/ros2_control/controller_manager/CMakeLists.txt;0;")
subdirs("gmock")
subdirs("gtest")
