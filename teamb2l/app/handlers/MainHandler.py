import logging
import os

import jinja2
import webapp2

from ..classes.User import *
from ..classes.User import User

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

            if(user != None):
                if user.permission == 0:
                   list =[]
                   course = []
                   del course[:]

                   student = User.query(User.email == user.email).fetch()

                   if(len(student)>0):
                       student = student[0].key
                       pivot = StudentCourse.query(StudentCourse.student==student)
                       ###############################USED TO DELETE ALL STUDENT KEYS
                       #pivot = StudentCourse.query()
                       #for p in pivot:
                           #p.key.delete()
                        ##############################
                       list = StudentCourse.query()
                       for p in pivot:
                           #list.append(p)
                           course.append(p.course.get())

                   data = {"user":user, "student":course,"list":list}
                   template = JINJA_ENVIRONMENT.get_template('/sPage.html')
                   self.response.write(template.render(data))
                elif user.permission == 1:
                    self.redirect('/teacher/courses')
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