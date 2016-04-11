#!/usr/bin/env python

from app import db
from flask.ext.sqlalchemy import SQLAlchemy


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_last = db.Column(db.String(80), default="")
    name_First = db.Column(db.String(80), default="")
    clarity = db.Column(db.Float, default=0.0)
    ease = db.Column(db.Float, default=0.0)
    helpfull = db.Column(db.Float, default=0.0)
    rating = db.Column(db.Float, default=0.0)

    def __init__(self, id, **kwargs):
        self.id = id

        if "name_last" in kwargs:
            self.name_last = kwags["name_last"]
        if "name_first" in kwargs:
            self.name_first = kwags["name_first"]
        if "ease" in kwargs:
            self.name_last = kwags["ease"]
        if "helpfull" in kwargs:
            self.name_last = kwags["helpfull"]
        if "rating" in kwargs:
            self.name_last = kwags["rating"]
