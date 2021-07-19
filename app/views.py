import falcon
from db import *
from model import *

form = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="http://127.0.0.1/update/(_id)" method="post">
        <textarea name='form_text'>  </textarea> 
        <button type="submit" name="btn">Submit</button>
    </form>
</body>
</html>

"""


class ItemList:
    def on_get(self, req, resp):
        item = Session.query(Todo_base).all()
        resp.status = falcon.HTTP_200 
        resp.content_type = falcon.MEDIA_TEXT
        resp.body = (str(item))

class ItemInfo:
    def on_get(self, req, resp,_id):
        item = Session.query(Todo_base).get(_id)
        resp.status = falcon.HTTP_200 
        resp.content_type = falcon.MEDIA_TEXT
        resp.body = (str(item))

class ItemDelete:
    def on_get(self, req, resp,_id):
        item = Session.query(Todo_base).get(_id)
        resp.content_type = falcon.MEDIA_TEXT
        item.active = False
        resp.status = falcon.HTTP_202 
        Session.commit()

#https://www.w3cschool.cn/doc_falcon_1_2/falcon_1_2-api-request_and_response.html
class ItemUpdate:
    # def on_get (self, req, resp, _id):
    #     resp.content_type = falcon.MEDIA_HTML
    #     resp.body = (form)
    
    def on_post(self, req, resp, _id):
        item = Session.query(Todo_base).get(_id)
        form_status = req.get_param("form_status")
        form_text = req.get_param("form_text")
        form_date_added = req.get_param("form_date_added")
        item.status = str(form_status)
        item.text = str(form_text)
        item.date_added = str(form_date_added)
        Session.commit()
        
