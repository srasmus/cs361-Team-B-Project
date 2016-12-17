import webapp2
import jinja2
import os
from teamb2l.app.classes import User

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)


class MessageHandler(webapp2.RequestHandler):

    def get(self):
        user = User.User.email
        messages = self.request.query()

        template = JINJA_ENVIRONMENT.get_template('/messager.html')
        self.response.write(template.render())

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('/messager.html')
        self.response.write(template.render())
