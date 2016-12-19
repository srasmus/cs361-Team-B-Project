import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from ..classes.User import*
from ..classes.Course import Course
from google.appengine.api import app_identity
from google.appengine.api import mail
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class SendHandler(webapp2.RequestHandler):
    def post(self):
        course_key = ndb.Key(urlsafe=self.request.get('course_key'))
        course = course_key.get()

        #all the names of the student in course
        student_query = StudentCourse.query(StudentCourse.course == course_key)

        #names = names in textarea
        names = self.request.get('names') #
        list = names.split(',',1)
        #for each name seperated by ","
        for name in list:
            logging.info(name)
            c=0
            n =User(email = name)
            n.put()
            #check if name is already in the system
            if User.query(User.email == name).fetch():
                c = c + 1
            #if name is already in the system then enroll
            if c>0:
                student = User.query(User.email == name).fetch()
                student =student[0]
                course.enroll(student.key)

                self.redirect('/teacher/courses/faq?course_key=' + course_key.urlsafe())
            else:
                email = name
                # send out email
                n = User(email=email)
                n.put()
                sender = 'Teacher@{}.appspotmail.com'.format(app_identity.get_application_id())
                to_address = name
                subject = "Register for Teamb2L."
                body = """Click on the link below to register.
                                      https://chrome-lambda-146117.appspot.com/register?"""
                mail.send_mail(sender, to_address, subject, body)
                self.redirect('/teacher/courses')

                course.enroll(n.key)
                self.redirect('/teacher/courses/faq?course_key=' + course_key.urlsafe())





