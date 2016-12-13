import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb

from ..classes.faq import FAQ
from ..classes.Course import Course

import main

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class TeacherFAQHandler(webapp2.RequestHandler):
    def get(self):
        course_key = ndb.Key(urlsafe=self.request.get('course_key'))
        course = course_key.get()

        faqs = FAQ.query(FAQ.course==course_key)

        template = JINJA_ENVIRONMENT.get_template('/teacher/faq.html')
        self.response.write(template.render({
        	'faqs' : faqs, 
        	'course': course
       	}))
    def post(self):
        course_key = ndb.Key(urlsafe=self.request.get('course_key'))
        if self.request.get('faq_key') != "":
            faq_key = ndb.Key(urlsafe=self.request.get('faq_key'))
            faq = faq_key.get()
            faq.question = self.request.get('question')
            faq.answer = self.request.get('answer')
            faq.put()
        else:
            question = self.request.get('question')
            answer = self.request.get('answer')
            faq = FAQ(question=question, answer=answer, course=course_key)

            faq_count_after = FAQ.query(FAQ.course==course_key).count() + 1
            faq.put()
            current_faq_count = FAQ.query(FAQ.course==course_key).count()

            while faq_count_after != current_faq_count:
                current_faq_count = FAQ.query(FAQ.course==course_key).count()

        self.redirect('/teacher/courses/faq?course_key=' + course_key.urlsafe())

class FAQDeletionHandler(webapp2.RequestHandler):
    def post(self):
        logging.info(self.request.get('course_key'))
        course_key = ndb.Key(urlsafe=self.request.get('course_key'))
        faq_key = ndb.Key(urlsafe=self.request.get('faq_key'))

        faq_count_after = FAQ.query(FAQ.course==course_key).count() - 1
        faq_key.delete()
        current_faq_count = FAQ.query(FAQ.course==course_key).count()

        while faq_count_after != current_faq_count:
            current_faq_count = FAQ.query(FAQ.course==course_key).count()

        self.redirect('/teacher/courses/faq?course_key=' + course_key.urlsafe())

class TeacherCourseHandler(webapp2.RequestHandler):
    def get(self):
        user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
        user = user_key.get()
        if user.permission == 0:
            self.redirect('/')
        else:
            courses = Course.query(Course.teacher==user_key)
            for course in courses:
                logging.info("GETTING COURSES")
                logging.info(course)
            courses = [] if courses == None else courses
            template = JINJA_ENVIRONMENT.get_template('/teacher/courses.html')
            self.response.write(template.render({
                'courses': courses, 'user':user.name
            }))
    def post(self):
        user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
        user = user_key.get()
        if user.permission == 0:
            self.redirect('/')
        else:
            if self.request.get('course_key') != "":
                course_key = ndb.Key(urlsafe=self.request.get('course_key'))
                course = course_key.get()
                course.name = self.request.get('name')
                course.put()
            else:
                name = self.request.get('name')
                tmp = Course()
                course = tmp.makeCourse(user_key,name)
                courses_count_after = Course.query(Course.teacher==user_key).count() + 1
                course.put()
                current_courses_count = Course.query(Course.teacher==user_key).count()

                 #NDB is stupid with addition lagg, so this will have to do...
                while(courses_count_after != current_courses_count):
                    current_courses_count = Course.query(Course.teacher==user_key).count()

            self.redirect('/teacher/courses')

class CourseDeletionHandler(webapp2.RequestHandler):
    def post(self):
        course_key = ndb.Key(urlsafe=self.request.get('course_key'))
        user_key = ndb.Key(urlsafe=self.request.cookies.get('user'))
        courses_count_after = Course.query(Course.teacher==user_key).count() - 1

        course_key.delete()

        current_courses_count = Course.query(Course.teacher==user_key).count()

        # NDB is stupid with deletion lagg, so this will have to do...
        while(courses_count_after != current_courses_count):
            current_courses_count = Course.query(Course.teacher==user_key).count()

        self.redirect('/teacher/courses')