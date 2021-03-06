#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    rospy.loginfo(msg)
    

def laser_sub():
    rospy.init_node("laser_scan")

    sub=rospy.Subscriber("/scan", LaserScan, clbk_laser)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        laser_sub()
    except rospy.ROSInterruptException:
        pass