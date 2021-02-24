#!/usr/bin/env python
import sys
import time
import unittest


import rospy
import rostopic


PKG = 'subscribe_test'
NAME = 'test_add'

from std_msgs.msg import Int32

class DoTest(unittest.TestCase):
    def __init__(self, *args):
        super(DoTest, self).__init__(*args)
        rospy.init_node('listener_test')

        
    def test_get_int(self):
        test_int = rospy.wait_for_message('test_int', Int32)
        self.assertEqual(test_int.data, 3)
        
if __name__ == '__main__':
    import rostest
    rostest.run(PKG, NAME, DoTest, sys.argv)
