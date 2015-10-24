#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs import msg

def callback(data):

    print data
    print '--------------------------'

def test_visionTask_pub():
        # init node
    rospy.init_node('test_visionTask_sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("visionTask", msg.visionInfo, callback)
    rospy.loginfo('wait for visionTask topic send message:')
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_visionTask_pub()
