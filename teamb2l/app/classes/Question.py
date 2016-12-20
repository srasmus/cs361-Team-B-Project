from google.appengine.ext import ndb


class Question(ndb.Model):
    student = ndb.StringProperty(required=True)
    course = ndb.StringProperty(required=True)
    subject = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    answer = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)
