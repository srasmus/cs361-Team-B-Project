import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
        user = user_key.get()

        logging.info(user)

        template = JINJA_ENVIRONMENT.get_template('/input.html')
        self.response.write(template.render())