#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def audio_cmd_pub():
    # init a node
    rospy.init_node('audio_cmd_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('audio_cmd', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.3)

    str = 'voltage'

    while not rospy.is_shutdown():
        # send
        pub.publish(str)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'audio_cmd')

if __name__ == '__main__':
    try:
        audio_cmd_pub()
    except rospy.ROSInterruptException:
        pass