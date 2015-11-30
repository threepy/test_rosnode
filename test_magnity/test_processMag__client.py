#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import magSrv
from dg_msgs.msg import processMag
from dg_msgs.msg import point


def processMag_client(pmag):
    rospy.wait_for_service('processMag')
    try:
        processMag = rospy.ServiceProxy('processMag', magSrv)
        resp1 = processMag(pmag)

        print resp1
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':
    pmag = processMag()

    pmag.taskID = '565c5e27099048f0b91d0f16051a0d2d'
    pmag.deviceID = 5

    pt1 = point()
    pt1.x = 384*0.2
    pt1.y = 288*0.2
    pmag.p1 = pt1

    pt2 = point()
    pt2.x = 384*0.8
    pt2.y = 288*0.8
    pmag.p2 = pt2

    processMag_client(pmag)