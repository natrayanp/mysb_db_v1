from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

from natrayan import views
from natrayan import kitelogin
from natrayan import portfolio
from natrayan import fundalloc
#import views
