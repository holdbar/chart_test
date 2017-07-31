# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
db = SQLAlchemy(app)


from charts_test import views




