import webapp2

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
              