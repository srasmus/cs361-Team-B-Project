import webapp2
import jinja2
import os

#-------------------------------
# Start of HEAD content
#-------------------------------

# from app.classes.StudentAcct import StudentAcct

# import main

# JINJA_ENVIRONMENT = jinja2.Environment(
# loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'Mocs')),
# extensions=['jinja2.ext.autoescape'],
# autoescape=True)


# class LoginHandler(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('/Login.html')
#         self.response.write(template.render(main.template_vars))
 
# # Login posts to self to save code   
#     def post(self):
#         authenticate = False
#         name = ""
#         main.template_vars['errors'] = []
#         email = self.request.get("username")
#         password = self.request.get("password")
        
#         main.template_vars['teacher'] = self.request.get("teacher")        
        
#         for student in StudentAcct.query().fetch():
#             if 1 == 1:
#                 authenticate = True
#                 name = student.name
# # Lets the user know they are logged in
#         if authenticate and not main.template_vars['teacher']:
#             postMe = """
# <html>
# <head></head>
#     <body> You are logged in as """ + name + """</body>
#     <meta http-equiv="refresh" content="2;url=/Student FAQs.html">
# </html>
#             """
#             self.response.write(postMe)
#         elif authenticate and main.template_vars['teacher']:
#             postMe = """
# <html>
# <head></head>
#     <body> You are logged in as TEACHER </body>
#     <meta http-equiv="refresh" content="2;url=/Teacher FAQs.html">
# </html>
#             """
#             self.response.write(postMe)
# # If login fails this happens
#         else:
#             main.template_vars['errors'].append("-Incorrect Login")
#             template = JINJA_ENVIRONMENT.get_template('/Login.html')
#             self.response.write(template.render(main.template_vars))
#--------------------------
#  End of HEAD content
#--------------------------


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
        password = self.request.get('password')
        user = User.query(User.email == email, User.password == password).get()

        if user == None:
            template = JINJA_ENVIRONMENT.get_template('/auth/login.html')
            self.response.write(template.render({'errors': ["Error:  Invalid Email or Password."]}))
        else:
            self.response.set_cookie('user', user.key.urlsafe())
            self.redirect('/')

