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
# limitations under the License
#
import webapp2
import random
import os
import urllib
import jinja2
import logging
from google.appengine.ext import ndb

# Handler Imports
from app.handlers.MainHandler import MainHandler
from app.handlers.TestHandler import TestHandler
from app.handlers.AdminHandler import AdminHandler
from app.handlers.StudentHandler import StudentHandler
from app.handlers.MailHandler import StudentMailHandler, TeacherMailHandler, StudentCompose, TeacherCompose, DummyStudent, DummyTeacher
from app.handlers.TeacherHandler import *
from app.handlers.AuthHandler import *
from app.handlers.CourseHandler import*
from app.handlers.StudentFAQHandler import StudentFAQHandler
from app.handlers.NewQuestionHandler import NewQuestionHandler

#('/teacher/courses/students'), AddHandler),
app = webapp2.WSGIApplication([
    ('/test', TestHandler),
    ('/Inbox Student.html', StudentMailHandler),
    ('/Inbox Teacher.html', TeacherMailHandler),
    ('/Student Compose.html', StudentCompose),
    ('/Teacher Compose.html', TeacherCompose),
    ('/Dummy Mail Student.html', DummyStudent),
    ('/Dummy Mail Teacher.html', DummyTeacher),
    ('/', MainHandler),
    ('/teachers', AdminHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/student/courses', StudentHandler),
    ('/student/faq', StudentFAQHandler),
    ('/register', RegisterHandler),
    ('/teacher/courses', TeacherCourseHandler),
    ('/teacher/courses/faq', TeacherFAQHandler),
    ('/teacher/courses/delete', CourseDeletionHandler),
    ('/teacher/courses/faq/delete', FAQDeletionHandler),
    ('/teacher/courses/students', SendHandler),
    ('/compose', NewQuestionHandler)
], debug=True)
