#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
get / set hikvsion param
"""
import rospy

def param_hikvision():
    rospy.init_node('param_hivision')

    # fetch a /hikvision_node parameter
    hikvision_node = rospy.get_param("hikvision_node")
    rospy.loginfo("%s is %s", rospy.resolve_name('hikvision_node'), hikvision_node)

    # 获取cameraIP参数
    cameraip = rospy.get_param('/hikvision_node/cameraIP')
    print 'camearIP is %s'%cameraip

    adminID = rospy.get_param('/hikvision_node/adminID')
    print 'adminID is %s'%adminID


    passwd = rospy.get_param('/hikvision_node/password')
    print 'password is %s'%passwd

    channelID = rospy.get_param('/hikvision_node/channelID')
    print 'channelID is %s'%channelID

    # rospy.loginfo('setting parameters..')
    # rospy.set_param('/hikvision_node/photoPath', '/home/robot/catkin/src/hikvision/cfg/photo/lxg')
    # PhotoPath = rospy.get_param('/hikvision_node/photoPath')
    # rospy.loginfo("photo path is %s", PhotoPath)

    # # delete a parameter
    # if rospy.has_param('to_delete'):
    #     rospy.delete_param('to_delete')
    #     rospy.loginfo("deleted %s parameter"%rospy.resolve_name('to_delete'))
    # else:
    #     rospy.loginfo('parameter %s was already deleted'%rospy.resolve_name('to_delete'))
    #
    # search for a parameter
    param_name = rospy.search_param('/hikvision_node/testlxg')
    rospy.loginfo('found testlxg parameter under key: %s'%param_name)

    # publish the value of utterance repeatedly
    # pub = rospy.Publisher(topic_name, String, queue_size=10)
    # while not rospy.is_shutdown():
    #     pub.publish(utterance)
    #     rospy.loginfo(utterance)
    #     rospy.sleep(1)

if __name__ == '__main__':
    try:
        param_hikvision()
    except rospy.ROSInterruptException: pass

