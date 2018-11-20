from run import app


@app.route("/api/v2/parcels", methods=["GET", "POST"])
def allParcels():
    pass


@app.route("/api/v1/parcels/<int:parcelId>")
def parcel(parcelId):
    pass


@app.route("/api/v1/parcels/<int:parcelId>/cancel", methods=["PUT"])
def cancelParcel(parcelId):
    pass


@app.route('/api/v2/parcels/<int:parcelId>/destination', methods=["PUT"])
def change_destination():
   pass