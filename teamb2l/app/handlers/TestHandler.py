import webapp2
import jinja2
import os
from ..tests.Test_StudentAcct import StudentTest

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)


class TestHandler(webapp2.RequestHandler):
    def get(self):
        x = StudentTest()
        template = JINJA_ENVIRONMENT.get_template('TestPage.html')
        self.response.write(template.render({
            't1': x.test_makeStudent()
        }))