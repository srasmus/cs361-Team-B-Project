import unittest
from teamb2l.app.handlers import QuestionHandler
from teamb2l.app.classes import Question


class TestQuestion(unittest.TestCase):

    def testQuestionHandler(self):
        return

    def testQuestion(self):
        self.assertRaises(TypeError, Question.Question.question("Junk", "Subject", "Content"))
