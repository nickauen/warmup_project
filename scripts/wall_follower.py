""" This script publishes ROS messages to make a turtlebot find a wall and follow it """
#!/usr/bin/env python3

from math import dist
from multiprocessing.dummy import current_process
from operator import indexOf
from threading import currentThread
from turtle import distance
import rospy
import numpy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class Follow_Wall(object):
    """ This node published ROS messages to make a turtlebot find a wall and follow it """

    def __init__(self):
        # Initiates the follow_wall node
        rospy.init_node('follow_wall')
        # Initiates the follow_wall publisher
        self.follow_wall_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # Initiates the scan subscriber
        rospy.Subscriber("/scan", LaserScan, self.process_scan)
        # Give time to set up connections
        rospy.sleep(1)
    # Takes in data from the scan topic and turns that data into cmd_vel movements
    def process_scan(self, data):
        # Goal orientation is 90 (the robot should be parallel from the wall)
        
        # Initializing speeds to 0
        linear_speed = 0
        angular_speed = 0
        # Robot should be close to 0.3 away from wall
        goal_distance = 0.3
        #Initialize twist()
        cmd = Twist()

        # Initialize low_value to random number
        low_value = 50
        
        # Iterate through each degree in the scan topic
        for x in range(359):
            # Find which orientation is closest to the robot
            if ((data.ranges[x] != 0.0) and (data.ranges[x] < low_value)):
                # For following the wall, we're not interested in directions behind or to the right of the robot
                if((x < 120) or (x > 320)):
                    low_value = data.ranges[x]
                    # Tracks what direction is closest to the robot via LiDAR
                    current_orientation = x
                # Tracks what direction is closest outside of specified ranges
                other_orientation_direction = x

        # Averages the distance values from the fron ~20 degrees of the robot to approximate distance from front
        # Allows robot to stop at walls/corners at specified time
        # Such a large range of degrees helps to give a more stable value
        front_distance = (data.ranges[351] + data.ranges[352] + data.ranges[353] + data.ranges[354] + data.ranges[355] + data.ranges[356] + data.ranges[357] + data.ranges[358] + data.ranges[359] + 
        data.ranges[0] + data.ranges[1] + data.ranges[2] + data.ranges[3] + data.ranges[4] + data.ranges[5] + data.ranges[6] + data.ranges[7] + data.ranges[8] + data.ranges[9])/17
        
        # If there's nothing in front of the robot or the wall if further than 0.3, and it's current orientation is in front
        # No angular speed, just find a wall
        # The robot stops at the goal_distance from the wall
        if (((front_distance == 0) or (front_distance > goal_distance)) and ((current_orientation < 15) or (current_orientation > 345))):
            linear_speed = 0.15
            # Set speeds to variables
            cmd.linear.x = linear_speed
            cmd.angular.z = angular_speed
            self.follow_wall_pub.publish(cmd)
        
        # If the robot is not aligned with the by a large amount, stop forward movement and fix it
        # Allows for robot to round corners
        elif ((current_orientation < 80) or (other_orientation_direction > 95)):
            # /80 was found to be a reasonable angular speed
            angular_speed = (current_orientation-90)/80
            linear_speed = 0.0
            # Set speeds to variables
            cmd.linear.x = linear_speed
            cmd.angular.z = angular_speed
            self.follow_wall_pub.publish(cmd)

        # Default -- robot moves forward while adjusting orientation relative to wall
        else:
            # /100 was found to be a reasonable angular speed when moving forward
            angular_speed = (current_orientation-90)/100
            linear_speed = 0.2
            # Set speeds to variables
            cmd.linear.x = linear_speed
            cmd.angular.z = angular_speed
            self.follow_wall_pub.publish(cmd)

    # Run indefinitely
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = Follow_Wall()
    node.run()
