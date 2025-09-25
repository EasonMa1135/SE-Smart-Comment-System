import json
from datetime import datetime
from apps import create_app
from apps.orm import *
from gevent import pywsgi
import logging

app = create_app()

@app.route('/')
def home():
    return 'Hello, Flask is running!'

from apps import db

topic = 'testapp'

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()
