#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):

    print data
    print 'success'

def test_task_result_Pub():
        # init node
    rospy.init_node('test_task_result_Pub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("task_result", String, callback)

    print 'Wait for test_task publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_task_result_Pub()
