from google.appengine.ext import ndb

from ferris import BasicModel


class Product(BasicModel):
    name = ndb.StringProperty(indexed=True, required=True)