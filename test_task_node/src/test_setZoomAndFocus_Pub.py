#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import hikInfo


def callback(data):
    print data
    print '--------------------------'


def test_SetHikZoomAndFocus_Pub():
    # init node
    rospy.init_node('test_SetHikZoomAndFocus', anonymous=True)

    # hikvison节点订阅此SetHikZoomAndFocus话题
    rospy.Subscriber("SetHikZoomAndFocus", hikInfo, callback)
    rospy.loginfo('wait for SetHikZoomAndFocus topic send message:')
    # bolock until node is shutdown
    rospy.spin()


if __name__ == '__main__':
    test_SetHikZoomAndFocus_Pub()
