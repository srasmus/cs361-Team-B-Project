from google.appengine.ext import ndb
from Course import Course


class TeacherAcct(ndb.model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    admin = ndb.BooleanProperty()
    courses = ndb.StringProperty(repeated = True)

    #Initializes an empty list of courses an instructor is teaching,
    #as well as add the account to the Master List.
    #Turns the first and last name into a Last, First naming convention
    def makeTeacher(self,firstName,lastName,email,password):
        tmp = TeacherAcct(name = lastName+", "+firstName, email = email, password = password, courses = [])
        tmp.put()

    #Creates a new Course, adds it to personal class list
    #Updates the teacher info in the datastore
    #Returns the newly created Course
    def createCourse(self,name):
        tmp = Course.makeCourse(self,name)
        self.courses.append(tmp)
        self.put()
        return tmp

    #Course is removed from course lists and the new teacher level course list is returned
    #Updates the teacher info in the datastore
    #Otherwise, None is returned
    def removeCourse(self,course):
        if self.courses.contains(course):
            self.courses.remove(course)
            Course.deleteCourse(course)
            self.put()
            return self.courses
        else:
            return None

    #Takes a string of emails separated by commas ","
    #If the Course exists, each student account with that email will be "enrolled" in the class
    #It returns a list of student emails
    #Otherwise, None
    def addStudents(self,course,students):
        if self.courses.contains(course):
            tmp = Course.query(courseID == course).fetch()
            tmp.enroll(students)
            return course.students
        else:
            return None

    #Takes the string of a student's email
    #If the Course exists, the student is removed from that Course's student list and the updated list is returned
    # Otherwise, None
    def removeStudent(self,course,students,teacher):
        if teacher.courses.contains(course):
            tmp = Course.query(courseID == course).fetch()
            tmp.unenroll(students)
            return course.students
        else:
            return None

    #Checks if given teacher is an admin
    #Takes the credentials of a new teacher, and creates a new teacher
    def addTeacher(self,teacher,firstName,lastName,email,password):
        if teacher.admin:
            TeacherAcct.makeTeacher(firstName,lastName,email,password)
        else:
            return None

    # Checks if given teacher is an admin
    # Deletes teacher with email (email)
    def deleteTeacher(self, teacher,email):
        if teacher.admin:
            tmp = TeacherAcct.query(TeacherAcct.email == email).fetch()
            tmp.delete()
        else:
            return None