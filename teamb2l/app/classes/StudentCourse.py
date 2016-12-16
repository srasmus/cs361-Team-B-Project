from google.appengine.ext import ndb

class StudentCourse(ndb.Model):
    student = ndb.KeyProperty(kind="User")
    course = ndb.KeyProperty(kind="Course")