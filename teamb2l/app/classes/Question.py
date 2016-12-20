from google.appengine.ext import ndb


class Question(ndb.Model):
    student = ndb.KeyProperty(required=True)
    course = ndb.KeyProperty(required=True)
    subject = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    answer = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)
