from google.appengine.ext import ndb


class Question(ndb.Model):
    sender = ndb.KeyProperty(required=True)
    student = ndb.KeyProperty(required=True)
    course = ndb.KeyProperty(required=True)
    content = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)
