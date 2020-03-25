#! /usr/bin/env python
import rospy
import time
import cv2
from geometry_msgs.msg import Twist
import sys
dist = 0
##### Distance to move #######
#dist = sys.argv[1]   
#### Command to move "w" : to move straight and return , "a" : to move straight and turn right , "b" : to move straight and turn left ####
#com = sys.argv[2]

#INITIALIZE PART
rospy.init_node('move')
pub = rospy.Publisher('/ros0xrobot/cmd_vel', Twist)
rate = rospy.Rate(10)

def straight():
	#MOVEMENT PART
	start_time = time.time()
	while time.time() - start_time < 15:   #2
		t = Twist()
		t.linear.x = 0.15
		print("Linear")
		print(time.time() - start_time)
		pub.publish(t)
		rate.sleep()

	t = Twist()
	t.linear.x = 0
	pub.publish(t)

def straight_custom(dist):
	#MOVEMENT PART
	start_time = time.time()
	while time.time() - start_time < dist:   #2
		t = Twist()
		t.linear.x = 0.15
		print("Linear")
		print(time.time() - start_time)
		pub.publish(t)
		rate.sleep()

	t = Twist()
	t.linear.x = 0
	pub.publish(t)

def rotate_left(fold):
	#ROTATE PART
	start_time = time.time()
	count=0
	cap = cv2.VideoCapture(0)
	while time.time() - start_time < 5.4:
		count+=1
		t=Twist()
		t.angular.z=-1
		pub.publish(t)
		print("Rotation")
		print(time.time() - start_time)
		rate.sleep()
		
		ret, frame = cap.read()
		if count % 5 == 0:
			cv2.imwrite("/home/alpha-2/Desktop/tpa/panaroma/"+str(fold)+"/"+str(count)+".png",frame)
	t = Twist()
	t.angular.z= 0
	pub.publish(t)
	rate.sleep()


def turn_left():
	#ROTATE PART
	start_time = time.time()
	while time.time() - start_time < 2.8:
		t=Twist()
		t.angular.z=1
		pub.publish(t)
		print("Rotation")
		print(time.time() - start_time)
		rate.sleep()

	t = Twist()
	t.angular.z= 0
	pub.publish(t)
	rate.sleep()

def turn_left_custom():
	#ROTATE PART
	start_time = time.time()
	while time.time() - start_time < 1.4:
		t=Twist()
		t.angular.z=1
		pub.publish(t)
		print("Rotation")
		print(time.time() - start_time)
		rate.sleep()

	t = Twist()
	t.angular.z= 0
	pub.publish(t)
	rate.sleep()



def rotate_right():
	#ROTATE PART
	start_time = time.time()
	while time.time() - start_time <5.4:
		t=Twist()
		t.angular.z=1
		pub.publish(t)
		print("Rotation")
		print(time.time() - start_time)
		rate.sleep()

	t = Twist()
	t.angular.z= 0
	pub.publish(t)
	rate.sleep()

def turn_right():
	#ROTATE PART
	start_time = time.time()
	while time.time() - start_time < 2.8:
		t=Twist()
		t.angular.z=-1
		pub.publish(t)
		print("Rotation")
		print(time.time() - start_time)
		rate.sleep()

	t = Twist()
	t.angular.z= 0
	pub.publish(t)
	rate.sleep()

def turn_right_custom(val=1.4):
	#ROTATE PART
	start_time = time.time()
	while time.time() - start_time < val:
		t=Twist()
		t.angular.z=-1
		pub.publish(t)
		print("Rotation")
		print(time.time() - start_time)
		rate.sleep()

	t = Twist()
	t.angular.z= 0
	pub.publish(t)
	rate.sleep()




dist=10
com = 'cus_zig'
print("######################################### Distance is #######################################")
print(dist)
print("######################################### Command is #######################################")
print(com)

#straight()
if com == 'l':
	rotate_left()
elif com == 's':
	straight()
elif com == 'b':
	straight()
	rotate_left(1)
	straight()
	rotate_left(2)
elif com == 'tl':
	#straight()
	turn_left()
elif com == 'tr':
	#straight()
	turn_right()
elif com == 'cus_box':
	straight_custom(25)
	turn_left()
	straight_custom(3)
	turn_left()
	straight_custom(25)
	turn_left()
	straight_custom(3)

### 1 unit = 9 cm in tile floor 

elif com == 'cus_zig':
	straight_custom(6)  ### start ##
	turn_left_custom()  ### pillar side turn diagonal ##
	straight_custom(9)  ### move diagonal ###
	turn_right_custom() ### pillar side turn ###
	straight_custom(8.5) ### pillar side movement ###
	turn_right()         ### turn to pillar width ###
	straight_custom(10)   ### pillar width movement ###
	turn_right()         ### pillar side turn ###
	straight_custom(6)   ### pillar side movement ###
	turn_right_custom(1) ### pillar side turn diagonal ###
	straight_custom(11.2) ### move diagonal ###
	turn_left_custom() ### pillar side turn diagonal ###
	straight_custom(6) ### pillar side movement ###
	turn_left()        ### pillar width turn ###
	straight_custom(6) ### pillar width movement ###

