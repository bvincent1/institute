#!/usr/bin/env python

from app import *
from app import api
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


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
