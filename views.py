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
    query = request.form.get('query').replace(' ', '+')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&defType=edismax'.format(server, query))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4())


@app.route('/search/<query>/filter/<option>', methods=["POST", "GET"])
def get_queries_filter(query, option):
    query = query.replace(' ', '+')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&fq=content_type%3A*{}*&defType=edismax'.format(server, query, option))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4())


@app.route('/search/<query>/sort/<option>', methods=["POST", "GET"])
def get_queries_sort(query, option):
    query = query
    server = 'http://localhost:8983'
    s_option = ''
    if option == 'oldest':
        s_option = 'created%20asc%2C%20creation_date%20asc%2C%20meta_creation_date%20asc'
    elif option == 'newest':
        s_option = 'created%20desc%2C%20creation_date%20desc%2C%20meta_creation_date%20desc'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&sort={}&defType=edismax'.format(server, query, s_option))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4())

