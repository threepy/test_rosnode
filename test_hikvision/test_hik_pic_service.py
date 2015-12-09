#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import getHikImg
from dg_msgs.msg import hikInfo


def hi_pic_client(hk, isInfrared):

    rospy.wait_for_service('hik_pic',10)
    try:
        # create a handle to the add_two_ints service
        hi_pic_handle = rospy.ServiceProxy('hik_pic', getHikImg)

        rospy.loginfo("Requesting %s",hk)
        resp1 = hi_pic_handle(hk, isInfrared)
        return resp1.state

        rospy.loginfo('return creamra state is: ', resp1.state)
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':

    hk = hikInfo()
    hk.zoom = 99
    hk.focus = 31421 # min:4096
    hk.taskID = 'd630a1f488af4aa2a4d5f366a0494fd6'
    hk.deviceID = '4b43b0aee35624cd95b910189b3dc231'

    isInfrared = False

    hi_pic_client(hk,isInfrared)
