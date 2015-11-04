#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import String

def callback(data):

    # print data
    rospy.loginfo('Subscriber from deleteTaskResp success, get these data:\n%s', data)
    print '-----------------------------------------------------'

def deleteTaskResp_Sub():
    # init node
    rospy.init_node('deleteTaskResp_Sub', log_level= rospy.INFO, anonymous=True)

    # subscribe topic
    rospy.Subscriber("deleteTaskResp", String, callback)

    print 'Wait for deleteTaskResp publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    deleteTaskResp_Sub()

