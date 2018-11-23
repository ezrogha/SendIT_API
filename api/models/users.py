from api.models.database import DBConnection

DBConn = DBConnection()

def setUser(username, email, phone, address, password, role):
    result = DBConn.add_user(username, email, phone, address, password, role)
    if result == "Already exists":
        return {"message": "username or email already used"}
    return {"message": "Account has been created"}


def loginUser(username, password):
    user = DBConn.login_user(username, password)
    if user == None:
        return {"message": "User doesnot exist"}
    return user

def deleteTables():
    DBConn.delete_tables()

def specificUserparcels(userId):
    result = DBConn.view_user_parcels(userId)
    if result == None:
        return {"message": "User doesnot exist"}
    return result

def fetchAllUsers():
    result = DBConn.all_users()
    return result
