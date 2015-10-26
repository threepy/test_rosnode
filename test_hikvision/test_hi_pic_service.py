#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import getHikImg
from dg_msgs.msg import hikInfo


def hi_pic_client(hk, isInfrared):

    rospy.wait_for_service('hic_pic',10)
    try:
        # create a handle to the add_two_ints service
        hi_pic_handle = rospy.ServiceProxy('hic_pic', getHikImg)

        rospy.loginfo("Requesting %s",hk)
        resp1 = hi_pic_handle(hk, isInfrared)
        return resp1.state

        rospy.loginfo('return creamra state is: ', resp1.state)
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':

    hk = hikInfo()
    hk.zoom = 0
    hk.focus = 0
    hk.taskID = 0
    hk.deviceID = 12

    isInfrared = True

    hi_pic_client(hk,isInfrared)
