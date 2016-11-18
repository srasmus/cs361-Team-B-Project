import webapp2
import jinja2
import os

from app.classes.StudentAcct import StudentAcct

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class StudentHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Student FAQs.html')
        self.response.write(template.render(main.template_vars))