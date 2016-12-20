import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from ..classes.User import*
from ..classes.Course import Course
from ..classes.faq import FAQ

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class StudentFAQHandler(webapp2.RequestHandler):
    def get(self):
        course = ndb.Key(urlsafe=self.request.get('classes'))

        faqs = FAQ.query(FAQ.course == course).fetch()

        template = JINJA_ENVIRONMENT.get_template('/student/faq.html')
        self.response.write(template.render({
        	'course': course.get(),
            'faqs':faqs
        }))