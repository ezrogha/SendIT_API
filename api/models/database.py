import psycopg2
import psycopg2.extras

class DBConnection(object):
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname='sendit', user='postgres', host='localhost', password='Rghshn1993', port='5432'
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print('Database connected.')
            create_user_table = "CREATE TABLE IF NOT EXISTS users (userId SERIAL NOT NULL PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL, address TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL);"
            create_parcels_table = "CREATE TABLE IF NOT EXISTS parcels (parcelId SERIAL NOT NULL PRIMARY KEY, userId INTEGER NOT NULL, p_from TEXT NOT NULL, p_to TEXT NOT NULL, weight INTEGER NOT NULL, price INTEGER NOT NULL, status TEXT NOT NULL, location TEXT NOT NULL);"
            
            self.cursor.execute(create_user_table)
            self.cursor.execute(create_parcels_table)

        except:
            print("Cannot connect to the database")


    def add_user(self, username, email, phone, address, password, role):
        check_user = f"SELECT * FROM users WHERE username='{username}'"
        self.cursor.execute(check_user)
        if self.cursor.rowcount > 0:
            return "Already exists"
        query = f"INSERT INTO users (username, email, phone, address, password, role) VALUES ('{username}', '{email}', '{phone}', '{address}', '{password}', '{role}')"
        self.cursor.execute(query)
        return "Account created"
    

    def all_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    
    def login_user(self, username, password):
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        self.cursor.execute(query)
        if self.cursor.rowcount < 1:
            return None
        user = self.cursor.fetchone()
        return user

    
    def add_parcel(self, userId, p_from, to, weight, price, status, location):
        query = f"INSERT INTO parcels (userId, p_from, p_to, weight, price, status, location) VALUES ({userId}, '{p_from}', '{to}', '{weight}', '{price}', '{status}', '{location}')"
        self.cursor.execute(query)

    
    def delete_parcel(self, parcelId):
        sel_query = f"SELECT * FROM parcels WHERE parcelId = {parcelId}"
        self.cursor.execute(sel_query)
        if self.cursor.rowcount < 1:
            return None
        del_query = f"DELETE FROM parcels WHERE parcelId = {parcelId}"
        self.cursor.execute(sel_query)      

    
    def view_all_parcels(self):
        parcels_query = "SELECT * from parcels"
        self.cursor.execute(parcels_query)
        all_parcels = self.cursor.fetchall()
        return all_parcels


    def view_user_parcels(self, userId):
        check_user_query = f"SELECT * FROM users WHERE userId = {userId}"
        self.cursor.execute(check_user_query)
        if self.cursor.rowcount < 1:
            return None
        parcels_query = f"SELECT * FROM parcels WHERE userId = {userId}"
        self.cursor.execute(parcels_query)
        user_parcels = self.cursor.fetchall()
        return user_parcels


    def change_status(self, parcelId, new_status):
        check_parcel = f"SELECT * FROM parcels WHERE parcelId = {parcelId}"
        self.cursor.execute(check_parcel)
        if self.cursor.rowcount < 1:
            return None
        change_status_query = f"UPDATE parcels SET status={new_status} WHERE parcelId = {parcelId}"
        self.cursor.execute(change_status_query)


    def parcel_details(self, parcelId, userId):
        check_parcel = f"SELECT * FROM parcels WHERE parcelId={parcelId} AND userid={userId}"
        self.cursor.execute(check_parcel)
        if self.cursor.rowcount > 0:
            result = self.cursor.fetchone()
            return result  
        return None


    def cancel_parcel(self, parcelId, userId):
        
        check_parcel_id = f"SELECT * FROM parcels WHERE parcelId={parcelId} AND userid={userId}"
        self.cursor.execute(check_parcel_id)
        if not self.cursor.rowcount > 0:
            return "Wrong parcelId"

        check_parcel_status = f"SELECT * FROM parcels WHERE parcelId={parcelId} and status='Delivered'"
        self.cursor.execute(check_parcel_status)
        if self.cursor.rowcount > 0:
            return "Already Delivered"

        cancel_query = f"UPDATE parcels SET status='Not Delivered' WHERE parcelId={parcelId}"
        self.cursor.execute(cancel_query)


    def send_parcel(self, parcelId, userId):
        check_parcel_id = f"SELECT * FROM parcels WHERE parcelId={parcelId} AND userid={userId}"
        self.cursor.execute(check_parcel_id)
        if not self.cursor.rowcount > 0:
            return "Wrong parcelId"

        check_parcel_status = f"SELECT * FROM parcels WHERE parcelId={parcelId} and status='Delivered'"
        self.cursor.execute(check_parcel_status)
        if self.cursor.rowcount > 0:
            return "Already Delivered"

        send_query = f"UPDATE parcels SET status='In Transit' WHERE parcelId={parcelId}"
        self.cursor.execute(send_query)


    def change_destination(self, parcelId, userId, destination):
        check_parcel_id = f"SELECT * FROM parcels WHERE parcelId={parcelId} AND userid={userId}"
        self.cursor.execute(check_parcel_id)
        if not self.cursor.rowcount > 0:
            return "Wrong parcelId"

        check_dest_status = f"SELECT * FROM parcels WHERE parcelId={parcelId} and status='Delivered'"
        self.cursor.execute(check_dest_status)
        if self.cursor.rowcount > 0:
            return "Already Delivered"
        
        change_dest_query = f"UPDATE parcels SET p_to='{destination}' WHERE parcelId={parcelId}"
        self.cursor.execute(change_dest_query)


    def change_location(self, parcelId, location):
        check_parcel_id = f"SELECT * FROM parcels WHERE parcelId={parcelId}"
        self.cursor.execute(check_parcel_id)
        if not self.cursor.rowcount > 0:
            return "Wrong parcelId"

        check_loc_status = f"SELECT * FROM parcels WHERE parcelId={parcelId} and status='Delivered'"
        self.cursor.execute(check_loc_status)
        if self.cursor.rowcount > 0:
            return "Already Delivered"
        
        change_loc_query = f"UPDATE parcels SET location='{location}' WHERE parcelId={parcelId}"
        self.cursor.execute(change_loc_query)


    def change_status(self, parcelId, status):
        check_parcel_id = f"SELECT * FROM parcels WHERE parcelId={parcelId}"
        self.cursor.execute(check_parcel_id)
        if not self.cursor.rowcount > 0:
            return "Wrong parcelId"

        change_loc_query = f"UPDATE parcels SET status='{status}' WHERE parcelId={parcelId}"
        self.cursor.execute(change_loc_query)


    def delete_tables(self):
        drop_tables = "DROP TABLE IF EXISTS users, parcels"
        self.cursor.execute(drop_tables)


if __name__ == "__main__":
    DBCon = DBConnection()
    

