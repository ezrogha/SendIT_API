from api.models.database import DBConnection

class Parcel(object):

    def __init__(self):
        self.DBConn = DBConnection()
    
    def viewAllParcels(self):
        result = self.DBConn.view_all_parcels()
        return result


    def setParcels(self, parcel_userId, parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status, parcel_location, parcel_creation_date):
        self.DBConn.add_parcel(parcel_userId, parcel_from, parcel_to, parcel_weight,
                        parcel_price, parcel_status, parcel_location, parcel_creation_date)
        return {"message": "Parcel has been created"}


    def parcelDetails(self, parcelId, userId):
        result = self.DBConn.parcel_details(parcelId, userId)
        if result == None:
            return {"message": "OrderId doesnot exist"}
        return result


    def cancelParcelOrder(self, parcelId, userId):
        result = self.DBConn.cancel_parcel(parcelId, userId)
        if result == "Wrong parcelId":
            return {"message": "OrderId does not exist"}
        elif result == "Already Delivered":
            return {"message": "The order cannot be cancelled because it has been delivered already"}
        return {"message": "Delivery Order has been cancelled"}


    def sendParcelOrder(self, parcelId, userId):
        result = self.DBConn.send_parcel(parcelId, userId)
        if result == "Wrong parcelId":
            return {"message": "OrderId does not exist"}
        elif result == "Already Delivered":
            return {"message": "The order cannot be sent because it has been delivered already"}
        return {"message": "Delivery Order is now in transit"}


    def changeParcelDestination(self, parcelId, userId, destination):
        result = self.DBConn.change_destination(parcelId, userId, destination)
        if result == "parcel doesn't exist":
            return {"message": "OrderId does not exist"}
        elif result == "Already Delivered":
            return {"message": "Destination cannot be changed because the parcel has already been delivered"}
        return {"message": f"New Destination for this parcel is {destination}"}


    def changeParcelLocation(self, parcelId, location):
        result = self.DBConn.change_location(parcelId, location)
        if result == "Wrong parcelId":
            return {"message": "OrderId does not exist"}
        elif result == "Already Delivered":
            return {"message": "Location cannot be changed because the parcel has already been delivered"}
        return {"message": f"New Location for this parcel is {location}"}


    def changeParcelStatus(self, parcelId, status):
        result = self.DBConn.change_status(parcelId, status)
        if result == "Wrong parcelId":
            return {"message": "OrderId does not exist"}
        return {"message": f"Status has been set to {status}"}
