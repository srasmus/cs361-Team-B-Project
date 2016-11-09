

class Student(object):

    #Constructor initializes an empty list of classes a student is taking,
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.classes = []
<<<<<<< HEAD:teamb2l/app/classes/StudentAcct.py
 
=======
        self.isTA = False

    #Simply assigns a student with basic attributes and adds the class 
    #the student is taking.
    def makeStudent(self, firstName, lastName, email, classID):        
        self.firstName = firstName;
        self.lastName = lastName;
        self.email = email;
        self.classes.append(classID)
        
>>>>>>> 99c03dde727f2ee0884af305de342bd7443b77ac:teamb2l/Classes/StudentAcct.py
