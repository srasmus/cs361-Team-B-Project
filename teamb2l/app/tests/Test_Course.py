import unittest

from teamb2l.app.classes.TeacherAcct import TeacherAcct
from teamb2l.app.classes.Course import Course
from teamb2l import main

class Test_Course(unittest.TestCase):

    def test_enroll(self, studentString):
        tmp = TeacherAcct("x","y","z")
        q = Course(tmp,"q")
        x = q.enroll("a,b,c")
        self.assertTrue(x == {"a":None,"b":None,"c":None})

    def test_unenroll(self, student):
        tmp = TeacherAcct("x", "y", "z")
        q = Course(tmp, "q")
        q.students = {"a":None,"b":None,"c":None}
        x = q.unenroll("b")
        self.assertTrue(x == {"a":None,"c":None})

    def test_updateDict(self):
        tmp = TeacherAcct("x", "y", "z")
        q = Course(tmp, "q")
        q.students = {"a":None,"b":None,"c":None}
        x = StudentAcct()
        x.email = "a"
        main.studentMasterl = [x]
        y = q.updateDict()
        self.assertTrue(y == {"a":x,"b":None,"c":None})

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Course)
unittest.TextTestRunner(verbosity=2).run(suite)