import Handler
from google.appengine.ext import ndb


class QuestionHandler(Handler):
    def get(self, question_id):
        key = ndb.Key('Question', int(question_id))
        question = key.get()

        if not question:
            self.error(404)
            return

        self.render("question.html")


class NewQuestion(Handler):
    def get(self):
        self.render("new_question.html")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if not subject or not content:
            error = "Your question lacks a subject and/or content"
            self.render("new_question.html", error=error)

