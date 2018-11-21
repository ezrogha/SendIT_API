from api.models.database import DBConnection

DBConn = DBConnection()


def viewAllParcels(parameter_list):
    result = DBConn.view_all_parcels()
    return result


def parcelDetails(parcelId):
    result = DBConn.parcel_details(parcelId)
    if result == None:
        return {"message": "OrderId doesnot exis"}
    return result


