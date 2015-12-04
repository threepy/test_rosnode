#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import hikVideo

def videoSrv_client(bStart, taskID):

    rospy.wait_for_service('videoSrv',10)
    try:
        # create a handle to the add_two_ints service
        videoSrv_handle = rospy.ServiceProxy('videoSrv', hikVideo)
        resp = videoSrv_handle(bStart, taskID)
        return resp.state
        rospy.loginfo('return videoSrv state is: ', resp.state)
    except rospy.ServiceException, e:
        print 'Service call failed: %s'%e

if __name__ == '__main__':
    bStart = False # 1: start 0: stop
    taskID = '1234'

    videoSrv_client(bStart, taskID)
