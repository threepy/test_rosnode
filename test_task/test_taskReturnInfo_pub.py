#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def callback(data):

    print data
    print '--------------'

def test_taskReturnInfo_pub():
        # init node
    rospy.init_node('taskReturnInfo_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("taskReturnInfo", msg.taskInfo, callback)

    print 'Wait for taskReturnInfo publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_taskReturnInfo_pub()
