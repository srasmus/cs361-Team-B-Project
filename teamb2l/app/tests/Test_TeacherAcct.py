

from ..classes.TeacherAcct import TeacherAcct
from ..classes.Course import Course

class Test_TeacherAcct:
    def test_createCourse(self):
        tmp = TeacherAcct()
        tmp = tmp.makeTeacher("a", "b", "c", "d", )
        q = tmp.createCourse("q")
        if tmp.courses.__contains__("q"):
            return "pass"
        else:
            return "fail"
    def test_removeCourse(self):
        tmp = TeacherAcct()
        tmp = tmp.makeTeacher("a", "b", "c", "d", )
        tmp.createCourse("q")
        tmp.removeCourse("q")
        if tmp.courses.__contains__("q") == False:
            return "pass"
        else:
            return "fail"
    def test_addStudents(self):
        tmp = TeacherAcct()
        tmp = tmp.makeTeacher("a", "b", "c", "d", )
        x = tmp.createCourse("q")
        tmp.addStudents("q","f")
        if x.students.__contains__("f"):
            return "pass"
        else:
            return "fail"
    def test_removeStudent(self):
        tmp = TeacherAcct()
        tmp = tmp.makeTeacher("a", "b", "c", "d", )
        x = tmp.createCourse("q")
        tmp.addStudents("q", "f")
        tmp.removeStudent("q", "f",tmp)
        if x.students.__contains__("f") == False:
            return "pass"
        else:
            return "fail"

