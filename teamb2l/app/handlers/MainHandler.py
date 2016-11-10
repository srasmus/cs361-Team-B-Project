import webapp2
import jinja2
import os

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

#template_vars = main.template_vars;

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/index.html')
        self.response.write(template.render(main.template_vars))
#These values will be appended to objects in lists instead of simple strings
        teacher = self.request.get("teachers")
        student = self.request.get("students")
        
        classID = self.request.get("classID")
        if teacher != '':
            main.template_vars['teacherMaster1'].append(teacher)
        if student != '':
            main.template_vars['studentMaster1'].append(student)
        if classID != '':
            main.template_vars['classMaster1'].append(classID)