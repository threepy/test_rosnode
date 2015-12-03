#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import taskInfo

def addTask_pub():
    # init a node
    rospy.init_node('addTask_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('addTask', taskInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.5)

    # msg data object
    data = msg.taskInfo()

    data.sessionId = '00000000000000000000000002748856'
    data.loopType = 0 # loopType: 0:立即 1:每天, 2:每周, 3:每月, 4:单次
    data.runMode = 1
    data.taskPlanID = '1234'
    data.taskType = 1
    data.finishAction = 0
    data.taskName = 'task_run_now'
    data.devices = '1,2,3,4,5,6'
    data.points = '4'
    data.execTime = '17:37:12'


    data.execDate = '1,2,3,4'
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


