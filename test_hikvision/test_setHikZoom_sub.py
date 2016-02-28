#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt32

def callback(data):
    print data
    print '--------------------------'


def setHikZoom_Pub():
    # init node
    rospy.init_node('setHikZoom_pub', anonymous=True)
    pub = rospy.Publisher('setHikZoom', UInt32, queue_size=10)
    rate = rospy.Rate(0.2)

    data = 0
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rate.sleep()
            rospy.loginfo('send msg to the topic: %s', 'setHikZoom')
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    setHikZoom_Pub()