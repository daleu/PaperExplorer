from flask import Flask
import DatabaseService

app = Flask(__name__)


@app.route("/")
def hello():
    print(DatabaseService.db.connection.__dict__)
    return "Hello World!"


if __name__ == "__main__":
    app.run()
