#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import hikInfo

def callback(data):
    print data
    print '--------------------------'


def setHikZoomAndFocus_Pub():
    # init node
    rospy.init_node('setHikZoomAndFocus_Pub', anonymous=True)
    pub = rospy.Publisher('setHikZoomAndFocus', hikInfo, queue_size=10)
    rate = rospy.Rate(0.2)

    hk = hikInfo()
    hk.zoom = 0 # min: 0 max: 16381
    hk.focus = 49153 # min: 4096 max: 49152
    hk.taskID = '123'
    hk.deviceID = '158'

    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(hk)
            rospy.loginfo('send msg to the topic: %s', 'setHikZoomAndFocus')
            rate.sleep()
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    setHikZoomAndFocus_Pub()