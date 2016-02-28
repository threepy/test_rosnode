#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    print data
    print '--------------------------'


def getHikImg_Pub():
    # init node
    rospy.init_node('getHikImg_Pub', anonymous=True)
    pub = rospy.Publisher('getHikImg', String, queue_size=10)
    rate = rospy.Rate(0.2)

    data = 'test'
    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rospy.loginfo('send msg to the topic: %s', 'getHikImg')
            rate.sleep()
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    getHikImg_Pub()