#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    print data
    print '--------------------------'


def setHikFocus():
    # init node
    rospy.init_node('setHikFocus_Pub', anonymous=True)
    pub = rospy.Publisher('setHikFocus', String, queue_size=10)
    rate = rospy.Rate(0.2)

    data = '-1'
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rospy.loginfo('send msg to the topic: %s', 'setHikFocus')
            rate.sleep()
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    setHikFocus()