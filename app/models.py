#!/usr/bin/env python

from app import db
from flask.ext.sqlalchemy import SQLAlchemy


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last = db.Column(db.String(80), default="")
    first = db.Column(db.String(80), default="")
    clarity = db.Column(db.Float, default=0.0)
    ease = db.Column(db.Float, default=0.0)
    helpfull = db.Column(db.Float, default=0.0)
    rating = db.Column(db.Float, default=0.0)

    def __init__(self, id, **kwargs):
        self.id = id

        if "last" in kwargs:
            self.last = kwargs["last"]
        if "first" in kwargs:
            self.first = kwargs["first"]
        if "ease" in kwargs:
            self.ease = kwargs["ease"]
        if "helpfull" in kwargs:
            self.helpfull = kwargs["helpfull"]
        if "rating" in kwargs:
            self.rating = kwargs["rating"]

    def toDict(self):
        d = {
            "id": self.id,
            "last": self.last,
            "first": self.first,
            "rating": self.rating,
            "ease": self.ease,
            "helpfull": self.helpfull,
            "clarity": self.clarity
        }
        return d
