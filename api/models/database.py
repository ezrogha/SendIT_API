import psycopg2
from pprint import pprint

class DBConnection(object):
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname='sendit', user='postgres', host='localhost', password='Rghshn1993', port='5432'
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print('Database connected.')
            create_user_table = "CREATE TABLE IF NOT EXISTS users (userId SERIAL NOT NULL PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL, address TEXT NOT NULL, password TEXT NOT NULL);"
            create_parcels_table = "CREATE TABLE IF NOT EXISTS parcels (parcelId SERIAL NOT NULL PRIMARY KEY, userId INTEGER NOT NULL, p_from TEXT NOT NULL, to TEXT NOT NULL, weight INTEGER NOT NULL, price INTEGER NOT NULL, status TEXT NOT NULL);"
            
            self.cursor.execute(create_user_table)
            self.cursor.execute(create_parcels_table)

        except:
            print("Cannot connect to the database")


    def add_user(self, username, email, phone, address, password):
        query = "INSERT INTO users (username, email, phone, address, password) VALUES ('{}', '{}', '{}', '{}', '{}')".format(username, email, phone, address, password)
        self.cursor.execute(query)
    
    
    def login_user(self, username, password):
        query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
        self.cursor.execute(query)
        if self.cursor.rowcount < 1:
            return None
        user = self.cursor.fetchone()
        return user

    
    def add_parcel(self, userId, p_from, to, weight, price, status):
        query = "INSERT INTO users (userId, p_from, to, weight, price, status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(userId, p_from, to, weight, price, status)
        self.cursor.execute(query)

    
    def delete_parcel(self, parcelId):
        sel_query = "SELECT * FROM parcels WHERE parcelId = {parcelId}"
        self.cursor.execute(sel_query)
        if self.cursor.rowcount < 1:
            return None
        del_query = "DELETE FROM parcels WHERE parcelId = {parcelId}".format(parcelId)
        self.cursor.execute(sel_query)      

    
    def view_all_parcels(self):
        parcels_query = "SELECT * from parcels"
        self.cursor.execute(parcels_query)
        all_parcels = self.cursor.fetchall()
        return all_parcels


    def view_user_parcels(self, userId):
        check_user_query = "SELECT * FROM users WHERE userId = {userId}".format(userId)
        self.cursor.execute(check_user_query)
        if self.cursor.rowcount < 1:
            return None
        parcels_query = "SELECT * FROM parcels WHERE userId = {userId}".format(userId)
        self.cursor.execute(user_parcels)
        user_parcels = self.cursor.fetchall()
        return user_parcels


    def change_desitination(self, parcelId, new_destination):
        check_parcel = "SELECT * FROM parcels WHERE parcelId = {parcelId}"
        self.cursor.execute(check_parcel)
        if self.cursor.rowcount < 1:
            return None
        change_dest_query = "UPDATE parcels SET to={} WHERE parcelId = {}".format(new_destination, parcelId)
        self.cursor.execute(change_dest_query)


    def change_status(self, parcelId, new_status):
        check_parcel = "SELECT * FROM parcels WHERE parcelId = {parcelId}"
        self.cursor.execute(check_parcel)
        if self.cursor.rowcount < 1:
            return None
        change_status_query = "UPDATE parcels SET status={} WHERE parcelId = {}".format(new_status, parcelId)
        self.cursor.execute(change_status_query)


    def delete_tables(self):
        drop_tables = "DROP TABLE IF EXISTS users, parcels"
        self.cursor.execute(drop_tables)


if __name__ == "__main__":
    DBCon = DBConnection()
    

