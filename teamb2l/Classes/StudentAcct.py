from teamb2l.Classes.Class import Class
from teamb2l import main

class StudentAcct():

    #Constructor initializes an empty list of classes a student is taking,
    #as well as add the account to the Master List.
    #Turns the first and last name into a Last, First naming convention
    def __init__(self,firstName,lastName,email,):
        self.name = lastName+", "+firstName
        self.email = email
        self.classes = []
        main.studentMasterl.append(self)

 