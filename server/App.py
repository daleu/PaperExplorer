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
    title = request.args.get('title')
    id = request.args.get('id')

    if not id and not title:
        abort(400)
    else:
        if id:
            nodes = PaperService.get_paper_by_id(id)
        elif title:
            nodes = PaperService.get_paper_by_title(title)

        r = make_response(json.dumps(nodes))
        r.status_code = 200
        r.headers = {'Content-Type': 'application/json',
                     'Access-Control-Allow-Origin': '*',
                     'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
                     'Access-Control-Allow-Headers': 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'}
        return r

if __name__ == "__main__":
    app.run()
