from Handler import Handler
from ..classes.Question import Question
from ..classes.User import User


class QuestionsHandler(Handler):
    def render_page(self,):
        self.render("/question/questions.html")

    def get(self):
        user = self.request.cookies.get('user')
        if user is None:
            self.redirect("/login")
        else:
            user = User.currentUser(self)
            if user.permission == 1:
                courses = user.getCoursesStudent()
            else:
                courses = user.getCoursesTeacher()

        for course in courses:
            questions = Question.getQuestionsCourse(courses)

        self.render_page()
