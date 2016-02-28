#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):

    print data
    print '----------------'

def test_magstatus_Pub():
        # init node
    rospy.init_node('test_magstatus_Pub', anonymous=True)

    # subscribe from 'addTask' publisher
    rospy.Subscriber("magStatus", String, callback)
    rospy.loginfo('wait for magstatus topic send message:')
    #bolock until node is shutdown
    rospy.spin()

if __name__ == '__main__':
    test_magstatus_Pub()
