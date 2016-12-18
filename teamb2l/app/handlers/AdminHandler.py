import webapp2
import jinja2
import os
from ..classes.TeacherAcct import TeacherAcct
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
    def post(self):
        logging.info(self.request.cookies.get('user'))
        user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
        user = user_key.get()
        newUser = User()
         
        studentName = self.request.get("studentName")
        teacherName = self.request.get("teacherName")
        if studentName:
            newUser.name = studentName
            newUser.permission = 0
        if teacherName:
            newUser.name = teacherName
            newUser.permission = 1
            
        userEmail = self.request.get("email")
        userPassword = self.request.get("password")
        if userEmail:
            newUser.email = userEmail
        newUser.password = userPassword  
        
        if not User.query(User.email == userEmail).get() and userEmail:
            newUser.put()           
            postMe = """
<html>
<head></head>
    <body style="background-color: rgb(38, 38, 38);">
    <center><font color="Gold" style="font-family:Montserrat;">
     Database Updated </font></center></body>
    <meta http-equiv="refresh" content="2;url=/teachers">
</html>
            """       
            self.response.write(postMe)
            
        deleteMail = self.request.get("deleteUser")
        
        if deleteMail:
            deleteS = User.query(User.email == deleteMail).get()
            if deleteS:
                deleteS.key.delete()
                
        teachers = User.query(ndb.OR(User.permission == 2, User.permission == 1)).fetch()
        students = User.query(User.permission == 0).fetch()        
        courses = Course.query().fetch()
        data = {"courses":courses, "students":students, "user":user, "teachers":teachers}
            
        template = JINJA_ENVIRONMENT.get_template('/admin/teachers.html')
        self.response.write(template.render(data))              