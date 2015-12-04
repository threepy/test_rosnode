#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    print data
    print '--------------------------'


def setHikLabel():
    # init node
    rospy.init_node('setHikLabel_Pub', anonymous=True)
    pub = rospy.Publisher('setHikLabel', String, queue_size=10)
    rate = rospy.Rate(0.2)

    data = '20'
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rospy.loginfo('send msg to the topic: %s', 'setHikLabel')
            rate.sleep()
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    setHikLabel()