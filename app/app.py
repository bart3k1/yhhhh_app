# from resources import GetObjectInfo
from sqlalchemy import create_engine
import falcon
from falcon_autocrud.middleware import Middleware
import psycopg2
# from resources import ToDoCollectionResource, ToDoResource, healthcheck
from falcon_autocrud.resource import CollectionResource, SingleResource

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from sqlalchemy import select
from app.model import *
import json


db_engine = create_engine('postgresql+psycopg2://myuser:mypass@localhost/mydb')

session_factory = sessionmaker(bind=db_engine)
Session = scoped_session(session_factory)


class SQLAlchemySessionManager:
    """
    Create a scoped session for every request and close it when the request
    ends.
    """

    def __init__(self, Session):
        self.Session = Session

    def process_resource(self, req, resp, resource, params):
        resource.session = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            if not req_succeeded:
                resource.session.rollback()
            Session.remove()


app = falcon.API(middleware=[Middleware()])

app1 = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
])


class healthcheck(object):
    def on_get(self, req, resp):
        resp.body = "APP OK"

healthcheck = healthcheck()


class GetObjectInfo:
    def on_get(self, req, resp, varid):
        resp = Session.query(ToDoBase).get(varid)
        resp.status = falcon.HTTP_200 
        resp.content_type = falcon.MEDIA_TEXT
        if str(resp)=="None":
            resp.body = "NO Objects"
        else:
            resp.text = (str(resp))     

class GetList:
    def on_get(self, req, resp):
        result = Session.query(ToDoBase).all()
        resp.status = falcon.HTTP_200 
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = (str(result)) 


app.add_route('/index',CollectionResource(db_engine))
app.add_route('/get/{id}',SingleResource(db_engine))
app.add_route('/update/{id}',SingleResource(db_engine))
app.add_route('/delete/{id}',SingleResource(db_engine))
app.add_route('/status',healthcheck)

app.add_route('/indexs',GetList())
app.add_route('/gets/{varid:int}',GetObjectInfo())
# app.add_route('/updates/{varid}',ToDoResource(db_engine))
# app.add_route('/deletes/{varid}',ToDoResource(db_engine))
# app.add_route('/statuss',healthcheck)