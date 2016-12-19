from google.appengine.ext import ndb

from StudentCourse import StudentCourse
from Course import Course


class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    # 0 = Student
    # 1 = Teacher
    # 2 = Admin
    permission = ndb.IntegerProperty()

    def getCoursesStudent(self):
        pivot_query = StudentCourse.query(StudentCourse.student == self.key)
        courses = []
        for pivot in pivot_query:
            course = pivot.course.get()
            courses.append(course)

        return pivot_query

    def getCoursesTeacher(self):
        course_query = Course.query(Course.teacher == self.key)

        courses = []

        for course in course_query:
            courses.append(course)

        return courses

    def makeStudent(self, firstName, lastName, email, password):
        tmplist = []
        """for i in Course.Course.query().fetch():
            if(i.students.contains(self.email)):
                tmplist.append(i.courseID)"""
        tmp = User(name=str(lastName + ", " + firstName), email=email, password=password, courses=tmplist)
        tmp.put()

    @staticmethod
    def currentUser(self):
        user_key = self.request.cookies.get('user')
        if user_key is not None:
            user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
            return user_key.get()
