from flask import Flask, jsonify
from flask import abort
from flask import make_response
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
        papers = PaperService.get_paper(title)
        return make_response(jsonify(papers.__dict__), 200)
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
