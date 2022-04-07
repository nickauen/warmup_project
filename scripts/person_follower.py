""" This script publishes ROS messages to make a turtlebot follow the closest thing to it """
#!/usr/bin/env python3

from math import dist
from multiprocessing.dummy import current_process
from operator import indexOf
import rospy
import numpy

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
        goal_orientation = 0
        angular_constant = .01
        goal_distance = 0.5
        angular_speed = 0
        linear_speed = 0
        cmd = Twist()


        low_value = None
        
        index = 0
        for x in data.ranges:
            index += 1
            if (low_value == None or x < low_value):
                low_value = x
                
                current_orientation = index
        
        distance = (data.ranges[355] + data.ranges[356] + data.ranges[357] + data.ranges[358] + data.ranges[359] + 
        data.ranges[0] + data.ranges[1] + data.ranges[2] + data.ranges[3] + data.ranges[4])/10
        
        
        if ((current_orientation > 0) and (current_orientation <= 180)):
            angular_speed = angular_constant*current_orientation/2
            linear_speed = 0.25

        if ((current_orientation < 359) and (current_orientation > 180)):
            angular_speed = angular_constant*current_orientation/2*-1
            linear_speed = 0.25

        if ((current_orientation > 90) and (current_orientation < 270)):
            linear_speed = 0.0
        
        if((distance > 9) or (distance <= goal_distance)):
            linear_speed = 0.0

        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed


        self.follow_thing_pub.publish(cmd)
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow()
    node.run()