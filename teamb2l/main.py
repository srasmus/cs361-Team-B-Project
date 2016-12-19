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


# Handler Imports
from app.handlers.MainHandler import MainHandler
from app.handlers.TestHandler import TestHandler
from app.handlers.AdminHandler import AdminHandler
from app.handlers.StudentHandler import StudentHandler
from app.handlers.TeacherHandler import *
from app.handlers.AuthHandler import *
from app.handlers.CourseHandler import*
from app.handlers.StudentFAQHandler import StudentFAQHandler
from app.handlers.NewQuestionHandler import NewQuestionHandler
from app.handlers.CurrentQuestionHandler import CurrentQuestionHandler
from app.handlers.QuestionsHandler import QuestionsHandler


app = webapp2.WSGIApplication([
    ('/Student FAQs.html', StudentHandler),
    ('/test', TestHandler),
    ('/', MainHandler),
    ('/teachers', AdminHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/student/faq', StudentFAQHandler),
    ('/register', RegisterHandler),
    ('/teacher/courses', TeacherCourseHandler),
    ('/teacher/courses/faq', TeacherFAQHandler),
    ('/teacher/courses/delete', CourseDeletionHandler),
    ('/teacher/courses/faq/delete', FAQDeletionHandler),
    ('/teacher/courses/students', SendHandler),
    ('/questions/?', QuestionsHandler),
    ('/questions/([0-9]+)', CurrentQuestionHandler),
    ('/questions/new', NewQuestionHandler),
], debug=True)
