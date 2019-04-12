#! usr/bin/ env python
# encoding: utf-8

from start import app
from flask import render_template, request
from urllib.request import *


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/search', methods=["POST", "GET"])
def get_queries():
    query = request.form.get('query')
    connection = urlopen('http://localhost:8989/solr/techproducts/select?q={}&wt=python'.format(query))
    response = eval(connection.read())
    return render_template('index.html', text=response)