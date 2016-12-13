import unittest

from ..classes.StudentAcct import StudentAcct
from ..classes.TeacherAcct import TeacherAcct
from ..classes.Course import Course
from ..classes.User import User


class CourseTest(unittest.TestCase):
    def setUp(self):
        self.Course = Course()

    def tear(self):
        del self.Course

    def test_makeCourse(self):
        self.setUp()
        teacher = User(email="x@uwm.edu",permission=1)
        teacher.put()
        tmp = self.Course.makeCourse(teacher.key,"name")
        tmp.put()
        self.assertEqual(tmp.name, "name")
        self.assertEqual(tmp.teacher.get().email, "x@uwm.edu")
        self.assertEqual(Course.query(Course.courseID==tmp.courseID).fetch(), [])
        teacher.key.delete()
        tmp.key.delete()
        self.tear()

suite = unittest.TestLoader().loadTestsFromTestCase(CourseTest)
alltests = unittest.TestSuite([suite])
unittest.TextTestRunner(verbosity=2).run(suite)
