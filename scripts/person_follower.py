""" This script publishes ROS messages to make a turtlebot follow the closest thing to it """
#!/usr/bin/env python3

from operator import indexOf
import rospy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class Follow(object):
    """ This node published ROS messages to make a turtlebot follow the closest thing to it """

    def __init__(self):
        rospy.init_node('follow_thing')
    
        self.follow_thing_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        rospy.Subscriber("/scan", LaserScan, self.process_scan)
        

        rospy.sleep(1)

    def process_scan(self, data):
        cmd = Twist()


        low_value = None
        index = 0
        for x in data.ranges:
            index += 1
            if (low_value == None or x < low_value):
                low_value = x
                
                holdvalue = index
        if (holdvalue < 90):
            print("front")  # Directly in front
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

        if ((holdvalue >= 90) and (holdvalue < 180)):
            print("left") # Directly to the left
            cmd.angular.z = 0.0

        if((holdvalue >=180) and (holdvalue < 270)):
            print("behind") # Directly behind
            cmd.linear.x = 0.0
            cmd.angular.z = .25

        if((holdvalue >= 270)):
            print("right") # Directly to the right


        self.follow_thing_pub.publish(cmd)
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow()
    node.run()