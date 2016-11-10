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
from app.handlers.AdminHandler import AdminHandler
from app.handlers.Lister import Lister

from mocs.login import Login

title = "Team B2L"

#Master lists of all the student accounts, teacher accounts, and classes in the program.
#The classes themselves update them
template_vars = {'title':title, 'teacherMaster1':[], 'studentMaster1':[], 'courseMaster1':[], 'length':1}
JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)
           
app = webapp2.WSGIApplication([
    ('/', Login),
    #('/', MainHandler),
    #("/list.html", Lister),
    #('/teachers', AdminHandler)
], debug=True)
