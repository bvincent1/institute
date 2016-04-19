#!/usr/bin/env python


from datetime import datetime
from app import db
from flask.ext.sqlalchemy import SQLAlchemy


class Professor(db.Model):
    __tablename__ = "professors"
    id = db.Column(db.Integer, primary_key=True)
    last = db.Column(db.String(80), default="")
    first = db.Column(db.String(80), default="")
    clarity = db.Column(db.Float, default=0.0)
    ease = db.Column(db.Float, default=0.0)
    helpfull = db.Column(db.Float, default=0.0)
    rating = db.Column(db.Float, default=0.0)
    updated = db.Column(db.String, default=datetime.utcnow().isoformat())
    total = db.Column(db.Integer, default=0)

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
        if "total" in kwargs:
            self.total = kwargs["total"]

    def toDict(self):
        """ ## retuns dictionary representation of prof """
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

class Meta(db.Model):
    """ ## stores database meta data"""
    __tablename__ = "meta"
    id = db.Column(db.Integer, primary_key=True, default=0)
    age = db.Column(db.String, default=datetime.utcnow().isoformat())
