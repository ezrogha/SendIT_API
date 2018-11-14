from api.models.data import db


def home_model():
  db["_response"] = {
    "code": 200,
    "message": "Welcome to SendIT api"
  }
  return db["_response"]


def get_all_parcels():
  if(db["parcels"] == {}):
    db["_response"] = {
      "code": 200,
      "message": "No Parcels currently available"
    }
    return db["_response"]
  return db["parcels"]


def set_parcel(parcel_id, parcel_userId, parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status):
  db["parcels"][parcel_id] = {
      "parcelId": parcel_id,
      "userId": parcel_userId,
      "from": parcel_from,
      "to": parcel_to,
      "weight": parcel_weight,
      "price": parcel_price,
      "status": parcel_status
  }
  db["_response"] = {
      "code": "201",
      "message": f"A parcel is created by user {parcel_userId}"
  }
  parcels = db["parcels"]
  message = db["_response"]
  parcels_db = {
      "_response": message,
      "parcels": parcels
  }
  return parcels_db


def check_parcel(parcelId):
  return db["parcels"].get(parcelId)