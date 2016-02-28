#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from visualization_msgs.msg import Marker

NODE = 'test_move'
TOPIC = 'testMove'

def movePub():
    # init a node
    rospy.init_node(NODE, log_level=rospy.INFO, anonymous=True)
    # init publisher
    pub = rospy.Publisher(TOPIC, Marker, queue_size=10)
    # 20 hz
    rate = rospy.Rate(1)
    data = Marker()
    data.ns = 'test'
    data.id = 0
    data.type = 0
    data.action = 0




    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(data)
            rospy.loginfo('send msg to the topic: %s', TOPIC)
            rate.sleep()

        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    try:
        movePub()
    except rospy.ROSInterruptException:
        pass