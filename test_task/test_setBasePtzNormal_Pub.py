#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import PanTilt

def callback(data):

    print data
    print '----------------'

def setBasePtzNormal_sub():
        # init node
    rospy.init_node('setBasePtzNormal_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("setBasePtzNormal", PanTilt, callback)

    print 'Wait for setBasePtzNormal publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    setBasePtzNormal_sub()
