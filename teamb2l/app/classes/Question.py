from google.appengine.ext import ndb
import StudentCourse


class Question(ndb.model):
    student = ndb.StringProperty(required=True)
    course = ndb.StringProperty(required=True)
    subject = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)

    def question(self, student_course, question, content):
        if student_course is not type == StudentCourse:
            raise TypeError(student_course + "is not StudentCourse object")
        self.student = student_course.getStudent()
        self.course = student_course.getCourse()
        self.subject = question
        self.content = content
        question = Question(self.student, self.course, self.subject, self.content)
        question.put()
