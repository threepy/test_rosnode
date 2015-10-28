#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import SetPanTilt
from dg_msgs.msg import PanTilt


def setBasePtzBlock_client(pantilt):
    rospy.wait_for_service('setBasePtzBlock')
    try:
        processImg = rospy.ServiceProxy('setBasePtzBlock', SetPanTilt)
        resp1 = processImg(pantilt)

        print resp1
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':

    pantilt = PanTilt()
    pantilt.pan = 124
    pantilt.tilt = 32

    setBasePtzBlock_client(pantilt)