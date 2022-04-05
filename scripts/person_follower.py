""" This script publishes ROS messages to make a turtlebot follow the closest thing to it """
#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class Follow(object):
    """ This node published ROS messages to make a turtlebot follow the closest thing to it """

    def __init__(self):
        rospy.init_node('follow_thing')
    
        self.drive_square_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        rospy.rospy.Subscriber("/scan", LaserScan, self.process_scan)
        

        rospy.sleep(1)

    def process_scan(self, data):
        cmd = Twist()

        if (data.ranges[0] <= 0.5):
            cmd.linear.x = 0.0
        else:

            
        cmd.linear.x = .1
        cmd.angular.z = 0


        self.follow_thing.publish(cmd)
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow()
    node.run()