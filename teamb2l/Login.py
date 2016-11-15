import webapp2
import jinja2
import os

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)


class Login(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Mocs/Login.html')
        self.response.write(template.render(main.template_vars))
 
# Login posts to self to save code   
    def post(self):
        main.template_vars['errors'] = []
        email = self.request.get("username")
        password = self.request.get("password")
        
        for student in main.template_vars["studentMaster1"]:            
            if student.email == email and student.password == password:
# Lets the user know they are logged in               
                postMe = """
<html>
<head></head>
    <body> You are logged in as """ + student.email + """</body>
    <meta http-equiv="refresh" content="2;url=/Student FAQs.html">
</html>
            """
                self.response.write(postMe)
# If login fails this happens
            else:
                main.template_vars['errors'].append("-Incorrect Login")
                template = JINJA_ENVIRONMENT.get_template('Mocs/Login.html')
                self.response.write(template.render(main.template_vars))                                  
