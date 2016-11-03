from teamb2l.Classes.Class import Class
from teamb2l import main

class TeacherAcct():

    #Constructor initializes an empty list of classes an instructor is teaching,
    #as well as add the account to the Master List.
    #Turns the first and last name into a Last, First naming convention
    def __init__(self,firstName,lastName,email,):
        self.name = lastName+", "+firstName
        self.email = email
        self.classes = []
        main.teacherMasterl.append(self)

    #Creates a new Class, adds it to personal class list, and Master
    #Returns the newly created Class
    def createClass(self,name):
        tmp = Class(self,name)
        self.classes.append(tmp)
        main.classMasterl.append(tmp)
        return tmp

    #If the Class exists, it is removed from both lists, and the new teacher level class list is returned
    #Otherwise, None is returned
    def deleteClass(self,clas):
        if self.classes.contains(clas):
            self.classes.remove(clas)
            main.classMasterl.remove(clas)
            return self.classes
        else:
            return None

    #Takes a string of emails separated by commas ","
    #If the Class exists, each student account with that email will be "enrolled" in the class
    #It returns a dictionary of students by (email string, StudentAcct) if students are succesfully enrolled
    #Otherwise, None
    def addStudents(self,clas,students):
        if self.classes.contains(clas):
            clas.enroll(students)
            return clas.students
        else:
            return None

    #Takes the string of a student's email
    #If the Class exists, the student is removed from that Class' student list and the updated list is returned
    # Otherwise, None
    def removeStudent(self,clas,student):
        if self.classes.contains(clas):
            clas.unenroll(student)
            return clas.students
        else:
            return None