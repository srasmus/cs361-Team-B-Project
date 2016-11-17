import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb
from ..classes.User import User

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('/auth/login.html')
		self.response.write(template.render())
	def post(self):
		email = self.request.get('email')
		user = User.query(User.email == email).get()

		logging.info(user.key)

		self.response.set_cookie('user', user.key.urlsafe())
		self.redirect('/')
