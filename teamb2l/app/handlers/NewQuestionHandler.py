from Handler import Handler
from ..classes.StudentCourse import StudentCourse


class NewQuestionHandler(Handler):
    def render_page(self, subject="", content="", error=""):
        user = self.request.cookies.get('user')
        student_courses = StudentCourse.query(student=user)
        courses = []
        for student_course in student_courses:
            courses.append(student_course)

        self.render("user/new_question.html", subject=subject, content=content, error=error, student=user, courses=courses)

    def get(self):
        self.render_page()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        courses = self.request.get("course")

        if not subject or not content:
            error = "Your question lacks a subject and/or content"
            self.render_page(subject, content, courses, error)
        else:
            self.write("Valid")
