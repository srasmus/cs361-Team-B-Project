"""
from google.appengine.ext import ndb
import unittest
from ..handlers.HTMLTestRunner import HTMLTestRunner

from ..classes.TeacherAcct import TeacherAcct
from ..classes.Course import Course
from ..classes.StudentAcct import StudentAcct

class Test_Course:
    def test_enroll(self):
        tmp = TeacherAcct()
        tmp = tmp.makeTeacher("a","b","c","d",)
        x = Course()
        x = x.makeCourse(tmp,"q")
        x.enroll("a,b,c")
        if x.students.__contains__("a") and x.students.__contains__("b") and x.students.__contains__("c"):
            return "pass"
        else:
            return "fail"


    def test_unenroll(self):
        tmp = TeacherAcct()
        tmp = tmp.makeTeacher("a", "b", "c", "d", )
        x = Course()
        x = x.makeCourse(tmp, "q")
        x.enroll("a,b,c")
        x.unenroll("b")
        if x.students.__contains__("b") == False:
            return "pass"
        else:
            return "fail"

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


if __name__ == '__main__':
    HTMLTestRunner.main()
"""