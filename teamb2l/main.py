##!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
import os
import urllib
import jinja2
import logging
from Classes.TeacherAcct import TeacherAcct

title = "Database Maintenance"

#Master lists of all the student accounts, teacher accounts, and classes in the program.
#The classes themselves update them
template_vars = {'title':title, 'teacherMaster1':[], 'studentMaster1':[], 'classMaster1':[], 'length':1}
JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/index.html')
        self.response.write(template.render(template_vars))
#These values will be appended to objects in lists instead of simple strings
        teacher = self.request.get("teachers")
        student = self.request.get("students")
        
        classID = self.request.get("classID")
        if teacher != '':
            template_vars['teacherMaster1'].append(teacher)
        if student != '':
            template_vars['studentMaster1'].append(student)
        if classID != '':
            template_vars['classMaster1'].append(classID)

class Lister(webapp2.RequestHandler):
    def post(self):
#These values will be appended to objects in lists instead of simple strings            
        teacher = self.request.get("teachers")
        student = self.request.get("students")        
        classID = self.request.get("classID")
        
        if teacher != '':
            template_vars['teacherMaster1'].append(teacher)
        if student != '':
            template_vars['studentMaster1'].append(student)
        if classID != '':
            template_vars['classMaster1'].append(classID)
#Remove feature must still be implemented and added too
       
        template_vars['length'] = template_vars['length'] + 1
        template = JINJA_ENVIRONMENT.get_template('/list.html')
        self.response.write(template.render(template_vars))

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        admin = TeacherAcct("admin", "admin", "admin@test.test")
        admin.admin = True
        if len(TeacherAcct.teachers) == 0:
            for i in range(0, 10):
                admin.addTeacher(TeacherAcct("Teacher", str(i), "Teacher" + str(i) + "@test.test"))
        teachers = TeacherAcct.teachers
        teacherList = JINJA_ENVIRONMENT.get_template('/teachers/index.html')
        self.response.write(teacherList.render({
            'teachers': teachers,
            'count' : len(teachers)
        }))
                         
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/list.html", Lister),
    ('/teachers', AdminHandler)
], debug=True)
