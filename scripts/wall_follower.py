""" This script publishes ROS messages to make a turtlebot find a wall and follow it """
#!/usr/bin/env python3

from math import dist
from multiprocessing.dummy import current_process
from operator import indexOf
from turtle import distance
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
        goal_distance = 0.6
        cmd = Twist()

        low_value = 50
        index = 0
        for x in range(359):
            if ((data.ranges[x] != 0.0) and (data.ranges[x] < low_value)):
                low_value = data.ranges[x]
               
                current_orientation = x
        
        side_distance = (data.ranges[94] + data.ranges[93] + data.ranges[92] + data.ranges[91] + data.ranges[90] + 
        data.ranges[45] + data.ranges[89] + data.ranges[88] + data.ranges[87] + data.ranges[86])/10

        front_distance = (data.ranges[351] + data.ranges[352] + data.ranges[353] + data.ranges[354] + data.ranges[355] + data.ranges[356] + data.ranges[357] + data.ranges[358] + data.ranges[359] + 
        data.ranges[0] + data.ranges[1] + data.ranges[2] + data.ranges[3] + data.ranges[4] + data.ranges[5] + data.ranges[6] + data.ranges[7] + data.ranges[8] + data.ranges[9])/19

        linear_speed = 0.2
        if ((current_orientation < 15) or (current_orientation > 345)):
            linear_speed = 0.2*front_distance

        if (front_distance <= goal_distance):
            linear_speed = 0.01*front_distance
            if ((current_orientation <= 86) or (current_orientation >= 270)):
                angular_variable = -1
            '''if ((current_orientation >= 94) or (current_orientation < 270)):
                angular_variable = 1'''
       
        elif ((current_orientation <= 93) and (current_orientation >= 87)):
                    angular_variable = 0.0
                    linear_speed = 0.5
                               

        angular_speed = 0.5*angular_variable

        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed

        self.follow_wall_pub.publish(cmd)
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow_Wall()
    node.run()