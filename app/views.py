#!/usr/bin/env python

from app import *
from app import api
from flask import render_template

import requests

@app.route('/')
def home():
    raw_feed = requests.get("https://api.github.com/users/bvincent1/events/public").json()
    git_feed = []

    for event in raw_feed:
        if event["type"] == "PushEvent" and event["repo"]["name"] == "bvincent1/institutional":
            for commit in event["payload"]["commits"]:
                git_feed.append({ "message": commit["message"] })


    return render_template('index.html', git=git_feed[:5])


@app.route('/robots.txt')
@auto.doc()
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

@app.route("/documentation")
def documentation():
    return auto.html(   template='documentation.html',
                        title='My Documentation',
                        author='Ben Vincent')

@app.route("/otherwise")
def otherwise():
    return render_template('otherwise.html')
