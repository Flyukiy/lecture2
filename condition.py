import datetime
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.year == 1 and now.day == 1
    return render_template("condition.html", new_year=new_year)


if __name__ == '__main__':
    app.run()
