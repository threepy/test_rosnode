#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header



def pose_Pub():
    # init a node
    rospy.init_node('pose_pub', log_level=rospy.INFO, anonymous=True)
    # init publisher
    pub = rospy.Publisher('pose', PoseStamped, queue_size=10)
    # 20 hz
    rate = rospy.Rate(1)

    poseStamped = PoseStamped()
    poseStamped.header = Header()
    poseStamped.header.frame_id = '0'

    poseStamped.pose = Pose()
    poseStamped.pose.position = Point()
    poseStamped.pose.position.x = 0
    poseStamped.pose.position.y = 0
    poseStamped.pose.position.z = 0

    poseStamped.pose.orientation = Quaternion()
    poseStamped.pose.orientation.x = 0
    poseStamped.pose.orientation.y = 0
    poseStamped.pose.orientation.z = 0
    poseStamped.pose.orientation.w = 0


    while not rospy.is_shutdown():
        try:
            # send
            pub.publish(poseStamped)
            rospy.loginfo('send msg to the topic: %s', 'pose')
            rate.sleep()
            poseStamped.pose.position.x = poseStamped.pose.position.x + 1
            poseStamped.pose.position.y = poseStamped.pose.position.y + 1
        except rospy.ROSException as e:
            rospy.logerr('%s', e)

if __name__ == '__main__':
    try:
        pose_Pub()
    except rospy.ROSInterruptException:
        pass