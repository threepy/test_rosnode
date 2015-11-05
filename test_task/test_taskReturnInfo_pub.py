#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import taskReturnInfo

def callback(data):

    print data
    print '--------------'

def test_taskReturnInfo_pub():
        # init node
    rospy.init_node('taskReturnInfo_Sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("taskReturnInfo", taskReturnInfo, callback)

    print 'Wait for taskReturnInfo publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_taskReturnInfo_pub()
