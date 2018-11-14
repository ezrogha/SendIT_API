from flask import jsonify, request, redirect, url_for
from run import app
from api.models.users import *

from datetime import datetime
from time import mktime


@app.route("/api/v1/users", methods=["GET", "POST"])
def allUsers():
  if request.method == "POST":
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    password = request.form.get("password")
    dt = datetime.now()
    user_id = str(int(mktime(dt.timetuple()))) 
    return jsonify(set_user(firstname, lastname, email, phone, address, password, user_id))

  elif request.method == "GET":
    return jsonify(get_all_users())