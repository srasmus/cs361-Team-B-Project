import webapp2
import jinja2
import os

from app.classes.TeacherAcct import TeacherAcct

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class TeacherFAQHandler(webapp2.RequestHandler):
    def get(self):
    	faqs = [
			{
				'question' : "Is the sky blue?",
				'answer' : "Yes"
			}
		]

        template = JINJA_ENVIRONMENT.get_template('/teacher/faq.html')
        self.response.write(template.render({
        	'faqs' : faqs,
        	'course_key' : "test key",
        	'course': {
        		'courseID': "CS 361"
        	}
       	}))
    def post(self):
        pass


class TeacherCourseHandler(webapp2.RequestHandler):
	def get(self):
		pass
	def post(self):
		pass