from google.appengine.ext import ndb

class StudentCourse(ndb.Model):
    student = ndb.KeyProperty(kind="User")
    course = ndb.KeyProperty(kind="Course")

    def getStudent(self):
    	return self.student.get()

    def getCourse(self):
    	return self.course.get()