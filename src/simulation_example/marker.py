#!/usr/bin/env python

PACKAGE_NAME = 'rviz'
import roslib; roslib.load_manifest(PACKAGE_NAME)
import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, Point, Vector3, Quaternion
from std_msgs.msg import ColorRGBA



rospy.init_node('Narko_base_marker')
marker_pub = rospy.Publisher('Narko_base_marker', Marker)

def make_marker(marker_type, scale, r, g, b, a):
    # make a visualization marker array for the occupancy grid
    m = Marker()
    m.action = Marker.ADD
    m.header.frame_id = '/narko_base_link'
    m.header.stamp = rospy.Time.now()
    m.ns = 'marker_test_%d' % marker_type
    m.id = 0
    m.type = marker_type
    m.pose.orientation.y = 0
    m.pose.orientation.w = 1
    m.scale = scale
    m.color.r = 0;
    m.color.g = 1;
    m.color.b = 0;
    m.color.a = 0.9;
    m.color.r = r;
    m.color.g = g;
    m.color.b = b;
    m.color.a = a;
    return m

 
while not rospy.is_shutdown():
    rospy.loginfo('Publishing Narko_base_marker')
    scale = Vector3(0.66,0.60,0.30)
    marker_pub.publish(make_marker(Marker.CUBE, scale, .2, 1, .5, .3))
    rospy.sleep(1.0)
