import unittest

from teamb2l.Classes.TeacherAcct import TeacherAcct
from teamb2l.Classes.Class import Class
from teamb2l import main

class Test_Class(unittest.TestCase):

    def test_enroll(self, studentString):
        tmp = TeacherAcct("x","y","z")
        q = Class(tmp,"q")
        x = q.enroll("a,b,c")
        self.assertTrue(x == {"a":None,"b":None,"c":None})

    def test_unenroll(self, student):
        tmp = TeacherAcct("x", "y", "z")
        q = Class(tmp, "q")
        q.students = {"a":None,"b":None,"c":None}
        x = q.unenroll("b")
        self.assertTrue(x == {"a":None,"c":None})

    def test_updateDict(self):
        tmp = TeacherAcct("x", "y", "z")
        q = Class(tmp, "q")
        q.students = {"a":None,"b":None,"c":None}
        x = StudentAcct()
        x.email = "a"
        main.studentMasterl = [x]
        y = q.updateDict()
        self.assertTrue(y == {"a":x,"b":None,"c":None})

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Class)
unittest.TextTestRunner(verbosity=2).run(suite)