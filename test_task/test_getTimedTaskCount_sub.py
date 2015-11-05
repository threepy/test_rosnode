#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def getTimedTaskCount_Pub():
    # init a node
    rospy.init_node('getTimedTaskCount_Pub', anonymous=True)
    # a publisher,topic name
    pub = rospy.Publisher('getTimedTaskCount', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(1)

    # msg data object
    str = '00000000000000000000000002748859'

    while not rospy.is_shutdown():
        # send
        pub.publish(str)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'getTimedTaskCount')
        
if __name__ == '__main__':
    try:
        getTimedTaskCount_Pub()
    except rospy.ROSInterruptException:
        pass