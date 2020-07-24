from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db

app = Flask(__name__)

# Congifure and Initialize Database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///movies_example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config['SECRET_KEY'] = "chickens"

connect_db(app)

@app.route("/")
def home_page():
  """Shows home page"""
  return render_template("home.html")