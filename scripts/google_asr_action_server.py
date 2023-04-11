#! /usr/bin/env python3

import rospy, os
import actionlib
import google_asr_action.msg

import audiorec as ar
import asr_file as asr


class GoogleASRAction(object):
    # create messages that are used to publish feedback/result
    _feedback = google_asr_action.msg.GoogleASRFeedback()
    _result = google_asr_action.msg.GoogleASRResult()
    print('STARTING')

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, google_asr_action.msg.GoogleASRAction, execute_cb=self.execute_cb, auto_start = False)
        self.recorder = ar.Recorder()
        self.filepath = '/home/nick/tmp'
        self._as.start()
      
    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        
        # append the seeds for the fibonacci sequence
        #self._feedback.response = ''
        
        rospy.loginfo('Waiting for the user to say something')
        
        # start executing the action
        if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
        
        # Call recaudio here
        #self._feedback.response = str(input("Enter Message"))
        print("GSR:Initiating AudioRec")
        self.recorder.listen()
        n_files = len(os.listdir(self.filepath))-1

        filename = os.path.join(self.filepath, '{}.wav'.format(n_files))
        print("GSR:Asking Google")
        self._feedback.response = asr.transcribe_file(filename)
        if self._feedback.response is None:
             self._feedback.response = "ERROR"

        
        # publish the feedback
        self._as.publish_feedback(self._feedback)
        # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
        r.sleep()
          
        if success:
            self._result.response = self._feedback.response
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)
        
if __name__ == '__main__':
    rospy.init_node('ASR_Node')
    server = GoogleASRAction(rospy.get_name())
    rospy.spin()
