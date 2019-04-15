#! usr/bin/ env python
# encoding: utf-8

from start import app
from flask import render_template, request
from urllib.request import *
import uuid


@app.route('/')
def start():
    return render_template('index.html', query_id=uuid.uuid4())


@app.route('/search', methods=["POST", "GET"])
def get_queries():
    query = request.form.get('query')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python'.format(server, query))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4())


@app.route('/search/filter/<option>', methods=["POST", "GET"])
def get_queries_filter(option):
    query = request.form.get('query')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&fq={}'.format(server, query, option))
    response = eval(connection.read())
    return render_template('index.html', text=response, query=query, query_id=uuid.uuid4())