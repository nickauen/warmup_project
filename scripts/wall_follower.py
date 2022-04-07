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
        goal_orientation = 90
        linear_speed = 0
        angular_speed = 0
        angular_variable = 0
        goal_distance = 1
        cmd = Twist()

        low_value = None
        index = 0
        for x in data.ranges:
            index += 1
            if (low_value == None or x < low_value):
                low_value = x
                
                current_orientation = index
        
        side_distance = (data.ranges[50] + data.ranges[49] + data.ranges[48] + data.ranges[47] + data.ranges[46] + 
        data.ranges[45] + data.ranges[44] + data.ranges[43] + data.ranges[42] + data.ranges[41])/10

        front_distance = (data.ranges[355] + data.ranges[356] + data.ranges[357] + data.ranges[358] + data.ranges[359] + 
        data.ranges[0] + data.ranges[1] + data.ranges[2] + data.ranges[3] + data.ranges[4])/10
        linear_speed = 0.2

        if (front_distance <= goal_distance):
            
            linear_speed = 0
            if ((current_orientation > 270) and (current_orientation < 85)):
                angular_variable = 1
            
            else:
                angular_variable = -1
            
        
        if (side_distance < goal_distance):
            linear_speed = .2
            angular_speed = 1

        angular_speed = 0.25*angular_variable
        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed

        self.follow_wall_pub.publish(cmd)
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow_Wall()
    node.run()