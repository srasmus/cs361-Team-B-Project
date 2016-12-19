from google.appengine.ext import ndb
from ..classes.StudentCourse import StudentCourse
import random
import logging


class Course(ndb.Model):
    courseID = ndb.StringProperty()
    name = ndb.StringProperty()
    teacher = ndb.KeyProperty(kind="User")

    def getStudents(self):
        student_query = StudentCourse.query(StudentCourse.course==self.key)
        students = []
        for query in student_query:
            student_key = query.student
            students.append(query.student)
        return students

    def enroll(self,student_key):
        pivot = StudentCourse()
        pivot.student = student_key
        pivot.course = self.key
        pivot.put()

    #removes student with key "student" from the course
    def unenroll(self,student_key):
        tmp = StudentCourse.query(StudentCourse.student==student_key and StudentCourse.course==self.key).fetch(1)
        for n in tmp:
            n.key.delete()

    def getTeacher(self):
        return self.teacher.get()