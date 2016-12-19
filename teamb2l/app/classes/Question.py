from google.appengine.ext import ndb


class Question(ndb.Model):
    student = ndb.StringProperty(required=True)
    course = ndb.StringProperty(required=True)
    subject = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)
    content = []

    @staticmethod
    def createQuestion(self, student, course, subject, message):
        question = Question(student=student, course=course, subject=subject)
        question.content.append(Message(sender=student, content=message))
        question.put()
        return question

    @staticmethod
    def getQuestionsCourse(self, course):
        return Question.query(Question.course == course)

class Message(ndb.Model):
    sender = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)