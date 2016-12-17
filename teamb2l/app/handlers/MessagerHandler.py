import webapp2
import jinja2
import os
from app.classes import User

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views', 'user')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)


class MessageHandler(webapp2.RequestHandler):

    def refresh(message_log):
        for message in message_log:
            sender = message[0]
            text = message[1]
            html_class = ""
            html = ""
            if User.name == sender:
                html_class = "selfMessage"
            else:
                html_class = "otherMessage"
            html.append("<div class=" + html_class + ">" + text + "</div>")
        return html

    def refresh(self):
        message_log = []
        self.refresh(message_log)

    JINJA_ENVIRONMENT.filters['refresh'] = refresh

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/messager.html')
        self.response.write(template.render())

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('/messager.html')
        self.response.write(template.render())
