#!/usr/bin/env python

from app import app
from app import api
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

@app.route("/otherwise")
def otherwise():
    return render_template('otherwise.html')
