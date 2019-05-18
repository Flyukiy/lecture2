from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)
app.congif["SESSION_PERMANENT"] = False
app.congif["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)


if __name__ == '__main__':
    app.run()
