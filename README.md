# Research-Track-Assignment 1
Python Robotics Simulator: This is a simple, portable robot simulator. The objective of this assignemt is to develop a Python code script which is capable to behave correctly inside of a given environment. Additionally, this simulator is developed by Studnet Robotics.

### ABSTRACT

The assignment is based on Pyhton language. Python laguage is an interpreted high-level programming language which is also a general purporsoe programming approach. In this assignment, code is designed to drive an autonomous robot in a given path. A robot is equiped with sensors which can detect boxes around all directions. When robot driving is initiated then robot needs to detect the silver and gold boxes. As the silver box detected in the robot driving path than robot grab that box and place that box to clear it's moving lane and move ahead. If there will be any golden box or boxes detected in the robot moving path than it avoids those box or boxes and find the clear lane to complete journey. In this code there some functions used such as R. see (), R. grab (), R. release (), and so on to perform different functions.    

### INTRODUCTION

This assignment is based on Python script for achieving the behaviour of robot. This robot continously drive around the arena in the counter-clockwise (CCW) direction which avoid touching of the golden box. Also, when the robot is close to the silver box or silver box detected in the robot moving path than it should grab that box and move it behind itself.     

### METHODOLOGY

This section will describe the methodology of the assignment such as behaviour of the robot, different functions used, and so on for achieving the goal. Firstly, pyhton code is developed to define the robot behaviour in a given environment. To detect silver box find_silver_box() is defined and for golden box find_gold_box() is defined. There are enourmous tasks performed by the robot to tour the complete path are as follows:   

###### 1. Robot's drive()

This function is to **DRIVE** the robot in the path. To initiate robot motion drive() is defined. There are two motors variable m0 and m1 being declared. When the direction of m0 and m1 should be same. The amount of speed is given to starts the motor in forward (+) or reverse (-) directions. 

###### 2. Robot's turn()

This function is to **TURN** the robot while moving in the arena. To initiate robot motion turn() is defined. When the same speed is given to motors but with different directions the robot turns.

###### 3. Robot's find_silver_box()

This function is used to recognise the silvcer box. In this two arguments **'a'** & **'w'** which stands for angle between the robot and box & width for the visual field, respectively. R.see() is also called in this function which detects the obstacle on robot's path. Two variables dist and rot_y is declared, which detects the distance and position of the silver box. The value of token.dist compares with the value of dist to check the distance between the robot and the silver box. Also, it checks the type of the whether it is silver or gold and robot moves in the direction towards the silver box if it is in allign with the silver then grabs the silver box. If it returns (-1, -1) it means no silver box is detected on robot's path.                                                                 

###### 4. Robot's find_gold_box()

This function is used to recognise the golden box or wall. In this two arguments **'a'** & **'w'** which stands for angle between the robot and box & width for the visual field, respectively. R.see() is also called in this function which detects the obstacle on robot's path. Two variables dist and rot_y is declared, which detects the distance and position of the golden box or wall. The value of token.dist compares with the value of dist to check the distance between the robot and the golden box or wall. Also, it checks the type of the whether it is silver or gold box. If it returns (-1, -1) it means no golden box or wall is detected on robot's path.  

###### 5. Robot's avoid golden()

This function robot will avoid the golden wall (which is the significance part of the robot's task). Also, robot look for the left and right side to avoid the collision with the golden wall. When the robot finds which side is better than it turns to that particulr side. It also gives priority to right side as robot detected right side is far away from collision with golden box or wall.

###### 6. Robot's right_primacy()

It is defined to check the distance between the robot and the golden wall or box to avoid collision. In this function it compares distance on the left and right side to avoid collision.

###### 7. Robot's grab_silver_box()

This is defined to detect the silver box, grab it, move behind itseld, and move ahead. When it finds the silver box and robot needs to grab the box. R.grab() is called to grab the Silver Box and it turns to the right side. R.release() is called to release the grabbed silver box and last but not the least robot turns left after move behind & release the silver box. Robot also check the alignment for the silver box such as if the robot is aligned with silver box than it moves ahead and grab it or else it align itself to grab.

### RESULT

Pyhton script is read for the execute. The execution can bne done by using command **python run.py RTassignment1.py**. After the execution robot will find the silver box and grabs that box. It also check for the gold box. When it finds the gold box or wall on its path then it avoids that finds the better right to move and continous the path to complete the task.
