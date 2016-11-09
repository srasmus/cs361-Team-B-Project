

class Student(object):

    #Constructor initializes an empty list of courses a student is taking,
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.courses = []

    #Simply assigns a student with basic attributes and adds the class 
    #the student is taking.
    def makeStudent(self, firstName, lastName, email, courseID):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.courses.append(courseID)

