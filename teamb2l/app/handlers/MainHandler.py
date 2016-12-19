import logging
import os

import jinja2
import webapp2

from google.appengine.ext import ndb
from ..classes.User import*
from ..classes.StudentCourse import*
from ..classes.User import *

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
                    self.redirect('/student/courses')
                else:
                    self.redirect('/teacher/courses')
            else:
                self.redirect('/login')