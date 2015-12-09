#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import recSound


def recordSound_client(taskID, deviceID, recLast):

    rospy.wait_for_service('recordSound',10)
    try:
        # create a handle to the service
        recordSound_handle = rospy.ServiceProxy('recordSound', recSound)
        resp = recordSound_handle(taskID, deviceID, recLast)
        rospy.loginfo('return is: ', resp)
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':
    taskID = 'd630a1f488af4aa2a4d5f366a0494fd6'
    deviceID = '01acf75582064325a84cbef62e9ae767'
    recLast = 12

    recordSound_client(taskID, deviceID, recLast)
