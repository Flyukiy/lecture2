from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    head = "Hello world"
    return render_template("index.html", headline=head)


if __name__ == "__main__":
    app.run()
