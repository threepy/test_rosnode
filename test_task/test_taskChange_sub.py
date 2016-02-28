#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def taskChange_pub():
    # init a node
    rospy.init_node('taskChange_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('taskChange', String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.3)

    while not rospy.is_shutdown():
        # send
        string = '1'
        pub.publish(string)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'taskChange')

if __name__ == '__main__':
    try:
        taskChange_pub()
    except rospy.ROSInterruptException:
        pass


