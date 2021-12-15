from __future__ import print_function
import time
from sr.robot import *
#RSEARCH TRACK ASSIGNMENT 1
#The robot is equiped with the sensors which can detect boxes around all directions (from -180.0 degrees to 180.0 degrees).
#this python code is for achieving robot's behaviour in the defined enivronment
#Robot drive continously around the path in the counter-clockwise (CCW) direction
#Avoiding the golden boxes
#When the robot is near to silver box than it grabs that box, move behind itself that box and later continous it's path

"""o_th is the threshold for orientation checking variables"""
o_th = 2.0 
"""l_th is the threshold for linear distance variable"""
l_th = 0.4
#l_thg is the threshold for linear distance value to avoid collision with gold box or boxes
l_thg = 0.8
#c_th threshold for linear distance to choose direction
c_th = 2.0

R = Robot() #Robot class

#drive() is defined for velocity to drive the robot and two arguments spd (SPEED for the wheels) & sec (SECOND for the time interval) is passed
def drive(spd, sec):            
    R.motors[0].m0.power = spd
    R.motors[0].m1.power = spd
    time.sleep(sec)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

#turn() is defined to turn the robot and two arguments spd (SPEED for the wheels) & sec (SECOND for the time interval) is passed
def turn(spd, sec):
    R.motors[0].m0.power = spd
    R.motors[0].m1.power = -spd
    time.sleep(sec)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

"""find_silver_box() is defined to find the silver box which is near to robot"""
def find_silver_box(a, w):
#two arguments a (angle between the robot & box) & w (width for the visual field) is passed
	dist = 100
	for token in R.see():
	    if token.dist < dist and token.info.marker_type == MARKER_TOKEN_SILVER and (a-w) <= token.rot_y <= (a + w):                 
#checking the closest silver box
	       dist = token.dist
	       #nearest silver box distance
	       rot_y = token.rot_y 
	       #angle between the robot and silver box
        if dist == 100:
               return -1, -1    #(-1,-1) when no silver box is detected in the robot's path
        else:
             return dist, rot_y
             
"""find_gold_box() is defined to find the gold box which is near to robot"""
def find_gold_box(a, w):
#two arguments a (angle between the robot box) & w (width for the visual field) is passed
	dist = 100
	for token in R.see():
	    if token.dist < dist and token.info.marker_type == MARKER_TOKEN_GOLD and (a-w) <= token.rot_y <= (a + w):                   #checking the closest silver box
	       dist = token.dist            #nearest silver box distance
	       rot_y = token.rot_y          #angle between the robot and silver box
        if dist == 100:
               return -1, -1    #(-1,-1) when no gold box is detected in the robot's path
        else:
             return dist, rot_y 
             
"""avoid_golden() is defined to find the gold wall which is in robot's path"""
def avoid_golden():
#in this function robot will avoid the golden wall (which is the significance part of the robot's task). Also, robot look for the left and right side to avoid the collision with the golden wall. When the robot finds which side is better than it turns to that particulr side.  
	dist, rot_y = find_gold_box(0, 60)
	
	if dist == -1:
	       return  
	       
	if dist < l_thg:
	    print("Ahh!! Golden Wall or Box on my (robot's) way")
	    right = right_primacy()    #giving priority to right side as robot detected right side is far away from collision with golden box or wall
	    
	    if right:
	        while(dist<c_th):
	    	   turn(15,0.1)
	    	   print("Turning to right side as right is best side to avoid collision")
	    	   dist, rot_y = find_gold_box(0,15)
	    else:
	        while(dist<c_th):
	    	   turn(-15,0.1)
	    	   print("Turning to left side as left is best side to avoid collision")
	    	   dist, rot_y = find_gold_box(0,15)
#right_primacy() is defined to check the distance between the robot and the golden wall or box to avoid collision	    
def right_primacy():
   
    dist_r, rot_yr = find_gold_box(90, 10)
    print("Distance on the right =", str(dist_r))
    dist_l, rot_yl = find_gold_box(-90, 10)
    print("Distance on the left =", str(dist_l))
    
    if dist_l < dist_r:           #comparing distance on the left and right side to avoid collision
       return True
       
    else:
       return False

#grab_silver_box() is defined to detect the silver box, grab it, move behind itseld, and move ahead
def grab_silver_box():

    dist, rot_y = find_silver_box(0,70)
    if dist == -1:      #-1 if no silver box detected on robot's path
           print("Ohh!! No silver box found till yet!!")
           return
    dist_gold, rot_ygold = find_gold_box(rot_y, 35)
    
    if dist_gold < dist:
    		  return
    while True:
       dist, rot_y = find_silver_box(0,90)
       if dist < l_th:
              print("Ahh!! Silver Box!! Grab it!!")
              R.grab()        #R.grab() called to grab the Silver Box
              print("Turning Right side to release the silver box")
              turn(35,1)      #turning right
              R.release()     #R.release() called to release the grabbed silver box
              turn(-35,1)     #turning left after moving behind & releasing the silver box
              return
       elif -o_th <= rot_y <= o_th:   #if the robot is aligned with silver box than it moves ahead and grab it or else it align itself to grab
               print("Moving ahead towards silver box")
               drive(40, 1)
       elif rot_y < -o_th:
       #for right
            print("Realligning to Right")
            turn(-1, 0.5)
       elif rot_y > o_th:
       #for left
            print("Realligning to Left")
            turn(1, 0.5) 
       return

while 1:   
	 drive(40,0.1)
	 avoid_golden() 
	 grab_silver_box()      
"""calling grab_silver_box() & avoid_golden"""    
