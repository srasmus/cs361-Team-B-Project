import webapp2
import jinja2
import os

from ..tests.Test_StudentAcct import StudentTest
from HTMLTestRunner import HTMLTestRunner
import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)



class TestHandler(webapp2.RequestHandler):
    def get(self):
        test = HTMLTestRunner()
        result = test._generate_report(test.run(StudentTest('test_makeStudent')))
        self.response.write(result)
