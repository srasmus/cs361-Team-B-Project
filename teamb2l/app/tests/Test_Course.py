
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from google.appengine.api import memcache
import unittest
from HTMLTestRunner import HTMLTestRunner

from ..classes.User import User
from ..classes.Course import Course
from ..classes.StudentCourse import StudentCourse
from ..classes.faq import FAQ

import logging

class Test_Course(unittest.TestCase):

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

        self.teacher_key = teacher.put()

        self.course = Course(courseID="cs123", name="Some Class")

        self.course.teacher = self.teacher_key

        self.course.put()

        pivot = StudentCourse()
        pivot.student = self.student_key
        pivot.course = self.course.key
        pivot.put()

    def tearDown(self):
        self.testbed.deactivate()

    def test_enroll(self):
        student_key = User(name="test", email="test@test.test", password="1234", permission=0)

        student_key = student_key.put()

        self.assertEquals(len(self.course.getStudents()), 1)

        self.course.enroll(student_key)

        self.assertEquals(len(self.course.getStudents()), 2)

    def test_unenroll(self):
        self.assertEquals(len(self.course.getStudents()), 1)

        self.course.unenroll(self.student_key)

        self.assertEquals(len(self.course.getStudents()), 0)

    def test_get_students(self):
        self.assertEquals(len(self.course.getStudents()), 1)

    def test_get_teacher(self):
        teacher = self.course.getTeacher()
        self.assertEquals(self.teacher_key.get(), teacher)

    def test_get_faq(self):
        
        faq = FAQ(question="test", answer="test", course = self.course.key)
        faq_key = faq.put()

if __name__ == '__main__':
    HTMLTestRunner.main()
