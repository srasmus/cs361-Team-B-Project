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
        logging.info(self.request.cookies.get('user'))
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
        courses.sort()
        self.render("/question/new_question.html", user=user, subject=subject, content=content, error=error, courses=courses)

    def get(self):
        self.render_page()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        courses = self.request.get("courses")
        course = self.request.get("course")

        if not subject or not content or not course:
            error = "Required field is blank"
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
                    course = ndb.Key(urlsafe=course)
                    question = Question(student=user_key, course=course, subject=subject, content=content)
                    question.put()

                    self.redirect('/question/inbox')

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
