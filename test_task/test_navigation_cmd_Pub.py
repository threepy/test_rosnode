#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import String

def callback(data):

    print data
    print '----------------'

def test_navigation_cmd_pub():
        # init node
    rospy.init_node('test_navigation_cmd_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("navigation_cmd", String, callback)

    print 'Wait for navigation_cmd publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_navigation_cmd_pub()
