from api.models.data import db

def get_all_users():
  if(db["users"] == {}):
    db["_response"] = {
      "code": 200,
      "message": "No Users currently available"
    }
    return db["_response"]
  return db["users"]


def set_user(firstname, lastname, email, phone, address, password, user_id):
  db["users"][user_id] = {
      "userId": user_id,
      "firstname": firstname,
      "lastname": lastname,
      "email": email,
      "phone": phone,
      "address": address,
      "password": password,
      "sent": 0,
      "received": 0,
      "status": "active"
  }
  db["_response"] = {
      "code": "201",
      "message": f"Hello {firstname}, your account was created, successfully"
  }
  users = db["users"]
  message = db["_response"]
  users_db = {
      "_response": message,
      "users": users
  }
  return users_db


# def check_user(userId):
#   return db["users"].get(userId)