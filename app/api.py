#!/usr/bin/env python

from flask import Flask
from app import *
from app.models import *
from scrape import *

import json


@app.route("/api/professor/<id>")
@auto.doc()
def getProfFromId(id):
    """ ## Returns json obj of professor with id, or empty json if none found """
    p = Professor.query.filter_by(id=id).first()
    if p:
        return json.dumps(p.toDict())
    else:
        return json.dumps({})

@app.route("/api/professor/all")
@auto.doc()
def getAllProfs():
    """ ## Returns all professors as json objs """
    p = Professor.query.all()
    if p:
        return json.dumps([i.toDict() for i in p])
    else:
        return json.dumps([{}])

@app.route("/api/update")
@auto.doc()
def updateEntries():
    """ ## update all our prof entries
    - returns either success or fail json obj
    - should not be spammed"""
    try:
        updateProfs()
        return json.dumps({"result": "success"})
    except:
        return json.dumps({"result": "fail"})
