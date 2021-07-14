import falcon
from falcon_autocrud.resource import CollectionResource, SingleResource
from model import *
from main import Session
import datetime

class healthcheck(object):
    def on_get(self, req, resp):
        resp.body = "APP OK"

class ToDoCollectionResource(CollectionResource):
 model=ToDoBase

class ToDoResource(SingleResource):
 model=ToDoBase
 
# def mark_deleted(self, req, resp, instance, *args, **kwargs):
#         instance.deleted = datetime.utcnow()


class GetObjectInfo:
    def on_get(self, req, res, varid):
        result = Session.query(ToDoBase).get(varid)
        res.status = falcon.HTTP_200 
        res.content_type = falcon.MEDIA_TEXT
        if str(res)=="None":
            res.text = "Object does not exist"
        else:
            res.text = (str(res))        