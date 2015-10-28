#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import ChargerInfo

def charger_info_Pub():
    # init a node
    rospy.init_node('charger_info_Pub', anonymous=True)
    # a publisher,topic name
    pub = rospy.Publisher('charger_info', ChargerInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(0.1)

    # msg data object
    data = ChargerInfo()
    data.batteryVoltage = 56.55
    data.batteryCurrent = 45.23
    data.expowerVoltage = 32.12
    data.expowerCurrent = 23.22
    data.windSpeed = 12.34
    data.windDirect = 2.12
    data.temperature = 43.31
    data.humidity = 2.13

    while not rospy.is_shutdown():
        # send
        pub.publish(data)
        rate.sleep()
        rospy.loginfo('publish to the topic %s', 'charger_info')
        
if __name__ == '__main__':
    try:
        charger_info_Pub()
    except rospy.ROSInterruptException:
        pass