from api.models.database import DBConnection

DBConn = DBConnection()

def setUser(username, email, phone, address, password):
    DBConn.add_user(username, email, phone, address, password)
    return {"message": "Account has been created"}


def loginUser(username, password):
    user = DBConn.login_user(username, password)
    if user == None:
        return {"message": "User doesnot exist"}
    return {"message": f"Welcome {username}"}

def deleteTables():
    DBConn.delete_tables()