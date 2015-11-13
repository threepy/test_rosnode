#!/usr/bin/env python
# -*- coding: utf-8 -*-

PKG = 'task'
NAME = 'test_task'

import rospy, rostest, sys
import unittest
from dg_msgs import msg

class TestTaskNode(unittest.TestCase):

    def __init__(self, *args):
        super(TestTalkerListener, self).__init__(*args)
        self.success = False

    def setUp(self):
    # init node
    rospy.init_node(NAME, anonymous=True)

    def tearDown(self):
        pass

    def addTaskCallback(self, data):
        print(rospy.get_caller_id(), "get data: %s"%data.data)
        self.success = data.data


    def test_addTask(self):
        rospy.Subscriber('addTask', msg.taskInfo, self.addTaskCallback)
        rospy.spin()
        self.assert_(self.success)

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestTaskNode, sys.ar