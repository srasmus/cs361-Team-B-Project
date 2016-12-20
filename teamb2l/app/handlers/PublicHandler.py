import webapp2
import jinja2
import os
from ..classes.Course import Course

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class PublicCourseHandler(webapp2.RequestHandler):
	def get(self):
		courses = Course.query().fetch()

		template = JINJA_ENVIRONMENT.get_template('/public/courses.html')

		self.response.write(template.render({
			'courses': courses
		}))

class PublicFAQHandler(webapp2.RequestHandler):
	def get(self):
		course = ndb.Key(urlsafe=self.request.get('course'))

		course = course.get()

		faqs = course.getFAQs()

		template = JINJA_ENVIRONMENT.get_template('/public/faqs.html')

		self.response.write(template.render({
			'course': course,
			'faqs': faqs
		}))