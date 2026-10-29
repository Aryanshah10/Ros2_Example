cmake_minimum_required(VERSION 3.8)
project(ros2_fundamentals)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
set(dependencies
rclcpp
std_msgs)

include_directories(
  include
)
#add_executable(minimal_cpp src/minimal_cpp_publisher.cpp)
#ament_traget_dependencies(minimal_cpp_publisher ${dependencies})

#add_executable(minimal_cpp src/minimal_cpp_subscriber.cpp)
#ament_traget_dependencies(minimal_cpp_subscriber ${dependencies})

install(
  DIRECTORY ros2_fundamentals scripts
  DESTINATION share/${PROJECT_NAME}
)
install(
  DIRECTORY include
  DESTINATION include
)

#incstall cpp executables
#install(
#TARGET
#minimal_cpp_publisher
#minimal_cpp_subscriber
#DESTINATION lib/${PROJECT_NAME}
#)

#Instal Python modules for import
ament_python_install_package(${PROJECT_NAME})

#Add this section to install python scripts
install(
  PROGRAMS
  ros2_fundamentals/py_minimal_publisher.py
  ros2_fundamentals/py_minimal_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_include_directories(include)

ament_package()
