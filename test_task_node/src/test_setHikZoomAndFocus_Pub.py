#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import hikInfo


def callback(data):
    print data
    print '--------------------------'


def SetHikZoomAndFocus_sub():
    # init node
    rospy.init_node('SetHikZoomAndFocus_sub', anonymous=True)

    # hikvison节点订阅此SetHikZoomAndFocus话题
    rospy.Subscriber("setHikZoomAndFocus", hikInfo, callback)
    rospy.loginfo('wait for SetHikZoomAndFocus topic send message:')
    # bolock until node is shutdown
    rospy.spin()


if __name__ == '__main__':
    SetHikZoomAndFocus_sub()
