#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rospy import Time
import rospy
import time
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import PoseStamped, Pose, PointStamped, PoseWithCovarianceStamped
import actionlib
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult, MoveBaseActionGoal, MoveBaseActionResult
from move_base_msgs.msg import MoveBaseActionGoal

x = [1.7, -0.4, -2.0]
y = [1.6, -0.3, -2.0]
w = 0.7
z = 1.0
ix = 0
iy = 0

if __name__ == '__main__':
    rospy.init_node('supermarket')
    print("Init Loop")
    client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    client.wait_for_server()
    pose_stamp = MoveBaseGoal()
    pose_stamp.target_pose.header.frame_id = "map"
    pose_stamp.target_pose.pose.position.x = x[ix]
    pose_stamp.target_pose.pose.position.y = y[iy]
    pose_stamp.target_pose.pose.orientation.z = z
    pose_stamp.target_pose.pose.orientation.w = w
    pose_stamp.target_pose.header.stamp = rospy.Time.now()
    feedback = MoveBaseFeedback()
    goal_status = GoalStatusArray()
    client.send_goal(pose_stamp)

    for points in range(100):
        for ix in range(3):
            point = ix + iy
            pose_stamp.target_pose.header.frame_id = "map"
            pose_stamp.target_pose.pose.position.x = x[ix]
            pose_stamp.target_pose.pose.position.y = y[iy]
            pose_stamp.target_pose.pose.orientation.z = z
            pose_stamp.target_pose.pose.orientation.w = w
            pose_stamp.target_pose.header.stamp = rospy.Time.now()
            feedback = MoveBaseFeedback()
            goal_status = GoalStatusArray()
            client.send_goal(pose_stamp)
            print("Point:" + str(point))
            time.sleep(20)
            for iy in range(3):
                point = ix + iy
                pose_stamp.target_pose.header.frame_id = "map"
                pose_stamp.target_pose.pose.position.x = x[ix]
                pose_stamp.target_pose.pose.position.y = y[iy]
                pose_stamp.target_pose.pose.orientation.z = z
                pose_stamp.target_pose.pose.orientation.w = w
                pose_stamp.target_pose.header.stamp = rospy.Time.now()
                feedback = MoveBaseFeedback()
                goal_status = GoalStatusArray()
                client.send_goal(pose_stamp)
                print("Point:" + str(point))
                time.sleep(20)
            ix = 0
            iy = 0
            print("New loop")
    rospy.spin()