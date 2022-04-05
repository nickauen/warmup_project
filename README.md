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

  ![ezgif-4-3050593917](https://user-images.githubusercontent.com/102747072/161753490-9fe40fa6-f2b1-4357-807d-7da3c5a33703.gif)

---
## README Instructions
A high-level description (a few sentences): Describe the problem and your approach at a high-level. Include any relevant diagrams or pictures that help to explain your approach.
Code explanation (a couple of sentences per function): Describe the structure of your code. For the functions you wrote, describe what each of them does.
A gif: Record a gif of the physical robot performing the behavior. Include this gif in your writeup and use it for analysis if needed.

Challenges (1 paragraph): Describe the challenges you faced programming these robot behaviors and how you overcame them.
Future work (1 paragraph): If you had more time, how would you improve your robot behaviors?
Takeaways (at least 2 bullet points with a few sentences per bullet point): What are your key takeaways from this project that would help you/others in future robot programming assignments? For each takeaway, provide a few sentences of elaboration.
