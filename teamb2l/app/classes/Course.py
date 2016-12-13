from google.appengine.ext import ndb
from ..classes.StudentCourse import StudentCourse
import random
from ..classes.User import User


class Course(ndb.Model):
    courseID = ndb.StringProperty()
    name = ndb.StringProperty()
    teacher = ndb.KeyProperty(kind="User")

    #a unique class id is generated from the teacher's email and a random number
    #it makes sure the ID is unique
    #Then stores it in the datastore
    def makeCourse(self,teacher,name):
        id = teacher.get().email+":"+str(random.randint(0,1000))
        if Course.query(Course.courseID == id).fetch():
            Course.makeCourse(teacher, name)
        else:
            tmp = Course(courseID=id, teacher=teacher, name=name)
            return tmp

    #Takes a string of student emails, all separated by commas ","
    #Then updates the Course object
    def enroll(self,studentString):
        students = studentString.split(",")
        courses = StudentCourse.query(StudentCourse.course==self.key).fetch()
        for i in students:
            if courses:
                for course in courses:
                    if course.student.get().email==i:
                        i.remove()
        for student in students:
            if User.query(User.email==student).fetch() == []:
                tmp = User(name="Unnamed",email=student,password="1234",permission=0)
                tmp.put()
                pivot = StudentCourse(student=tmp.key,course=self.key)
                pivot.put
            else:
                tmp = User.query(User.email==student).fetch()[0]
                pivot = StudentCourse(student=tmp.key, course=self.key)
                pivot.put

        self.put()


    #removes student with key "student" from the course
    def unenroll(self,student):
        tmp = StudentCourse.query(StudentCourse.student==student and StudentCourse.course==self.key)
        tmp.key.delete()