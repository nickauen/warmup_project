""" This script publishes ROS messages to make a turtlebot find a wall and follow it """
#!/usr/bin/env python3

from math import dist
from multiprocessing.dummy import current_process
from operator import indexOf
import rospy
import numpy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class Follow_Wall(object):
    """ This node published ROS messages to make a turtlebot find a wall and follow it """

    def __init__(self):
        rospy.init_node('follow_wall')
    
        self.follow_wall_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        rospy.Subscriber("/scan", LaserScan, self.process_scan)
        

        rospy.sleep(1)

    def process_scan(self, data):
        goal_orientation = 45
        linear_speed = 0
        angular_speed = 0
        goal_distance = 0.5
        cmd = Twist()

        low_value = None
        index = 0
        for x in data.ranges:
            index += 1
            if (low_value == None or x < low_value):
                low_value = x
                
                current_orientation = index
        
        distance = (data.ranges[50] + data.ranges[49] + data.ranges[48] + data.ranges[47] + data.ranges[46] + 
        data.ranges[45] + data.ranges[44] + data.ranges[43] + data.ranges[42] + data.ranges[41])/10

        if (distance <= goal_distance):
            