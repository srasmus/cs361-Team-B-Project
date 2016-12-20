from google.appengine.ext import ndb
from ..classes.Question import Question
from StudentCourse import StudentCourse
from faq import FAQ
import random
import logging


class Course(ndb.Model):
    courseID = ndb.StringProperty()
    name = ndb.StringProperty()
    teacher = ndb.KeyProperty(kind="User")

    def getStudents(self):
        student_query = StudentCourse.query(StudentCourse.course==self.key)
        students = []
        for query in student_query:
            student_key = query.student
            students.append(query.student)
        return students

    def getQuestions(self):
        question_query = Question.query(StudentCourse.course == self.key)
        questions = []
        for query in question_query:
            question_key = query.question
            questions.append(query.question)
        return questions

    def enroll(self,student_key):
        pivot = StudentCourse()
        pivot.student = student_key
        pivot.course = self.key
        pivot.put()

    #removes student with key "student" from the course
    def unenroll(self,student_key):
        tmp = StudentCourse.query(StudentCourse.student==student_key and StudentCourse.course==self.key).fetch(1)
        for n in tmp:
            n.key.delete()

    def getTeacher(self):
        return self.teacher.get()

    def getFAQs(self):
        faqs = FAQ.query(FAQ.course == self.key).fetch()

        return faqs