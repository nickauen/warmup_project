""" This script publishes ROS messages to make a turtlebot drive in a square """
#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist, Vector3

class DriveSquare(object):
    """ This node published ROS messages to make a turtlebot drive in a square """

    def __init__(self):
        # Initiates the drive_square node
        rospy.init_node('drive_square')
        # Initiates the publisher for drive_square (publishes Twist)
        self.drive_square_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        # Sleep to ensure node connections are established
        rospy.sleep(1)

    def run(self):
        r = rospy.Rate(5.0) # 5Hz
        while not rospy.is_shutdown():
            cmd = Twist()
            cmd.linear.x = 0.21 # Sets forward movement vector
            for i in range(5): # Iterates 5 times
                self.drive_square_pub.publish(cmd)
                rospy.sleep(1)

            cmd = Twist()
            cmd.angular.z = 0.315 # Sets angular (spinning) movement vector
            for i in range(5): # Iterates 5 times
                self.drive_square_pub.publish(cmd)
                rospy.sleep(1)

            

if __name__ == '__main__':
    # Run the node
        node = DriveSquare()
        node.run()