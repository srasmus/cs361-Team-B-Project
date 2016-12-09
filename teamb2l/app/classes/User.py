from google.appengine.ext import ndb

class User(ndb.Model):
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	password = ndb.StringProperty()
	# 0 = Student
	# 1 = Teacher
	# 2 = Admin
	permission = ndb.IntegerProperty()