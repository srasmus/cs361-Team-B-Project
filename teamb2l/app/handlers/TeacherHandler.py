import webapp2
import jinja2
import os

from app.classes.TeacherAcct import TeacherAcct

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class TeacherHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/Teacher FAQs.html')
        self.response.write(template.render(main.template_vars))
        
    def post(self):
            postMe = """
<html>
<head></head>
    <body> Logging Out </body>
    <meta http-equiv="refresh" content="2;url=/">
</html>
            """
            self.response.write(postMe)
