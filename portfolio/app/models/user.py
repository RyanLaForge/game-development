__author__ = 'Ryan'

from google.appengine.ext import ndb


class User(ndb.Model):
    username = ndb.StringProperty(required=True, indexed=True)
    password = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    last_action = ndb.DateTimeProperty(auto_now=True, indexed=True)

