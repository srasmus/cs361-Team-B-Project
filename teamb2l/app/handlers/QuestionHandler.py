import logging
import os

import jinja2
import webapp2

from google.appengine.ext import ndb

from Handler import Handler
from ..classes.Question import Question

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class InboxHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(self.request.cookies.get('user'))
        user_key = self.request.cookies.get('user')
        if user_key is None:
            self.redirect('/login')
        else:
            user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
            user = user_key.get()
            if user.permission == 0:
                courses = user.getCoursesStudent()
                course = self.request.get('course')
                questions = []
                if course != "":
                    course = ndb.Key(urlsafe=course).get()
                    questions = course.getQuestions(user_key)

                template = JINJA_ENVIRONMENT.get_template('/question/question_base.html')

                self.response.write(template.render({
                    'courses': courses,
                    'course_selected': course,
                    'questions': questions,
                    'questions_count': len(questions),
                    'user': user
                }))
            else:
                courses = user.getCoursesTeacher()
            courses.sort()




class NewQuestionHandler(webapp2.RequestHandler):
    def post(self):
        content = self.request.get("content")
        course = ndb.Key(urlsafe=self.request.get("course"))
        sender = ndb.Key(urlsafe=self.request.get("sender"))

        if not content:
            self.redirect('/question/inbox?course=' + course)
        else:
            user_key = self.request.cookies.get('user')
            if user_key is None:
                self.redirect('/login')
            else:
                user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
                user = user_key.get()
                if user.permission != 0:
                    self.redirect('/')
                else:
                    question = Question(student=user_key, course=course, sender=user_key, content=content)
                    question.put()

                    self.redirect('/question/inbox?course=' + course.urlsafe())

class QuestionHandler(Handler):
    def render_page(self, question_id):
        logging.info(self.request.cookies.get('user'))
        user_key = self.request.cookies.get('user')
        if user_key is None:
            self.redirect('/login')
        else:
            user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
            user = user_key.get()
            if user.permission == 0:
                courses = user.getCoursesStudent()
            else:
                courses = user.getCoursesTeacher()
            courses.sort()
            course = courses.query()
            key = ndb.Key.from_path('Question', int(question_id))
            question = ndb.get(key)

            if not question:
                self.redirect('/')
            else:
                self.render("/question/question.html", courses=courses, question=question, user=user)

    def get(self, question_id):
        self.render_page(question_id=question_id)
