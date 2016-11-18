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
from app.classes.TeacherAcct import TeacherAcct
from app.handlers.MainHandler import MainHandler
from app.handlers.TestHandler import TestHandler

from app.handlers.AdminHandler import AdminHandler
from app.handlers.Lister import Lister
from Login import Login
from app.classes import StudentAcct

from google.appengine.ext import ndb

title = "Team B2L"
# Testing Login page capabilities
test1 = StudentAcct.StudentAcct()
test1.makeStudent("John", "Doe", "jdoe@uwm.edu", "1234")

#Master lists of all the student accounts, teacher accounts, and classes in the program.
#The classes themselves update them
template_vars = {'title':title, 'errors':[]}

app = webapp2.WSGIApplication([
    ('/', Login),
    ('/Student FAQs.html', MainHandler),
    ('/test', TestHandler),
    #("/list.html", Lister),
    #('/teachers', AdminHandler)
], debug=True)
