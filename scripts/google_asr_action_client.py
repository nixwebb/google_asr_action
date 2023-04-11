#! /usr/bin/env python3
from __future__ import print_function

import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import google_asr_action.msg

def trial_client():

    client = actionlib.SimpleActionClient('ASR_Node', google_asr_action.msg.GoogleASRAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = google_asr_action.msg.GoogleASRGoal(msg = 'ask for stuff')

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result() 

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('google_asr_client_py')
        print('Asking for stuff')
        result = trial_client()
        print("Result:", result.response)
    except rospy.ROSInterruptException:
        print("program interrupted before completion")
