import webapp2
import jinja2
import os

from app.classes.StudentAcct import StudentAcct

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class StudentMailHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Inbox Student.html')
        self.response.write(template.render(main.template_vars))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('/Inbox Student.html')
        self.response.write(template.render())
            
class TeacherMailHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Inbox Teacher.html')
        self.response.write(template.render(main.template_vars))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('/Inbox Teacher.html')
        self.response.write(template.render(main.template_vars)) 

class StudentCompose(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Student Compose.html')
        self.response.write(template.render(main.template_vars))

class TeacherCompose(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Teacher Compose.html')
        self.response.write(template.render(main.template_vars))

class DummyStudent(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Dummy Mail Student.html')
        self.response.write(template.render())

class DummyTeacher(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Dummy Mail Teacher.html')
        self.response.write(template.render(main.template_vars))