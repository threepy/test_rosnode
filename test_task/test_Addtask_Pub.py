#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def callback(data):

    # print data
    rospy.loginfo('Subscriber from addTask success, get these data:\n%s', data)
    print '-----------------------------------------------------'

def AddTask_Sub():
    # init node
    rospy.init_node('addTask_Sub', log_level= rospy.INFO, anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("addTask", msg.taskInfo, callback)

    print 'Wait for addTask publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    AddTask_Sub()

