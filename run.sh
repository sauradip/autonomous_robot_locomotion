source /opt/ros/kinetic/setup.bash
source catkin_ws/devel/setup.bash

roscore

#open new terminal and repeat lines 1 and 2

rosrun ros0xrobot ros0xrobotNode

#open new terminal and repeat lines 1 and 2
#place this basic_move.py in catkin_ws/src/ros0xrobot/src/ path

cd catkin_ws/src/ros0xrobot/src/
python basic_move.py

