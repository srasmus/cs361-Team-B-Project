from google.appengine.ext import ndb
from StudentAcct import StudentAcct
import random


class Course(ndb.model):
    courseID = ndb.StringProperty()
    teacher = ndb.StringProperty()
    name = ndb.StringProperty()
    students = ndb.StringProperty(repeated = True)


    #Takes a TeacherAcct object and a name for the class
    #a unique class id is generated from the teacher's email and a random number
    #it makes sure the ID is unique
    #Then stores it in the datastore
    def makeCourse(self,teacher,name):
        id = teacher.email+":"+random.randint(0,1000)
        if teacher.courses.contains(id) == False:
            tmp = Course(courseID = id, teacher = teacher.email, name = name, students = [])
            tmp.put()
        else:
            Course.makeCourse(teacher,name)

    #Takes a string of student emails, all separated by commas ","
    #It then merges the list of strings into the student list
    #Then updates the Course object
    #The updated list is returned
    def enroll(self,studentString):
        tmp = studentString.split(",")
        for i in tmp:
            if self.students.contains(i) == False:
                self.students.append(i)
        self.put()
        for e in self.students:
            if StudentAcct.query().fetch().contains(e):
                StudentAcct.query(StudentAcct.email == e).fetch().courses.append(e.courseID)

        return self.students

    #If the email exists in the list, it is removed and the new list is returned
    #Otherwise, None
    def unenroll(self,email):
        if self.students.contains(email):
            self.students.remove(email)
            self.put()
            for e in self.students:
                if StudentAcct.query().fetch().contains(e):
                    StudentAcct.query(StudentAcct.email == e).fetch().courses.remove(e.courseID)
            return self.students
        else:
            return None