#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import String

def deleteTask_pub():
    # init a node
    rospy.init_node('deleteTask_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('deleteTask', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(1)

    # msg data object
    str = '1'
    sessionId = '00000000000000000000000002748856'

    while not rospy.is_shutdown():
        # send
        pub.publish(str, sessionId)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'deleteTask')
        
if __name__ == '__main__':
    try:
        deleteTask_pub()
    except rospy.ROSInterruptException:
        pass