import webapp2
import jinja2
import os
from ..tests import Test_StudentAcct

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        x = Test_StudentAcct.StudentTest
        template = JINJA_ENVIRONMENT.get_template('/TestPage.html')
        self.response.write(template.render({
            #'t1': x.test_makeStudent()
        }))