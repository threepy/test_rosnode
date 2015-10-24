#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def callback(data):

    print data
    print '-----------------'

def test_deviceReturnInfo_pub():
        # init node
    rospy.init_node('deviceReturnInfo_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("deviceReturnInfo", msg.deviceReturnInfo, callback)

    print 'Wait for deviceReturnInfo publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_deviceReturnInfo_pub()
