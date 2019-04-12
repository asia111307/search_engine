#! usr/bin/ env python
# encoding: utf-8

from start import app
from flask import render_template, request


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/search', methods=["POST", "GET"])
def get_queries():
    query = request.form.get('query')
    return render_template('index.html', text=query)