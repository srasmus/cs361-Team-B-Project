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