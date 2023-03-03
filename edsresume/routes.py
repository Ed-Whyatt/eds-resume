from flask import render_template
from edsresume import app, db
from edsresume.models import Users


@app.route("/")
def home():
    return render_template("base.html")
