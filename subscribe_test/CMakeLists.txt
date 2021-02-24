# %Tag(FULLTEXT)%
cmake_minimum_required(VERSION 2.8.3)
project(subscribe_test)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg my_test)


## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})


## Build service client and server
# %Tag(SRVCLIENT)%
add_executable(client src/client.cpp)
target_link_libraries(client ${catkin_LIBRARIES})
add_dependencies(client my_test)

add_executable(service src/service.cpp)
target_link_libraries(service ${catkin_LIBRARIES})
add_dependencies(service my_test)

add_executable(pub src/pub.cpp)
target_link_libraries(pub ${catkin_LIBRARIES})

add_executable(sub src/sub.cpp)
target_link_libraries(sub ${catkin_LIBRARIES})

find_package(rostest REQUIRED)

add_rostest(test/launch_test.test)

# %EndTag(SRVCLIENT)%

# %EndTag(FULLTEXT)%
