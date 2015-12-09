#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def startSound_pub():
    # init a node
    rospy.init_node('startSound_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('startSound', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.5)

    str = 'start'

    while not rospy.is_shutdown():
        # send
        rospy.loginfo('publish to the topic %s', 'startSound')
        pub.publish(str)
        rate.sleep()

if __name__ == '__main__':
    try:
        startSound_pub()
    except rospy.ROSInterruptException:
        pass