
from teamb2l import main
class Course():
    courses = []
    #Constructor initializes an empty dict of students enrolled in the class,
    #as well as add the class to the Master List.
    def __init__(self,teacher,name):
        self.teacher = teacher
        self.name = name
        self.students = {}

    #Takes a string of student emails, all separated by commas ","
    #It then parses the list of strings into the dictionary as keys
    #Then it calls the updateDict() method and returns the dictionary
    def enroll(self,studentString):
        tmp = studentString.split(",")
        for i in tmp:
            self.students.update(i,None)
        self.updateDict()
        return self.students

    #If the key exists in the dictionary, it is removed and the new dict is returned
    #Otherwise, None
    def unenroll(self,student):
        if self.students.contains(student):
            self.students.remove(student)
            return self.students
        else:
            return None

    #Goes through the Master List of students, and checks if a student exists with said email
    #If it does, the account is paired with the email string
    #Otherwise, the key has no value, and the method can be called again when the account is created
    def updateDict(self):
        for i in main.courseMasterl:
            if self.students.contains(i.email):
                self.students[i.email] = i