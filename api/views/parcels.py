from flask import jsonify, request, redirect, url_for
from run import app
from api.models.parcels import *


@app.route("/")
def index():
  return redirect(url_for("home"))


@app.route("/api/v1/")
def home():
  return jsonify(home_model())