#! usr/bin/ env python
# encoding: utf-8

from start import app
from flask import render_template, request
from urllib.request import *
from urllib.parse import quote
import uuid


@app.route('/')
def start():
    return render_template('index.html', query_id=uuid.uuid4())


@app.route('/search', methods=["POST", "GET"])
def get_queries():
    query = request.form.get('query').replace(' ', '+')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&defType=edismax'.format(server, quote(query)))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4())


@app.route('/search/<query>/<page>', methods=["POST", "GET"])
def get_queries_page(query, page):
    start = (int(page) -1) * 30
    query = query.replace(' ', '+')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&start={}&defType=edismax'.format(server, quote(query), start))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4())


@app.route('/search/<query>/filter/<option>/<page>', methods=["POST", "GET"])
def get_queries_filterPage(query, option, page):
    start = (int(page) - 1) * 30
    query = query.replace(' ', '+')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&start={}&fq=content_type%3A*{}*&defType=edismax'.format(server, quote(query), start, option))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4(), filter=True, f_option=option)


@app.route('/search/<query>/filter/<option>', methods=["POST", "GET"])
def get_queries_filter(query, option):
    query = query.replace(' ', '+')
    server = 'http://localhost:8983'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&fq=content_type%3A*{}*&defType=edismax'.format(server, quote(query), option))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4(), filter=True, f_option=option)


@app.route('/search/<query>/sort/<option>/<page>', methods=["POST", "GET"])
def get_queries_sortPage(query, option, page):
    start = (int(page) - 1) * 30
    query = query
    server = 'http://localhost:8983'
    s_option = ''
    if option == 'oldest':
        s_option = 'created%20asc%2C%20creation_date%20asc%2C%20meta_creation_date%20asc'
    elif option == 'newest':
        s_option = 'created%20desc%2C%20creation_date%20desc%2C%20meta_creation_date%20desc'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&start={}&sort={}&defType=edismax'.format(server, quote(query), start, s_option))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4(), sort=True, s_option=s_option)


@app.route('/search/<query>/sort/<option>', methods=["POST", "GET"])
def get_queries_sort(query, option):
    query = query
    server = 'http://localhost:8983'
    s_option = ''
    if option == 'oldest':
        s_option = 'created%20asc%2C%20creation_date%20asc%2C%20meta_creation_date%20asc'
    elif option == 'newest':
        s_option = 'created%20desc%2C%20creation_date%20desc%2C%20meta_creation_date%20desc'
    connection = urlopen('{}/solr/datasets/select?q={}&wt=python&rows=30&sort={}&defType=edismax'.format(server, quote(query), s_option))
    response = eval(connection.read())
    return render_template('index.html', text=response['response'], query=query, query_id=uuid.uuid4(), sort=True, s_option=s_option)

