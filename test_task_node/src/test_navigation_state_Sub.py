#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs import msg

def navigation_state_Pub():
    # init a node
    rospy.init_node('navigation_state', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('navigation_state', msg.String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    str = '1'

    while not rospy.is_shutdown():
        # send
        pub.publish(str)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'navigation_state')

if __name__ == '__main__':
    try:
        navigation_state_Pub()
    except rospy.ROSInterruptException:
        pass