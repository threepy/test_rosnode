#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs import msg

def deleteTask_pub():
    # init a node
    rospy.init_node('deleteTask_pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('deleteTask', msg.String, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    # msg data object
    str = 'taskname'

    while not rospy.is_shutdown():
        # send
        pub.publish(str)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'deleteTask')
        
if __name__ == '__main__':
    try:
        deleteTask_pub()
    except rospy.ROSInterruptException:
        pass