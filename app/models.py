#!/usr/bin/env python

from app import db
from flask.ext.sqlalchemy import SQLAlchemy


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_last = db.Column(db.String(80))
    name_First = db.Column(db.String(80))
