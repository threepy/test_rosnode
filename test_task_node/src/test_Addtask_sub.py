#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def test_AddTask_Sub():
    # init a node
    rospy.init_node('test_AddTask_Sub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('addTask', msg.taskInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    # msg data object
    data = msg.taskInfo()

    data.taskID = 0
    data.taskPlanID = 22
    data.taskType = 0
    data.finishAction = 1
    data.taskName = 'name'
    data.devices = [1,2,3]
    data.points = [5,6,8]
    data.forceExec = False

    while not rospy.is_shutdown():
        # send
        pub.publish(data.taskID, data.taskPlanID,data.taskType, data.finishAction, data.taskName, data.devices, data.points, data.forceExec)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'addTask')
        
if __name__ == '__main__':
    try:
        test_AddTask_Sub()
    except rospy.ROSInterruptException:
        pass


