#!/usr/bin/env python


from app import app, db
from app.models import *
from flask import Flask

import json


@app.route("/api/professor/<id>")
def getProfFromId(id):
    """ ## Returns json obj of professor with id, or empty json if none found """
    p = Professor.query.filter_by(id=id).first()
    if p:
        return json.dumps(p.toDict())
    else:
        return json.dumps({})
