from flask import Flask
from app import views
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')