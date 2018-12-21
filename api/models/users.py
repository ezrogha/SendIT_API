from api.models.database import DBConnection


class User(object):

    def __init__(self):
        self.DBConn = DBConnection()


    def setUser(self, username, email, phone, address, password, role):
        result = self.DBConn.add_user(username, email, phone, address, password, role)
        if result == "Already exists":
            return {"message": "username or email already used"}
        return {"message": "Account has been created"}


    def loginUser(self, username, password):
        user = self.DBConn.login_user(username, password)
        if user == None:
            return {"message": "User doesnot exist"}
        return user


    def deleteTables(self):
        self.DBConn.delete_tables()


    def specificUserparcels(self, userId):
        result = self.DBConn.view_user_parcels(userId)
        if result == None:
            return {"message": "User doesnot exist"}
        return result


    def fetchAllUsers(self):
        result = self.DBConn.all_users()
        return result
