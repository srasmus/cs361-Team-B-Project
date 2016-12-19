import webapp2
import os
import jinja2
import logging
from ..classes.User import User

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
        name = self.request.get('name')

        user = User.query(User.email == email).get()

        logging.info(user)

        # if(question == None):
        # 	question = User(email=email, password=password, permission=0)
        # 	user_key = question.put()
        # 	self.response.set_cookie('question', user_key.urlsafe())
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
            if int(self.request.get('userType')) == 0:
                user = User()
                user.name = self.request.get('name')
            else:
                user = User()

            user.permission = int(self.request.get('userType'))
            user.email = email
            user.password = password
            user.name = name
            user_key = user.put()
            self.response.set_cookie('user', user_key.urlsafe())
            postMe = """<body style="background-color:rgb(45, 45, 45);">
                        <center><img src="/assets/giphy.gif" alt="Check"><br>
                        <font color="Gold" style="font-family:Montserrat;">
                        Registration Successful </font></center></body>
                        <meta http-equiv="refresh" content="2;url=/">"""
            self.response.write(postMe)


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/auth/login.html')
        self.response.write(template.render())

    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')
        user = User.query(User.email == email, User.password == password).get()

        if email == "hmccringleberry@uwm.edu" and password == "1234" and not user:
            user = User()
            user.name = "Hingle McCringleberry"
            user.email = email
            user.password = password
            user.permission = 2
            user.put()

        if user == None:
            user = User.query(User.email == email, User.password == password).get()

        if user == None:
            template = JINJA_ENVIRONMENT.get_template('/auth/login.html')
            self.response.write(template.render({'errors': ["Error:  Invalid Email or Password."]}))
        else:
            self.response.set_cookie('user', user.key.urlsafe())
            self.redirect('/')


class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        user_cookie = self.request.cookies.get('user')
        if user_cookie == "":
            self.redirect("/")
        else:
            self.response.delete_cookie('user')
            self.redirect("/login")

    def post(self):
        user_cookie = self.request.cookies.get('user')
        if user_cookie == "":
            self.redirect("/")
        else:
            self.response.delete_cookie('user')
            self.redirect("/login")
