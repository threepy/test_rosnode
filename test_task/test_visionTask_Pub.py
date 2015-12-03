#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import visionInfo

def callback(data):

    print data
    print '--------------------------'

def visionTask_sub():
        # init node
    rospy.init_node('visionTask_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("visionTask", visionInfo, callback)
    rospy.loginfo('wait for visionTask topic send message:')
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    visionTask_sub()
