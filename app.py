from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/<string:name>")
def hello(name):
    return f"Hello {name}"

# if __name__ == "__main__":
#     app.run()
