""" This script publishes ROS messages to make a turtlebot drive in a square """
#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist, Vector3

class DriveSquare(object):
    """ This node published ROS messages to make a turtlebot drive in a square """

    def __init__(self):
        rospy.init_node('drive_square')
    
        self.drive_square_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        rospy.sleep(1)

    def run(self):
        r = rospy.Rate(5.0)
        while not rospy.is_shutdown():
            cmd = Twist()
            cmd.linear.x = 0.21
            for i in range(5):
                self.drive_square_pub.publish(cmd)
                rospy.sleep(1)

            cmd = Twist()
            cmd.angular.z = 0.315
            for i in range(5):
                self.drive_square_pub.publish(cmd)
                rospy.sleep(1)

            

if __name__ == '__main__':
        node = DriveSquare()
        node.run()