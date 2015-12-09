#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def stopSound_pub():
    # init a node
    rospy.init_node('stopSound_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('stopSound', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.5)

    str = 'stop'

    while not rospy.is_shutdown():
        # send
        rospy.loginfo('publish to the topic %s', 'stopSound')
        pub.publish(str)
        rate.sleep()

if __name__ == '__main__':
    try:
        stopSound_pub()
    except rospy.ROSInterruptException:
        pass