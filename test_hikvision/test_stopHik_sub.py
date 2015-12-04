#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    print data
    print '--------------------------'


def stopHik_Pub():
    # init node
    rospy.init_node('stopHik_pub', anonymous=True)
    pub = rospy.Publisher('stopHik', String, queue_size=10)
    rate = rospy.Rate(0.2)

    data = 'stopHik'
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rospy.loginfo('send msg to the topic: %s', 'stopHik')
            rate.sleep()
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    stopHik_Pub()