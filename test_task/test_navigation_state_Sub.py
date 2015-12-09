#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import String


def navigation_state_Pub():
    # init a node
    rospy.init_node('navigation_state', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('navigation_state', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.3)

    id = 0
    data = 'OnNode:' + str(id) + ' NextNode:2'
    sessionId = '81aa604efcc84ac0895973d7369aee05'

    # while not rospy.is_shutdown():
    for id in range(11): #send for 10 times
        # send
        pub.publish(data, sessionId)
        id = id*10 + 10
        data = 'OnNode:' + str(id) + ' NextNode:20'
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'navigation_state')

if __name__ == '__main__':
    try:
        navigation_state_Pub()
    except rospy.ROSInterruptException:
        pass