# Research-Track-Assignment 1
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

This function is used to recognise the silvcer box. In this two arguments **'a'** & **'w'** which stands for angle between the robot and box & width for the visual field, respectively. R.see() is also called in this function which detects the obstacle on robot's path. Two variables dist and rot_y is declared, which detects the distance and position of the silver box.  

