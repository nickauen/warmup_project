
# warmup_project

## Warmup Project README
### **DRIVE IN A CIRCLE**

> drive_square.py is a script that makes the turtlebot drive in a square
> indefinitely. To do this, I used a timing method, sending Twist
> signals to the turtlebot to move forward then stop, followed by Twist
> signals to turn in place 90 degrees, and then this is repeated.
> 
> This script was created with a class object (DriveSquare).
> __init__(self) intializes the drive_square node and the publisher that publishes the twist command is also initialized. run(self)
> senpublishesds the messages identifintely on two 5 second loops, one
> that commands the turtlebot to drive forward and the other for it to
> turn in place. The rospy.rate is set to 5Hz and the linear.x and
> angular.z values were adjusted to get the turtlebot to drive in as
> much of square as possible.

  ![IMG_1055_AdobeCreativeCloudExpress](https://github.com/nickauen/warmup_project/blob/4ae733f9280dc2230b6a6ec2e021539c8b49cbdf/IMG_1055_AdobeCreativeCloudExpress.gif)

### **PERSON FOLLOWER**

> person_follower.py is a script that makes the turtlebot follow the
> closest person to it (really the closest *thing* to it). To do this, I
> scanned the data from the LiDAR sensor using the scan topic and found
> which direction from the turtlebot the closest person was. Based on
> this orientation, I calculated the necessary angular velocity to
> orient the turtlebot *0 degrees* relative to the nearest person. The
> turtlebot also stops when it reaches a set distance from this person.
> This script was created with a class object (Follow(object)).  
> **init**(self) initializes the follow_thing node, the publisher that publishes the twist command, and the subscriber that listens for the
> scan topic are also initialized.
> **process_scan** takes in the LiDAR data and iterates through all 360 degrees to find which direction the closest object is relative to the
> turtlebot. This is then transformed into an angular velocity for the
> turtlebot. The turtlebot moves forward towards the person while
> constantly adjusting its orientation relative to them. The distance
> value is calculated by averaging the values measured in the front ~20
> degrees of the robot in order to generate a more stable distance
> measurement.

![Untitled_AdobeCreativeCloudExpress](https://github.com/nickauen/warmup_project/blob/4ae733f9280dc2230b6a6ec2e021539c8b49cbdf/Untitled_AdobeCreativeCloudExpress.gif)
  
### **WALL FOLLOWER**

> wall_follower.py is a script that instructs the turtlebot to drive
> forward until it finds a wall, turn 90 degrees, and then continue to
> drive forward until it finds a corner and turns, continuing
> indefinitely. The turtlebot attempts to stay as parallel to the wall
> as possible while doing this. This script was created with a class
> object (Follow_Wall(object)).  
> **init**(self) initializes the follow_wall node, the publisher that publishes the twist command, and the subscriber that listens for the
> scan topic are also initialized. Similar to that in the
> person_follower.py code, **process_scan** takes in the LiDAR data and
> iterates through all 360 degrees to find which direction the closest
> object is relative to the turtlebot; however, objects that are close
> but are behind or to the right of the robot are excluded since the
> robot only needs to see the wall in front of it or to the left of it.
> All directions around the robot are also tracked in a separate
> variable (*other_orientation_direction*). The robot first finds a wall
> and stops a set distance from it. The robot now turns 90 degrees and
> begins to follow the wall while keeping as close to parallel
> (*current_orientation = 90*) to the wall as possible. By stopping the goal_distance from the wall and staying parallel, 
> the distance from the robot to the wall is kept constant.
> The distance value is calculated by averaging the values measured in the front ~20 degrees
> of the robot in order to generate a more stable distance measurement.

![RenderedVideo_AdobeCreativeCloudExpress](https://github.com/nickauen/warmup_project/blob/4ae733f9280dc2230b6a6ec2e021539c8b49cbdf/RenderedVideo_AdobeCreativeCloudExpress.gif)
  

### **CHALLENGES**
I found understanding what state the robot was in relative to the wall or the person to be particularly difficult, and I struggled to find ways to have the robot know whether it should search for a wall, follow a wall, or round a corner since the LiDAR data from all of these scenarios can look similar) . By incorporating both front distance data and LiDAR data (current orientation) I was able to distinguish between states and orientations of the robot relative to its surroundings. This allowed me to create conditions wherein the robot could adjust its linear and angular velocities depending on the scenario.

### **FUTURE WORK**
Some of my solutions for understanding the robot's current state are not as robust as I would like them to be, and it's likely that there are certain scenarios in which the robot would become confused (multiple tight corners, etc.). I would like to better be able to recognize people in front of the robot. My current implementation often becomes confused when looking at two legs of a person (since there's a gap in the middle) - my LiDAR "seeing" implementation could be more robust with regards to this.

### **TAKEAWAYS**

 - The turtlebot can see in all directions (360 degrees) at once. Understand that you may need to exclude certain data to understand the robot's orientation in order to create a cleaner signal from the LiDAR Scanner. Multiple of these directions can also be combined to understand the robot's orientation as well.
 - Simulation != Reality. The proportional control values vary between simulation and real life which can cause the code that runs perfectly in simulation to fail in reality (and vice versa). Save time to run code *on* the robot.
