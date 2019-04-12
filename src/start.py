__author__ = 'Asia Paliwoda'

from os import path
from flask import Flask

app = Flask(__name__)

app.static_path = path.join(path.abspath(__file__), 'static')

from views import *
