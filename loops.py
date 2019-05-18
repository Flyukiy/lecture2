from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    names = ['Kamol', 'Odil', 'Akram']
    return render_template("loops.html", names=names)


@app.route("/lists")
def lists():
    names = ['TV', 'PC', 'Phone']
    return render_template("loops.html", names=names)


if __name__ == '__main__':
    app.run()
