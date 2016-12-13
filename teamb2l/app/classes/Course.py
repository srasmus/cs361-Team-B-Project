from google.appengine.ext import ndb
import StudentAcct
import random


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
    #It then merges the list of strings into the student list
    #Then updates the Course object
    #The updated list is returned
    def enroll(self,studentString):
        tmp = studentString.split(",")
        for i in tmp:
            if self.students.__contains__(i) == False:
                self.students.append(i)
        self.put()
        for e in self.students:
            if StudentAcct.StudentAcct.query().fetch().__contains__(e):
                StudentAcct.StudentAcct.query(StudentAcct.email == e).fetch().courses.append(e.courseID)

        return self.students

    #If the email exists in the list, it is removed and the new list is returned
    #Otherwise, None
    def unenroll(self,email):
        if self.students.__contains__(email):
            self.students.remove(email)
            self.put()
            for e in self.students:
                if StudentAcct.StudentAcct.query().fetch().__contains__(e):
                    StudentAcct.StudentAcct.query(StudentAcct.email == e).fetch().courses.remove(e.courseID)
            return self.students
        else:
            return None