from Handler import Handler
from ..classes.StudentCourse import StudentCourse
from ..classes.Question import Question
from google.appengine.ext import ndb


class NewQuestionHandler(Handler):
    def render_page(self, subject="", content="", cur_course="", error=""):
        user = self.request.cookies.get('user')
        user = ndb.Key(urlsafe=user)
        user_courses = StudentCourse.query(StudentCourse.student == user)
        courses = []
        for user_course in user_courses:
            courses.append(user_course.getCourse().name)

        self.render("user/new_question.html", subject=subject, content=content, error=error, cur_course=cur_course, courses=courses)

    def get(self):
        self.render_page()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        course = self.request.get("courses")

        if not subject or not content:
            error = "Your question lacks a subject and/or content"
            self.render_page(subject, content, course, error)
        else:
            student = self.request.cookies.get('user')
            student = ndb.Key(urlsafe=student)
            Question.createQuestion(student=student, course=course, subject=subject, content=content)

            self.redirect("/")
