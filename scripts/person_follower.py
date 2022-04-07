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
        angular_constant = 0.8
        goal_distance = 0.3
        angular_speed = 0
        linear_speed = 0
        linear_constant = 0.5
        cmd = Twist()

 
        
        low_value = 50
        index = 0
        for x in range(359):
            if ((data.ranges[x] != 0.0) and (data.ranges[x] < low_value)):
                low_value = data.ranges[x]
               
                current_orientation = x
        
        
        distance = (data.ranges[351] + data.ranges[352] + data.ranges[353] + data.ranges[354] + data.ranges[355] + data.ranges[356] + data.ranges[357] + data.ranges[358] + data.ranges[359] + 
        data.ranges[0] + data.ranges[1] + data.ranges[2] + data.ranges[3] + data.ranges[4] + data.ranges[5] + data.ranges[6] + data.ranges[7] + data.ranges[8] + data.ranges[9])/19
        
        """if ((current_orientation < 25) or (current_orientation > 330)):
            angular_speed = 0.0
            linear_speed = linear_constant*distance"""

        linear_speed = linear_constant*distance/2
        if ((current_orientation <= 25) or (current_orientation >= 340)):
            linear_speed = linear_constant*distance

        if ((current_orientation > 10) and (current_orientation <= 180)):
            angular_speed = angular_constant*(current_orientation/2)
          

        if ((current_orientation < 350) and (current_orientation > 180)):
            angular_speed = -1*(angular_constant*(1/current_orientation))*500
            

        """if ((current_orientation > 90) and (current_orientation < 270)):
            linear_speed = 0.0"""
        
        if(distance <= goal_distance):
            linear_speed = 0.0

        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed


        self.follow_thing_pub.publish(cmd)
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow()
    node.run()