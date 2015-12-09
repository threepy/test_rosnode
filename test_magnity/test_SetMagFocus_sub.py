#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import magInfo

def SetMagFocus_Pub():
    # init a node
    rospy.init_node('SetMagFocus_Pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('SetMagFocus', magInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    data = magInfo()
    data.focus = 580
    data.isSaveTemp = True
    data.taskID = 'a504699e639a4980adba75f9aedaabfa'
    data.deviceID = 'c8e488d06b0046409f5e76746c5b9601'

    while not rospy.is_shutdown():
        # send
        pub.publish(data)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'SetMagFocus')

if __name__ == '__main__':
    try:
        SetMagFocus_Pub()
    except rospy.ROSInterruptException:
        pass