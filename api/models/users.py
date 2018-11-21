from api.models.database import DBConnection

DBConn = DBConnection()

def setUser(username, email, phone, address, password):
    result = DBConn.add_user(username, email, phone, address, password)
    if result == "Already exists":
        return {"message": "username already exists"}
    return {"message": "Account has been created"}


def loginUser(username, password):
    user = DBConn.login_user(username, password)
    if user == None:
        return {"message": "User doesnot exist"}
    return {"message": f"Welcome {username}"}

def deleteTables():
    DBConn.delete_tables()

def SpecificUserparcels(userId):
    result = DBConn.view_user_parcels(userId)
    if result == None:
        return {"message": "User doesnot exist"}
    return result