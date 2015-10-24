#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import magSrv
from dg_msgs.msg import processMag
from dg_msgs.msg import point


def process_Img_client(pmag):
    rospy.wait_for_service('processMag')
    try:
        processImg = rospy.ServiceProxy('processMag', magSrv)
        resp1 = processImg(pmag)

        print resp1
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':
    pmag = processMag()

    pmag.path = '/home/robot/test_magnity/2015-09-09 16-53-06.ddt'

    pt1 = point()
    pt1.x = 384
    pt1.y = 248

    pmag.p1 = pt1

    pt2 = point()
    pt2.x = 30
    pt2.y = 240

    pmag.p2 = pt2

    process_Img_client(pmag)