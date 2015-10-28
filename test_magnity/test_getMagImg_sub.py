#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs import msg

def getMagImg_Pub():
    # init a node
    rospy.init_node('getMagImg_Pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('getMagImg', msg.String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    str = '/home/robot/history/1314691378/mag/getMag/'

    while not rospy.is_shutdown():
        # send
        pub.publish(str)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'getMagImg')

if __name__ == '__main__':
    try:
        getMagImg_Pub()
    except rospy.ROSInterruptException:
        pass