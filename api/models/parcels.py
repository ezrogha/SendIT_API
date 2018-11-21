from api.models.database import DBConnection

DBConn = DBConnection()

def viewAllParcels(parameter_list):
  result = DBConn.view_all_parcels()
  return result
