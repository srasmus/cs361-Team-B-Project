import webapp2
import os
import jinja2
import logging
from ..classes.User import User
from ..handlers.Handler import Handler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class RegisterHandler(Handler):
    def render_page(self, name="", email="", password="", confirm_pass="", error=""):
        self.render('/auth/register.html', name=name, email=email, password=password, confirm_pass=confirm_pass,
                    error=error)

    def get(self):
        self.render_page()

    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        password = self.request.get('password')
        confirm_pass = self.request.get('confirm')

        if name == "" or email == "" or password == "" or confirm_pass == "":
            self.render_page(name=name, email=email, password=password, confirm_pass=confirm_pass,
                             error="Fill in missing fields")

        else:
            user = User.query(User.email == email).get()

            logging.info(user)

            if user != None:
                self.render_page(name=name, email=email, password=password, confirm_pass=confirm_pass,
                                 error="Email already taken")
            elif password != confirm_pass:
                self.render_page(name=name, email=email, password=password, confirm_pass=confirm_pass,
                                 error="Passwords do not match")
            else:
                user = User()

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

class LoginHandler(Handler):
    def get(self):
        user = User.currentUser(self)
        if user is not None:
            self.redirect("/logout")
        self.render('/auth/login.html')

    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')
        user = User.query(User.email == email, User.password == password).get()

        #hardcoded admin for testing and demos
        if email == "hmccringleberry@uwm.edu" and password == "1234" and not user:
            user = User()
            user.name = "Hingle McCringleberry"
            user.email = email
            user.password = password
            user.permission = 2
            user.put()

        #hardcoded student for testing and demos
        elif email == "jdoe@mail.mail" and password == "1234" and not user:
            user = User()
            user.name = "John Doe"
            user.email = email
            user.password = password
            user.permission = 0
            user.put()

        if user == None:
            user = User.query(User.email == email, User.password == password).get()

        if user == None:
            self.render('/auth/login.html', error="Invalid Email or Password.")
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
