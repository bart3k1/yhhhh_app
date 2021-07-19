import falcon
from db import *
from model import *
from views import *

app = falcon.App()
app.req_options.auto_parse_form_urlencoded=True

app.add_route('/index', ItemList())
app.add_route('/get/{_id}', ItemInfo())
app.add_route('/update/{_id}', ItemUpdate())
app.add_route('/delete/{_id}', ItemDelete())
