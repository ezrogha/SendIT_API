# SendIT API

## Badges
 [![Build Status](https://travis-ci.org/ezrogha/SendIT_API.svg?branch=features)](https://travis-ci.org/ezrogha/SendIT_API)
 [![Coverage Status](https://coveralls.io/repos/github/ezrogha/SendIT_API/badge.svg?branch=features)](https://coveralls.io/github/ezrogha/SendIT_API?branch=features)
 [![Maintainability](https://api.codeclimate.com/v1/badges/39caaa1fe94e4554a26c/maintainability)](https://codeclimate.com/github/ezrogha/SendIT_API/maintainability)

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
    "userId": "<userId>",
    "parcelId": "<parcelId>",
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
