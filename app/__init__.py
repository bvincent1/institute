#!/usr/bin/env python

import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
app.config["PORT"] = os.environ.get("PORT", "5000")

db = SQLAlchemy(app)

from app import views, models
