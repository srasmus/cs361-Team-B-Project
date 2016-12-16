from google.appengine.ext import ndb

class FAQ(ndb.Model):
	answer = ndb.StringProperty()
	question = ndb.StringProperty()
	course = ndb.KeyProperty(kind="Course")

	def getCourse(self):
		return self.course.get() 