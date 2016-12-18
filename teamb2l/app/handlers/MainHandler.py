import webapp2
import jinja2
import os
import logging

from google.appengine.ext import ndb
from app.classes.StudentCourse import StudentCourse
from app.classes.User import User
from app.classes.Course import Course

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        logging.info(self.request.cookies.get('user'))
        user_key = self.request.cookies.get('user')
        if user_key == None:
            self.redirect('/login')
        else:
            user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
            user = user_key.get()

            logging.info(user)

            if(user != None):
                if user.permission == 0:
                    courses = StudentCourse.query(StudentCourse.student == user_key).fetch()
                    data = {"courses":courses, "user":user}
                    template = JINJA_ENVIRONMENT.get_template('/sPage.html')
                    self.response.write(template.render(data))
                else:
                    self.redirect('/teacher/courses')
                #else:
                #    students = User.query(User.permission == 0).fetch()
                #    courses = Course.query().fetch()
                #    data = {"courses":courses, "students":students, "user":user, "teachers":[]}
                #    template = JINJA_ENVIRONMENT.get_template('/admin/teachers.html')
                #    self.response.write(template.render(data))
                
            else:
                self.redirect('/login')