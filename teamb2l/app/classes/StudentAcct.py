from google.appengine.ext import ndb
import Course

class StudentAcct(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    courses = ndb.StringProperty(repeated = True)


    #Searches through the courses and finds all that contain their email, and adds it to their list
    #Turns name into the last, first naming convention
    #Stores in datastore
    def makeStudent(self, firstName, lastName, email, password):
        tmplist = []
        for i in Course.Course.query().fetch():
            if(i.students.contains(self.email)):
                tmplist.append(i.courseID)
        tmp = StudentAcct(name = str(lastName+", "+firstName), email = email,password = password,courses = tmplist)
        tmp.put()