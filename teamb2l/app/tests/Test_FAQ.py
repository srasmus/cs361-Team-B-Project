
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from google.appengine.api import memcache
import unittest
from HTMLTestRunner import HTMLTestRunner

from ..classes.User import User
from ..classes.Course import Course
from ..classes.faq import FAQ

import logging

class Test_FAQ(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

        teacher = User(name="teacher", email="teacher@test.test", password="test1234", permission=1)

        teacher_key = teacher.put()

        self.course = Course(courseID="cs123", name="Some Class")

        self.course.teacher = teacher_key

        self.course.put()

        self.faq = FAQ(question="test", answer="test", course=self.course.key)

        self.faq.put()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_course(self):
        course = self.faq.getCourse()

        self.assertEquals(course, self.course)

if __name__ == '__main__':
    HTMLTestRunner.main()
