
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from google.appengine.api import memcache
import unittest
from HTMLTestRunner import HTMLTestRunner

from ..classes.User import User
from ..classes.Course import Course
from ..classes.StudentCourse import StudentCourse

import logging

class Test_User(unittest.TestCase):

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

        self.student = User(name="test", email="test@test.test", password="test1234", permission=0)

        student_key = self.student.put()

        self.teacher = User(name="teacher", email="teacher@test.test", password="test1234", permission=1)

        teacher_key = self.teacher.put()

        course = Course(courseID="cs123", name="Some Class")

        course.teacher = teacher_key

        course_key = course.put()

        pivot = StudentCourse()
        pivot.student = student_key
        pivot.course = course_key
        pivot.put()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_courses_for_student(self):
        self.assertEquals(len(self.student.getCoursesStudent()), 1)

    def test_get_courses_for_teacher(self):
        self.assertEquals(len(self.teacher.getCoursesTeacher()), 1)



if __name__ == '__main__':
    HTMLTestRunner.main()
