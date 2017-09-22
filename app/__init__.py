# app/__init__.py

# third-party imports
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views
