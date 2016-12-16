import unittest

from ..classes.StudentAcct import StudentAcct
from ..classes.TeacherAcct import TeacherAcct
from ..classes.Course import Course
from ..classes.User import User
from ..classes.StudentCourse import StudentCourse

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

    def test_enroll(self):
        self.setUp()
        self.Course = Course(courseID="xyz")
        self.Course.put()
        student = User(email="x@uwm.edu",permission=0)
        student.put()
        self.Course.enroll("x@uwm.edu,y@uwm.edu")
        self.assertEqual(User.query(User.email == "y@uwm.edu").fetch()[0].name, "Unnamed")
        self.assertEqual(User.query(User.email == "x@uwm.edu").fetch()[0].name, None)
        self.assertEqual(StudentCourse.query(StudentCourse.student==student.key).fetch()[0].course.get().courseID, "xyz")
        self.Course.key.delete()
        student.key.delete()
        User.query(User.email == "y@uwm.edu").fetch()[0].key.delete()
        self.tear()


suite = unittest.TestLoader().loadTestsFromTestCase(CourseTest)
alltests = unittest.TestSuite([suite])
unittest.TextTestRunner(verbosity=2).run(suite)
