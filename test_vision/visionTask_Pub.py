#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def visionTask_Pub():
    # init a node
    rospy.init_node('visionTask_Pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('visionTask', msg.visionInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    # msg data object
    data = msg.visionInfo()

    data.taskID = 205605164
    data.state = 1




    while not rospy.is_shutdown():
        # send
        pub.publish(data)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'visionTask')

if __name__ == '__main__':
    try:
        visionTask_Pub()
    except rospy.ROSInterruptException:
        pass



