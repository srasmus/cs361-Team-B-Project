
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from google.appengine.api import memcache
import unittest
from HTMLTestRunner import HTMLTestRunner

from ..classes.User import User
from ..classes.Course import Course
from ..classes.StudentCourse import StudentCourse

import logging

class Test_Student_Course(unittest.TestCase):

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

        student = User(name="test", email="test@test.test", password="test1234", permission=0)

        self.student_key = student.put()

        teacher = User(name="teacher", email="teacher@test.test", password="test1234", permission=1)

        teacher_key = teacher.put()

        course = Course(courseID="cs123", name="Some Class")

        course.teacher = teacher_key

        self.course_key = course.put()

        self.pivot = StudentCourse()
        self.pivot.student = self.student_key
        self.pivot.course = self.course_key
        self.pivot.put()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_student(self):
        student = self.pivot.getStudent()
        self.assertEquals(self.student_key, student.key)

    def test_get_course(self):
        course = self.pivot.getCourse()
        self.assertEquals(self.course_key, course.key)



if __name__ == '__main__':
    HTMLTestRunner.main()
