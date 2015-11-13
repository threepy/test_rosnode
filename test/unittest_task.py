#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg
import unittest

import sqlite3
import urllib
import time
import logging

PKG = 'task'

def init_TimedTask_table():
    url = '/home/robot/sqlite/robotdb.db'
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    logging.info("Delete from TimeTask..")
    conn.execute("DELETE FROM TimedTask")
    conn.commit()

    # get time now
    hour = time.strftime('%H',  time.localtime(time.time()))
    min = time.strftime('%M', time.localtime(time.time()))
    second = time.strftime('%S', time.localtime(time.time()))
    # translate to second
    time_sec = int(hour)*3600 + int(min)*60 + int(second)
    schedule_time = time_sec + 5
    # loopType: 0:立即 1:每天, 2:每周, 3:每月, 4:单次
    # SCHEDULE_PARAM: 每周的周一至周日(1,2,3,4,5,6,7),(1,2,3,...31)每月的1,2,3号
    loopType = 1

    taskname = 'taskname'
    sql = "INSERT INTO TimedTask (taskPlanID, taskName, taskType, loopType, runMode, SCHEDULE_PARAM, SCHEDULE_TIME, finishAction, RecordVideo) \
          VALUES (" + str(id) + ",'" + taskname + "', 1," + str(loopType) + ", 1,'1,2,3,26,30'," + str(schedule_time) + ", 0, 1)"
    conn.execute(sql)
    conn.commit()


class TestTaskNode(unittest.TestCase):

    def setUp(self):
        # init node
        rospy.init_node('test_task', anonymous=True)

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

