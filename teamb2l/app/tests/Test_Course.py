from google.appengine.ext import ndb

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

