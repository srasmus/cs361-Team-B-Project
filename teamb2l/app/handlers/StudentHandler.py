import webapp2
import jinja2
import os
from ..classes.Course import Course

from google.appengine.ext import ndb
import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class StudentHandler(webapp2.RequestHandler):
    def get(self):
        user = ndb.Key(urlsafe=self.request.cookies.get('user')).get()

        courses = user.getCoursesStudent()

        data = {"user": user, "courses": courses}
        template = JINJA_ENVIRONMENT.get_template('/sPage.html')
        self.response.write(template.render(data))
        
    def post(self):
            postMe = """
<html>
<head></head>
    <body style="background-color:rgb(45, 45, 45);">
    <center><font color="Gold" style="font-family:Montserrat;">
     Going Home</font></center></body>
    <meta http-equiv="refresh" content="2;url=/">
</html>
            """
            self.response.write(postMe)
