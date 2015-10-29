#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from dg_msgs.srv import getMagImg
from dg_msgs.msg import magInfo


def get_Imag_client(mg):
    rospy.wait_for_service('mag_pic')
    try:
        getImag = rospy.ServiceProxy('mag_pic', getMagImg)
        resp1 = getImag(mg)
        # 拍照是否成功,照片是否保存到路径
        print resp1
    except rospy.ServiceException, e:
        print 'Service call failed: %s' % e


if __name__ == '__main__':
    mg = magInfo()

    mg.taskID = 1314691379
    mg.deviceID = 1025
    mg.focus = 560
    mg.isSaveTemp = True

    get_Imag_client(mg)
