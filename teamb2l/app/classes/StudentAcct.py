from google.appengine.ext import ndb
from Course import Course

class StudentAcct(ndb.model):
    name = ndb.StringProperty
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    courses = ndb.StringProperty(repeated = True)


    #Searches through the courses and finds all that contain their email, and adds it to their list
    #Turns name into the last, first naming convention
    #Stores in datastore
    def makeStudent(self, firstName, lastName, email, password):
        tmplist = []
        for i in Course.query().fetch():
            if(i.students.contains(self.email)):
                tmplist.append(i.courseID)
        tmp = StudentAcct(name = lastName+", "+firstName,email = email,password = password,courses = tmplist)
        tmp.put()