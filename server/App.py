#!/usr/bin/env python3
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import json

import PaperService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/search")
def search():
    name = request.args.get('name')
    id = request.args.get('id')

    if not id and not name:
        abort(400)
    else:
        if id:
            nodes = PaperService.get_paper_by_id(id)
        elif name:
            nodes = PaperService.get_node_by_name(name)

        r = make_response(json.dumps(nodes))
        r.status_code = 200
        r.headers = {'Content-Type': 'application/json',
                     'Access-Control-Allow-Origin': '*',
                     'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
                     'Access-Control-Allow-Headers': 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'}
        return r


@app.route("/list")
def list():
    title = request.args.get('title')
    if not title:
        abort(400)
    else:
        papers = PaperService.list(title)
        r = make_response(json.dumps(papers))
        r.status_code = 200
        r.headers = {'Content-Type': 'application/json',
                     'Access-Control-Allow-Origin': '*',
                     'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
                     'Access-Control-Allow-Headers': 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'}
        return r


if __name__ == "__main__":
    app.run()
