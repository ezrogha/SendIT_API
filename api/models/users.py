from api.models.data import db


def get_all_users():
    if(db["users"] == {}):
        db["_response"] = {
            "code": 404,
            "message": "No Users currently available"
        }
        return db["_response"]
    db["_response"] = {
        "message": "All Users",
        "code": 200
    }
    users = db["users"]
    response = db["_response"]
    users_db = {
        "_response": response,
        "users": users
    }
    return users_db


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
        "code": 201,
        "message": f"Hello {firstname}, your account was created successfully"
    }
    users = db["users"]
    message = db["_response"]
    users_db = {
        "_response": message,
        "users": users
    }
    return users_db


def check_user(userId):
    return db["users"].get(userId)


def set_user_parcels(parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status, parcel_id, userId):
    db["parcels"][parcel_id] = {
        "parcelId": parcel_id,
        "userId": userId,
        "from": parcel_from,
        "to": parcel_to,
        "weight": parcel_weight,
        "price": parcel_price,
        "status": parcel_status
    }
    userdb = {}
    userdb["user"] = db["users"][userId]
    user_parcels = {}

    for parcelId in db["parcels"]:
        if not db["parcels"][parcelId] == {}:
            if userId == db["parcels"][parcelId]["userId"]:
                user_parcels[parcelId] = db["parcels"][parcelId]
    userdb["parcels"] = user_parcels
    userparcels = userdb["parcels"]
    db["_response"] = {
        "code": 201,
        "message": f"A new parcel has been created by user {userId}"
    }
    message = db["_response"]
    user_db = {
        "_response": message,
        "parcels": userparcels}
    return user_db


def get_user_parcels(userId):
    userdb = {}
    userdb["user"] = db["users"][userId]
    user_parcels = {}

    for parcelId in db["parcels"]:
        if not db["parcels"][parcelId] == {}:
            if userId == db["parcels"][parcelId]["userId"]:
                user_parcels[parcelId] = db["parcels"][parcelId]
    userdb["parcels"] = user_parcels
    userparcels = userdb["parcels"]
    db["_response"] = {
        "code": 200,
        "message": f"list of all parcels of user {userId}"
    }
    message = db["_response"]
    user_db = {
        "_response": message,
        "parcels": userparcels}
    return user_db
