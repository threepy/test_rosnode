#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def callback(data):

    # print data
    rospy.loginfo('Subscriber from addTask success, get these data:\n%s', data)
    print '-----------------------------------------------------'

def test_AddTask_Pub():
    # init node
    rospy.init_node('AddTask_Subscriber_test', log_level= rospy.DEBUG, anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("addTask", msg.taskInfo, callback)

    print 'Wait for addTask publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_AddTask_Pub()

