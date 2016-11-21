import webapp2
import os
import jinja2
import logging
from ..classes.User import User

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class RegisterHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('/auth/register.html')
		self.response.write(template.render())
	def post(self):
		email = self.request.get('email')
		password = self.request.get('password')
		confirm_pass = self.request.get('confirm')

		user = User.query(User.email == email).get()

		logging.info(user)

		# if(user == None):
		# 	user = User(email=email, password=password, permission=0)
		# 	user_key = user.put()
		# 	self.response.set_cookie('user', user_key.urlsafe())
		# 	self.redirect('/')
		# else:
		# 	self.redirect('/')
		if user != None:
			template = JINJA_ENVIRONMENT.get_template('/auth/register.html')
			self.response.write(template.render({'errors': ["Error:  Email already taken"]}))
		elif password != confirm_pass:
			template = JINJA_ENVIRONMENT.get_template('/auth/register.html')
			self.response.write(template.render({'errors': ["Error: Passwords do not match"]}))
		else:
			user = User()
			user.email = email
			user.password = password
			user.permission = 0
			user_key = user.put()
			self.response.set_cookie('user', user_key.urlsafe())
			self.redirect('/')