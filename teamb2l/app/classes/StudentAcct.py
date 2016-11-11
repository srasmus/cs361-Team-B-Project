

class Student(object):

    #Constructor initializes an empty list of courses a student is taking,
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.password = ""
        self.courses = []

    #Simply assigns a student with basic attributes and adds the class 
    #the student is taking.
    def makeStudent(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

