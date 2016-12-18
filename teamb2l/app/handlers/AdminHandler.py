import webapp2
import jinja2
import os
from ..classes.User import User
from ..classes.Course import Course
import logging
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        #admin = TeacherAcct("admin", "admin", "admin@test.test")
        #admin.admin = True
        #if len(TeacherAcct.teachers) == 0:
        #    for i in range(0, 10):
        #        admin.addTeacher(TeacherAcct("Teacher", str(i), "Teacher" + str(i) + "@test.test"))
        #teachers = TeacherAcct.teachers
        #teacherList = JINJA_ENVIRONMENT.get_template('/teachers/index.html')
        #self.response.write(teacherList.render({
        #    'teachers': teachers,
        #    'count' : len(teachers)
        #}))
        logging.info(self.request.cookies.get('user'))
        user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
        user = user_key.get()
        if user.permission != 2:
            postMe = """
<html>
<head></head>
    <body style="background-color:rgb(45, 45, 45);">
    <center><font color="Gold" style="font-family:Montserrat;">
     Permission Insufficient </font></center></body>
    <meta http-equiv="refresh" content="2;url=/">
</html>
            """
            self.response.write(postMe)
        else:   
            teachers = User.query(ndb.OR(User.permission == 2, User.permission == 1)).fetch()
            students = User.query(User.permission == 0).fetch()        
            courses = Course.query().fetch()
            data = {"courses":courses, "students":students, "user":user, "teachers":teachers}
            
            template = JINJA_ENVIRONMENT.get_template('/admin/teachers.html')
            self.response.write(template.render(data))              