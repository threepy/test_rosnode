#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt32

def callback(data):
    print data
    print '--------------------------'


def setHikFocus():
    # init node
    rospy.init_node('setHikFocus_Pub', anonymous=True)
    pub = rospy.Publisher('setHikFocus', UInt32, queue_size=10)
    rate = rospy.Rate(0.2)

    data = 100
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rate.sleep()
            rospy.loginfo('send msg to the topic: %s', 'setHikFocus')
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    setHikFocus()