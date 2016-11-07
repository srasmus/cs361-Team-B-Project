class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/input.html')
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