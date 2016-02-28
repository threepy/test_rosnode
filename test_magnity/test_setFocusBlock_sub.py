#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt32

def setFocusBlock_Pub():
    # init a node
    rospy.init_node('setFocusBlock_Pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('setFocusBlock', UInt32, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    data = 400

    while not rospy.is_shutdown():
        # send
        pub.publish(data)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'setFocusBlock')

if __name__ == '__main__':
    try:
        setFocusBlock_Pub()
    except rospy.ROSInterruptException:
        pass