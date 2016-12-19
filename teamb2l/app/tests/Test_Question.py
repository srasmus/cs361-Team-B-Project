import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from ..classes.Course import Course
from ..classes.Question import Question
from ..tests.HTMLTestRunner import HTMLTestRunner


class Test_Question(unittest.TestCase):
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

    def test_get_questions_course(self):
        self.course = Course(courseID="cs123", name="Some Class")
        self.course.put()

        self.question = Question.createQuestion(self, "Test Student", self.course.name, "Test Question", "Test Content")

        self.assertEquals(Question.query(Question.course == self.course.name).get(), self.question)

if __name__ == '__main__':
    HTMLTestRunner.main()