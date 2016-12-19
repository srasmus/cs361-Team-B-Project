import logging

from google.appengine.ext import ndb

from Handler import Handler
from ..classes.Question import Question


class InboxHandler(Handler):
    def render_page(self):
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
            self.render("/question/question_base.html", user=user, courses=courses)

    def get(self):
        self.render_page()


class NewQuestionHandler(Handler):
    def render_page(self, subject="", content="", courses="", error=""):
        user_key = self.request.cookies.get('user')
        if user_key is None:
            self.redirect('/login')
        else:
            user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
            user = user_key.get()
            if user.permission != 0:
                self.redirect('/')
            else:
                courses = user.getCoursesStudent()

        self.render("/question/new_question.html", user=user, subject=subject, content=content, error=error, courses=courses)

    def get(self):
        self.render_page()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        courses = self.request.get("courses")
        course = self.request.get("course")

        if not subject or not content:
            error = "Your question lacks a subject and/or content"
            self.render_page(subject, content, courses, error)
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
                    question = Question(student=user, course=course, subject=subject, content=content)
                    question.put()

                    self.redirect('/question/' + question.get())

