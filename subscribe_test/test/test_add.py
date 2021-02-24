#!/usr/bin/env python
import sys
import time
import unittest


import rospy
import rostopic


PKG = 'subscribe_test'
NAME = 'test_add'

from my_test.srv import AddTwoInts

class DoTest(unittest.TestCase):
    def __init__(self, *args):
        super(DoTest, self).__init__(*args)
        rospy.init_node('do_test')

        timeout = 10

        self.service_client = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        try:
            self.service_client.wait_for_service(timeout)
        except rospy.exceptions.ROSException as err:
            self.fail(
                "Could not reach SetIO service. Make sure that the driver is actually running."
                " Msg: {}".format(err))
    def test_get_int(self):
        resp = self.service_client(1, 2)
        self.assertEqual(resp.sum, 3)
        
if __name__ == '__main__':
    import rostest
    rostest.run(PKG, NAME, DoTest, sys.argv)
