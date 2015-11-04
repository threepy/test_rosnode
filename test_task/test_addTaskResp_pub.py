#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import String

def callback(data):

    # print data
    rospy.loginfo('Subscriber from addTaskResp success, get these data:\n%s', data)
    print '-----------------------------------------------------'

def addTaskResp_Sub():
    # init node
    rospy.init_node('addTaskResp_Sub', log_level= rospy.INFO, anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("addTaskResp", String, callback)

    print 'Wait for addTaskResp publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    addTaskResp_Sub()

