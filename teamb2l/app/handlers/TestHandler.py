import jinja2
import os
import webapp2

from app.tests.HTMLTestRunner import HTMLTestRunner
from..tests import TestSuite

class TestHandler(webapp2.RequestHandler):
    def get(self):
        test = HTMLTestRunner()
        result = test._generate_report(test.run(TestSuite.alltests))
        self.response.write(result)
