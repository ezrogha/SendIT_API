from api.models.data import db

def home_model():
  db["_response"] = {
    "code": 200,
    "message": "Welcome to SendIT api"
  }
  return db["_response"]