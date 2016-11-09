from teamb2l.app.classes.Course import Course

class TeacherAcct():
    teachers = []

    #Constructor initializes an empty list of courses an instructor is teaching,
    #as well as add the account to the Master List.
    #Turns the first and last name into a Last, First naming convention
    def __init__(self,firstName,lastName,email):
        self.name = lastName+", "+firstName
        self.email = email
        self.courses = []
        self.admin = False

    #Creates a new Course, adds it to personal class list, and Master
    #Returns the newly created Course
    def createCourse(self,name):
        tmp = Course(self,name)
        self.courses.append(tmp)
        Course.courses.append(tmp)
        return tmp

    #If the Course exists, it is removed from both lists, and the new teacher level class list is returned
    #Otherwise, None is returned
    def deleteCourse(self,course):
        if self.courses.contains(course):
            self.courses.remove(course)
            Course.courses.remove(course)
            return self.courses
        else:
            return None

    #Takes a string of emails separated by commas ","
    #If the Course exists, each student account with that email will be "enrolled" in the class
    #It returns a dictionary of students by (email string, StudentAcct) if students are succesfully enrolled
    #Otherwise, None
    def addStudents(self,course,students):
        if self.courses.contains(course):
            course.enroll(students)
            return course.students
        else:
            return None

    #Takes the string of a student's email
    #If the Course exists, the student is removed from that Course' student list and the updated list is returned
    # Otherwise, None
    def removeStudent(self,course,student):
        if self.courses.contains(course):
            course.unenroll(student)
            return course.students
        else:
            return None

    def addTeacher(self,teacher):
        if self.admin:
            # if ~TeacherAcct.teachers.contains(teacher):
                TeacherAcct.teachers.append(teacher)
        else:
            return None

    def removeTeacher(self, teacher):
        if self.admin:
            if TeacherAcct.teachers.contains(teacher):
                TeacherAcct.teachers.remove(teacher)
        else:
            return None