#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import hikPTZCtrl

def callback(data):
    print data
    print '--------------------------'


def hikPtzUsage():
    # init node
    rospy.init_node('hikPtzUsage_Pub', anonymous=True)
    pub = rospy.Publisher('hikPtzUsage', hikPTZCtrl, queue_size=10)
    rate = rospy.Rate(0.2)

    data = hikPTZCtrl()
    data.dwPTZCommand = 121
    data.dwStop = 12
    data.dwSpeed = 2
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rospy.loginfo('send msg to the topic: %s', 'hikPtzUsage')
            rate.sleep()
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    hikPtzUsage()