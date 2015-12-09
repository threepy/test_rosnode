#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import twoStage


def twoStage_client(taskID, deviceID, pan, tilt):

    rospy.wait_for_service('twoStage',10)
    try:
         # create a handle to the add_two_ints service
        twoStage_handle = rospy.ServiceProxy('twoStage', twoStage)
        resp1 = twoStage_handle(taskID, deviceID, pan, tilt)
        print resp1
        print "----------------------------"
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':

    taskID = 'd630a1f488af4aa2a4d5f366a0494fd6'
    deviceID = '273d08cc881d4371a9e7a9a227a960a3'
    pan = 22.9
    tilt = 12.4

    twoStage_client(taskID, deviceID, pan, tilt)
