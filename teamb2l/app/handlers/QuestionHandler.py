from Handler import Handler
from google.appengine.ext import ndb


class QuestionHandler(Handler):
    def get(self):
        Handler.render("question.html")
