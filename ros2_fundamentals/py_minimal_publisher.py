#! /usr/bin/env python3  
# use the following intepreter to run this program 
#Tells the python to run python3 on this interpeter 

""" 
Description:
    This ROS 2 node periodically publishes "Hello World" message to a topic
  
---------
Publishing Topics:
    The channel containing the "Hello WOrld" messages
    /py_example_topic - std_msgs/String

Subscription Topics:
    None
"""

import rclpy #Import the ROS 2 client lib for python 
from rclpy.node import Node # Importing node class , used for creating nodes
from std_msgs.msg import String # IMport String message type for ROS 2

class MinmalPyPublisher(Node): #Inheritance from Node
  """Create a minimal Publisher Node



  Args:
      Node (_type_): _description_
  """

  def __init__(self):
    """Create a custon node class for  publishing messages"""

    #initailize the code with a name
    super().__init__('minimal_py_publisher') 

    #Create a publisher on the toSSpic with a queue size of 10 messages 

    self.publisher_1 = self.create_publisher(String,'/py_example_topic',10)

    #create timer with period of 0.5 sec to trigger publishing of message 
    timer_period = 0.5
    self.timer = self.create_timer(timer_period, self.timer_callback)

    #initalize a counter variable for message content 
    self.i =0 

  def timer_callback(self):
    """Callback fxn executed periodically by the timer"""
    #Create a new string message object 
    msg = String()

    # set the mssg data with a counter 
    msg.data = "Hello world: %d" %self.i

    #publish the message you created above to a topic
    self.publisher_1.publish(msg)

    #Log a message indicating the message has been published 
    self.get_logger().info('Publishing: %s'  %msg.data)
    
    self.i +=1 

def main(args=None):
  """Main fxn to start a ros 2 node

  Args:
      args (Lists, optional): Command-line arguments default to none
  """
  rclpy.init(args=args)

  #Create an instance of the minimal publisher node
  minmal_py_publisher =MinmalPyPublisher()

  rclpy.spin(minmal_py_publisher)

  #Destroy the node explicitly
  minmal_py_publisher.destroy_node()

  #shutdown ros2 communicatuion 
  rclpy.shutdown()

if __name__ == '__main__':
    #run the main fxn in the script directly 
  main()



