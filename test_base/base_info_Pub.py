#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import BaseInfo
from geometry_msgs.msg import Vector3
import sys


def base_info_Pub():
    # init a node
    rospy.init_node('base_info_Pub', log_level=rospy.INFO, anonymous=True)
    # init publisher
    pub = rospy.Publisher('base_info', BaseInfo, queue_size=10)
    # 20 hz
    rate = rospy.Rate(5)

    info = BaseInfo()

    info.odom = Vector3()
    info.odom.x = 10
    info.odom.y = 20
    info.odom.z = 30

    info.velocity = Vector3()
    info.velocity.x = 400
    info.velocity.y = 500
    info.velocity.z = 600

    info.pan = 0
    info.tilt = 0
    info.lArm1 = 1
    info.lArm2 = 2
    info.rArm1 = 3
    info.rArm2 = 4
    info.battery = 500.00
    # info.stopButton = False
    # info.Ultrasonic_forward = False
    # info.Ultrasonic_back = False
    # info.drop_forward = False
    # info.drop_back = False
    # info.softStop = False
    # info.ZERO_steering_wheel = False
    # info.overcurrent = False
    # info.PH_Encoder = False
    # info.Mag_Encoder = False
    # info.Ctrl_Board = False
    # info.ZERO_RobotArm = False
    # info.ZERO_Pantilt = False
    info.ang1 = 10
    info.ang2 = 60

    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(info)
            rospy.loginfo('send msg to the topic: %s', 'base_info')
            rate.sleep()
            info.pan = info.pan + 1
            info.tilt = info.tilt + 1
            if info.pan == sys.maxint or info.pan == sys.maxint:
                info.pan = 0
                info.tilt = 0
        except rospy.ROSException as e:
            rospy.logerr('%s', e)
            break

if __name__ == '__main__':
    try:
        base_info_Pub()
    except rospy.ROSInterruptException:
        pass