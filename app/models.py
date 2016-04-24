#!/usr/bin/env python


from datetime import datetime
from app import db
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ScalarListType


class Professor(db.Model):
    __tablename__ = "professors"
    id = db.Column(db.Integer, primary_key=True)
    last = db.Column(db.String(80), default="")
    first = db.Column(db.String(80), default="")
    clarity = db.Column(db.Float, default=0.0)
    ease = db.Column(db.Float, default=0.0)
    helpfull = db.Column(db.Float, default=0.0)
    rating = db.Column(db.Float, default=0.0)
    total = db.Column(db.Integer, default=0)
    tags = db.Column(ScalarListType(), default = [])
    grade = db.Column(db.String(2), default="")
    updated = db.Column(db.String(30), default=datetime.utcnow().isoformat())

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
            "clarity": self.clarity,
            "grade": self.grade,
            "tags": self.tags
        }
        return d
