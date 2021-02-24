#include "ros/ros.h"
#include "std_msgs/Int32.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "talker");

  
  ros::NodeHandle n;

  
  ros::Publisher chatter_pub = n.advertise<std_msgs::Int32>("chatter", 1000);
  ros::Publisher test_chatter_pub = n.advertise<std_msgs::Int32>("test_int", 1000);

  ros::Rate loop_rate(10);

  
  int count = 0;
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    std_msgs::Int32 msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = count;

    ROS_INFO("%d", count);
    
    std_msgs::Int32 testMsg;
    testMsg.data = 3;

    
    chatter_pub.publish(msg);
    test_chatter_pub.publish(testMsg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}

