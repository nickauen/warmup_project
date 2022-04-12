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
        # Initiates the follow_thing node
        rospy.init_node('follow_thing')
        # Initiates the follow_wall publisher
        self.follow_thing_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # Initiates the scan subscriber
        rospy.Subscriber("/scan", LaserScan, self.process_scan)
        # Give time to set up connections
        rospy.sleep(1)
    
    def process_scan(self, data):
        
        # Initialize variables
        current_orientation = 0
        # Robot stops 0.5 from person
        goal_distance = 0.5
        angular_speed = 0
        linear_speed = 0
        cmd = Twist()

 
        # Initialize low_value to random number
        low_value = 50

        # Iterate through each degree in the scan topic
        for x in range(359):
            # Find which orientation is closest to the robot
            if ((data.ranges[x] != 0.0) and (data.ranges[x] < low_value)):
                # Tracks what direction is closest to the robot via LiDAR
                low_value = data.ranges[x]
               
                current_orientation = x
        
        # Averages the distance values from the fron ~20 degrees of the robot to approximate distance from front
        # Allows robot to stop at walls/corners at specified time
        # Such a large range of degrees helps to give a more stable value
        distance = (data.ranges[351] + data.ranges[352] + data.ranges[353] + data.ranges[354] + data.ranges[355] + data.ranges[356] + data.ranges[357] + data.ranges[358] + data.ranges[359] + 
        data.ranges[0] + data.ranges[1] + data.ranges[2] + data.ranges[3] + data.ranges[4] + data.ranges[5] + data.ranges[6] + data.ranges[7] + data.ranges[8] + data.ranges[9])/19
        
        # Default forward speed
        linear_speed = 0.2
       
       # If robot is not directly facing person, adjust angular speed based on orientation
        if (current_orientation != 0):
            angular_speed = (current_orientation-0)/50
            if ((current_orientation < 360) and (current_orientation > 180)):
                # Flip the velocity values if person is to right of robot
                angular_speed *= -1/10
            
        # Stop when robot reaches 0.5 away from person
        if(distance <= goal_distance):
            linear_speed = 0.0

        # Set speeds to variables
        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed

        # Publish
        self.follow_thing_pub.publish(cmd)
    def run(self):
        # Run indefinitely
        rospy.spin()

if __name__ == '__main__':
    node = Follow()
    node.run()