import webapp2
import jinja2
import os
from ..tests import Test_StudentAcct
from ..tests.Test_Course import Test_Course
from ..tests.Test_TeacherAcct import Test_TeacherAcct
import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/TestPage.html')
        self.response.write(template.render({
            't1': Test_Course().test_enroll(),
            't2': Test_Course().test_unenroll(),
            't3': Test_TeacherAcct().test_createCourse(),
            't4': Test_TeacherAcct().test_removeCourse(),
            't5': Test_TeacherAcct().test_addStudents(),
            't6': Test_TeacherAcct().test_removeStudent()
        }))