#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg
import unittest

class TestTaskNode(unittest.TestCase):

    def setUp(self):
        # init node
        rospy.init_node('test_task_node', anonymous=True)
    def tearDown(self):
        pass

    def addTaskcallback(self,data):

        print data
        list1 = [data.taskID, data.taskPlanID, data.taskType, data.finishAction, data.taskName, data.devices, data.points, data.forceExec]
        list2 = [0,1,1,1,'name',(),(),False]

        self.assertListEqual(list1,list2,'failed')
        # print data
        # rospy.loginfo('Subscriber from addTask success, get these data:\n%s', data)
        # print '-----------------------------------------------------'
        rospy.signal_shutdown('stop subscribe addTask')

    def test_AddTask_Pub(self):

        # subscribe from 'addTask' publisher
        rospy.Subscriber("addTask", msg.taskInfo, self.addTaskcallback)

        rospy.loginfo('subscribe addTask topic, and wait for message')
        #bolock until node is shutdown
        rospy.spin()

    def testII(self):
        print 'aaa'

    # def test_AddTask_Sub(self):
    #     pub = rospy.Publisher('addTask', msg.taskInfo, queue_size=10)
    #     # 10 hz
    #     rate = rospy.Rate(10)
    #
    #     # msg data object
    #     data = msg.taskInfo()
    #
    #     data.taskID = 0
    #     data.taskPlanID = 22
    #     data.taskType = 0
    #     data.finishAction = 1
    #     data.taskName = 'name'
    #     data.devices = []
    #     data.points = []
    #     data.forceExec = False
    #
    #     while not rospy.is_shutdown():
    #         # send
    #         pub.publish(data)
    #         rate.sleep()
    #         rospy.loginfo('publish to the topic %s', 'addTask')
    #         print '1212'


if __name__ == '__main__':
    unittest.main()

