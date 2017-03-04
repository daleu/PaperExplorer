from flask import Flask, jsonify
from flask import abort
from flask import request

import PaperService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/search")
def search():
    title = request.args.get('title')
    if title:
        papers = PaperService.list(title)
        return jsonify(papers)
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
