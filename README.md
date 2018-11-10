# SendIT API

## Badges
 [![Build Status](https://travis-ci.org/ezrogha/SendIT_API.svg?branch=features)](https://travis-ci.org/ezrogha/SendIT_API)
## Heroku
https://sendit-api-.herokuapp.com/api/v1/

## Pivotal Tracker
https://www.pivotaltracker.com/n/projects/2224545

## Features
- User can fetch all parcel delivery orders
- User can view details of a specific order
- User can create a parcel delivery order
- User can cancel parcel delivery order
- User can view all parcel delivery orders from a specific user
- User can fetch all users
- User can create a new user

## Sample Data
```json
db = {
    "_response": {
      "code": "",
      "message": ""
    },
    "parcels": {
        "1541802758_0": {
            "from": "Kla",
            "parcelId": "1541802758_0",
            "price": "3200",
            "status": "Not Delivered",
            "to": "Kigali",
            "userId": "1541802758",
            "weight": "1.2"
        },
        "1541802758_1": {
            "from": "Kla",
            "parcelId": "1541802758_1",
            "price": "1600",
            "status": "Not Delivered",
            "to": "Kisumu",
            "userId": "1541802758",
            "weight": "0.7"
        },
        "1541802758_2": {
            "from": "Kla",
            "parcelId": "1541802758_2",
            "price": "2200",
            "status": "Not Delivered",
            "to": "Da res alaam",
            "userId": "1541802758",
            "weight": "0.8"
        },
        "1541803030_3": {
            "from": "Entebbe",
            "parcelId": "1541803030_3",
            "price": "40000",
            "status": "Not Delivered",
            "to": "New York",
            "userId": "1541803030",
            "weight": "0.87"
        }
    },
    "users": {
        "1541802758": {
            "address": "Nsambya",
            "email": "rtimbi@",
            "firstname": "Rogha",
            "lastname": "Timbi",
            "password": "null",
            "phone": "036489",
            "received": 0,
            "sent": 0,
            "status": "active",
            "userId": "1541802758"
        },
        "1541803030": {
            "address": "Entebbe",
            "email": "rorine@",
            "firstname": "Roshin",
            "lastname": "Masika",
            "password": "null",
            "phone": "043909",
            "received": 0,
            "sent": 0,
            "status": "active",
            "userId": "1541803030"
        }
    }
}
```

## Usage

All response will have the form

```json
{
  "_response": {},
  "users": {},
  "parcels": {}
}
```

### Fetch all parcels

**Definition**

`GET /api/v1/parcels`

**Responses**

- `200 OK` on success

```json
{
  "parcelId": {
    "userId": "<userId>",
    "parcelId": "<parcelId>",
    "p_from": "Kampala, Uganda",
    "to": "Kisumu, Kenya",
    "weight": "1.2",
    "price": "4000",
    "status": "Not Delivered"
  },
  "parcelId": {
    "userId": "<userId>",
    "parcelId": "<parcelId>",
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

`POST /api/v1/parcels`

**Arguments**

- `"p_from: string"` Parcel's Source
- `"To: string"` Parcel's Destination
- `"weight: string"` Parcel's weight

**Responses** 

- `201 Created` on success
- 

```json
{
  "userId": "<userId>",
  "parcelId": "<parcelId>",
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

`POST /api/v1/users`

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
  "userId": "<user_id>",
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

`GET /api/v1/parcels/<parcelId>`

**Responses**

- `200 OK` on success
- `404 Not Found` if the parcel does not exist

```json
{
  "parcelId": {
    "userId": "<parcelId>",
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

`GET /api/v1/users/<userId>/parcels`

**Responses**

- `200 OK` on success
- `404 Not Found` if the User does not exist

```json
  user: {
    "userId": "<userId>",
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
      "userId": "<userId>",
      "parcelId": "<parcelId>",
      "p_from": "Kampala, Uganda",
      "to": "Kisumu, Kenya",
      "weight": "1.2",
      "price": "4000",
      "status": "Not Delivered"
    },
    "15727872": {
      "userId": "<userId>",
      "parcelId": "<parcelId>",
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

`PUT /api/v1/parcels/<parcelId>/cancel`

**Responses**

- `204 No Content` on success
- `404 Not Found` if the parcel does not exist

```json
  {

  }
```
