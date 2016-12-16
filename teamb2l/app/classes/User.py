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
		pivot_query = StudentCourse.query(StudentCourse.student==self.key)

		courses = []
		for pivot in pivot_query:
			course = pivot.course.get()
			courses.append(course)

		return courses

	def getCoursesTeacher(self):
		course_query = Course.query(Course.teacher==self.key)

		courses = []

		for course in course_query:
			courses.append(course)

		return courses