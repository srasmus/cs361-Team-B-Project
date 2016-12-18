import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from ..classes.User import*
from ..classes.Course import Course
from ..classes.faq import FAQ

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class StudentFAQHandler(webapp2.RequestHandler):
    def get(self):
        course = self.request.get('classes')
        faqs = FAQ.query(FAQ.course == course).fetch()

        template = JINJA_ENVIRONMENT.get_template('/Student FAQs.html')
        self.response.write(template.render({
            'faqs':faqs
        }))