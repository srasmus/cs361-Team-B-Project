import unittest

from ..classes.StudentAcct import StudentAcct
from ..classes.TeacherAcct import TeacherAcct
from ..classes.Course import Course


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.StudentAcct = StudentAcct()

    def tear(self):
        del self.StudentAcct

    def test_initial(self):
        self.assertEqual(self.StudentAcct.firstName, "")
        self.assertEqual(self.StudentAcct.lastName, "")
        self.assertEqual(self.StudentAcct.email, "")
        self.assertTrue(len(self.StudentAcct.courses) == 0)

    def test_makeStudent(self):
        self.setUp()
        self.StudentAcct.makeStudent("John", "Smith", "jsmith@uwm.edu", "12345")
        for i in StudentAcct.query().fetch():
            if i.email == "jsmith@uwm.edu":
                tmp = i
        self.assertEqual(tmp.name, "Smith, John")
        self.assertEqual(tmp.email, "jsmith@uwm.edu")
        """self.assertEqual(tmp.courses[0], "12345")"""
        self.tear()

class Test_TeacherAcct(unittest.TestCase):
    def test_createCourse(self):
        tmp = TeacherAcct("x","y","z")
        q = tmp.createCourse("q")
        self.assertTrue(q.name == "q")
        self.assertTrue(tmp.classes.contains(q))
        self.assertTrue(main.classMasterl.contains(q))
    def test_deleteCourse(self):
        tmp = TeacherAcct("x", "y", "z")
        q = tmp.createCourse("q")
        tmp.deleteCourse(q)
        self.assertFalse(tmp.classes.contains(q) and main.classMasterl.contains(q))
    def test_addStudents(self):
        tmp = TeacherAcct("x","y","z")
        x = Course(tmp,"foo")
        y= tmp.addStudents(x,"a,b,c")
        self.assertTrue(y.has_key("a") and y.has_key("b") and y.has_key("c"))
    def test_removeStudent(self):
        tmp = TeacherAcct("x", "y", "z")
        x = Course(tmp,"foo")
        x.students = {"a":None,"b":None,"c":None}
        tmp.removeStudent(x,"c")
        self.assertTrue(x.students == {"a":None,"b":None})



suite = unittest.TestLoader().loadTestsFromTestCase(StudentTest)
suite2 = unittest.TestLoader().loadTestsFromTestCase(Test_TeacherAcct)
alltests = unittest.TestSuite([suite,suite2])
unittest.TextTestRunner(verbosity=2).run(suite)
