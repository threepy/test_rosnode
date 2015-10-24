"""
ptzNormalPub = nh.advertise<dg_msgs::PanTilt>("setBasePtzNormal",20);
hikSetZoomAndFocusPub = nh.advertise<dg_msgs::hikInfo>("setZoomAndFocus",20);

这两发布器写在函数里面,但task.cpp里没有调用,暂时不用
"""