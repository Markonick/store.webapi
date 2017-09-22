# app/__init__.py

# third-party imports
from flask import Flask

app = Flask(__name__)
from app import views
