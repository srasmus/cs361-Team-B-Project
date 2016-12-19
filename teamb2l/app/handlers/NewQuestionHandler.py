from Handler import Handler
from ..classes.User import User
from ..classes.Question import Question


class NewQuestionHandler(Handler):
    def render_page(self, subject="", message="", cur_course="", error=""):
        user = User.currentUser(self)
        courses = User.getCoursesStudent(user)

        self.render("question/new_question.html", subject=subject, message=message, error=error, cur_course=cur_course,
                    courses=courses)

    def get(self):
        user = self.request.cookies.get('user')
        if user is None:
            self.redirect("/login")
        else:
            self.render_page()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        course = self.request.get("courses")

        if not subject or not content:
            error = "Your question lacks a subject and/or content"
            self.render_page(subject, content, course, error)
        else:
            student = User.currentUser(self)
            Question.createQuestion(student=student, course=course, subject=subject, content=content)

            self.redirect("/")
