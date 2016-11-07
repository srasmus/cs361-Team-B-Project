import unittest

from teamb2l.Classes.TeacherAcct import TeacherAcct
from teamb2l.Classes.Class import Class
from teamb2l import main

class Test_TeacherAcct(unittest.TestCase):
    def test_createClass(self):
        tmp = TeacherAcct("x","y","z")
        q = tmp.createClass("q")
        self.assertTrue(q.name == "q")
        self.assertTrue(tmp.classes.contains(q))
        self.assertTrue(main.classMasterl.contains(q))
    def test_deleteClass(self):
        tmp = TeacherAcct("x", "y", "z")
        q = tmp.createClass("q")
        tmp.deleteClass(q)
        self.assertFalse(tmp.classes.contains(q) and main.classMasterl.contains(q))
    def test_addStudents(self):
        tmp = TeacherAcct("x","y","z")
        x = Class(tmp,"foo")
        y= tmp.addStudents(x,"a,b,c")
        self.assertTrue(y.has_key("a") and y.has_key("b") and y.has_key("c"))
    def test_removeStudent(self):
        tmp = TeacherAcct("x", "y", "z")
        x = Class(tmp,"foo")
        x.students = {"a":None,"b":None,"c":None}
        tmp.removeStudent(x,"c")
        self.assertTrue(x.students == {"a":None,"b":None})


suite = unittest.TestLoader().loadTestsFromTestCase(Test_TeacherAcct)
unittest.TextTestRunner(verbosity=2).run(suite)