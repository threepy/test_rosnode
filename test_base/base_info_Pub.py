#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.msg import BaseInfo
from geometry_msgs.msg import Vector3
import random


def base_info_Pub():
    # init a node
    rospy.init_node('base_info_Pub', anonymous=True)
    # a publisher,topic name is addTask,msg class is msg.taskInfo
    pub = rospy.Publisher('base_info', BaseInfo, queue_size=10)
    # 10 hz
    rate = rospy.Rate(20)

    odom = Vector3()
    odom.x = 10
    odom.y = 20
    odom.z = 30

    velocity = Vector3()
    velocity.x = 400
    velocity.y = 500
    velocity.z = 600

    pan = 0
    tilt = 0
    lArm1 = 0
    lArm2 = 0
    rArm1 = 0
    rArm2 = 0
    battery = 50
    stopButton = False
    Ultrasonic_forward = False
    Ultrasonic_back = False
    drop_forward = False
    drop_back = False
    softStop = False
    ZERO_steering_wheel = False
    overcurrent = False
    PH_Encoder = False
    Mag_Encoder = False
    Ctrl_Board = False
    ZERO_RobotArm = False
    ZERO_Pantilt = False
    ang1 = 10
    ang2 = 60

    while not rospy.is_shutdown():
        # send
        pub.publish(odom,velocity,pan,tilt,lArm1,lArm2,rArm1,rArm2,battery,stopButton,Ultrasonic_forward,Ultrasonic_back,drop_forward
            ,drop_back,softStop,ZERO_steering_wheel,overcurrent,PH_Encoder,Mag_Encoder,Ctrl_Board,ZERO_RobotArm,ZERO_Pantilt,ang1,ang2)
        rate.sleep()
        pan = pan + 1
        tilt = random.randint(-32768,32767)
        rospy.loginfo('publish to the topic %s', 'base_info')

if __name__ == '__main__':
    try:
        base_info_Pub()
    except rospy.ROSInterruptException:
        pass