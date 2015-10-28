#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def callback(data):

    print data
    print '-----------------'

def test_hikStatus_pub():
        # init node
    rospy.init_node('hikStatus_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("hikStatus", msg.hikStatus, callback)

    print 'Wait for hikStatus publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_hikStatus_pub()
