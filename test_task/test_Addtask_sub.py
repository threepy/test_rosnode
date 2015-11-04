#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def addTask_pub():
    # init a node
    rospy.init_node('addTask_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('addTask', msg.taskInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    # msg data object
    data = msg.taskInfo()

    data.sessionId = '00000000000000000000000002748856'
    data.loopType = 1
    data.runMode = 1
    data.taskPlanID = 462972512
    data.taskType = 1
    data.finishAction = 0
    data.taskName = 'taskname1'
    data.devices = '1,2,3,4,5,6,7,8,9,10'
    data.points = '45,32'
    data.execTime = 35293
    data.execDate = '20151104'
    data.forceExec = False
    data.recordVideo = True

    while not rospy.is_shutdown():
        # send
        pub.publish(data)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'addTask')

if __name__ == '__main__':
    try:
        addTask_pub()
    except rospy.ROSInterruptException:
        pass


