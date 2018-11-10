# SendIT API

## Usage

All response will have the form

```json
{
  "users": {},
  "parcels": {}
}
```

### Fetch all parcels

**Definition**

`GET /parcels`

**Responses**

- `200 OK` on success

```json
{
  parcelId: {
    "userId": userId,
    "parcelId": parcelId,
    "p_from": "Kampala, Uganda",
    "to": "Kisumu, Kenya",
    "weight": "1.2",
    "price": "4000",
    "status": "Not Delivered"
  },
  parcelId: {
    "userId": userId,
    "parcelId": parcelId,
    "p_from": "Kampala, Uganda",
    "to": "Nairobi, Kenya",
    "weight": "0.5",
    "price": "3000",
    "status": "Not Delivered"
  }
}
```

### Creating a new Parcel

**Definitions**

`POST /parcels`

**Arguments**

- `"p_from: string"` Parcel's Source
- `"To: string"` Parcel's Destination
- `"weight: string"` Parcel's weight

**Responses** 

- `201 Created` on success
- `404 Not Found` if the device does not exist

```json
{
  "userId": userId,
  "parcelId": parcelId,
  "p_from": "Kampala, Uganda",
  "to": "Kisumu, Kenya",
  "weight": "1.2",
  "price": "4000",
  "sent": 0,
  "status": "Not Delivered"
}
```

### Creating a new User

**Definitions**

`POST /users`

**Arguments**

- `"Firstname: string"` User's Firstname
- `"Lastname: string"` User's Lastname
- `"Phone: string"` User's Phone number
- `"email: string"` User's email address
- `"Address: string"` User's Address
- `"Password: string"` User's Password

**Responses** 
- `201 Created` on success

```json
{
  "userId": "user_id",
  "firstname": "firstname",
  "lastname": "lastname",
  "email": "email",
  "phone": "phone",
  "address": "address",
  "password": "password",
  "sent": 0,
  "received": 0,
  "status": "active"
}
```

### Fetch specific Parcel Delivery Order

**Definition**

`GET /parcels/parcelId`

**Responses**

- `200 OK` on success
- `404 Not Found` if the device does not exist

```json
{
  parcelId: {
    "userId": parcelId,
    "parcelId": 15727377,
    "p_from": "Kampala, Uganda",
    "to": "Kisumu, Kenya",
    "weight": "1.2",
    "price": "4000",
    "status": "Not Delivered"
  }
}
```

### Fetch all parcel delivery orders by a specific user

**Definition**

`GET /users/<userId>/parcels`

**Responses**

- `200 OK` on success
- `404 Not Found` if the device does not exist

```json
  user: {
    "userId": userId,
    "firstname": "Roghashin",
    "lastname": "Timbiti",
    "email": "rtimbiti@gmail.com",
    "phone": "0777579402",
    "address": "Nsambya",
    "password": "password",
    "sent": 0,
    "received": 0,
    "status": "active"
  }
  parcels: {
    "15727377": {
      "userId": userId,
      "parcelId": parcelId,
      "p_from": "Kampala, Uganda",
      "to": "Kisumu, Kenya",
      "weight": "1.2",
      "price": "4000",
      "status": "Not Delivered"
    },
    "15727872": {
      "userId": userId,
      "parcelId": parcelId,
      "p_from": "Kampala, Uganda",
      "to": "Da res alaam, Tanzania",
      "weight": "0.6",
      "price": "6000",
      "status": "Not Delivered"
    }
  }
```

### Cancel the specific parcel delivery order

**Definition**

`PUT parcels/<parcelId>/cancel`

**Responses**

- `204 No Content` on success
- `404 Not Found` if the device does not exist

```json
  {

  }
```