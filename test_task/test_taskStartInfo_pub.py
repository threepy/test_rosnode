#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import taskStartInfo

def callback(data):

    print data
    print '--------------'

def test_taskStartInfo_pub():
        # init node
    rospy.init_node('taskStartInfo_Sub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("taskStartInfo", taskStartInfo, callback)

    print 'Wait for taskStartInfo publisher send msg'
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_taskStartInfo_pub()
