import os
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def welcome_page():
    return render_template("welcomepage.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)