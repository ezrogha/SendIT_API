# SendIT_API

SendIT_API is a courier service api that helps users create, view, cancel and send parcel delivery orders to different destinations. SendIT provides courier quotes based on weight categories.

### Badges
 [![Build Status](https://travis-ci.org/ezrogha/SendIT_API.svg?branch=ft-challenge-3)](https://travis-ci.org/ezrogha/SendIT_API)
 [![Coverage Status](https://coveralls.io/repos/github/ezrogha/SendIT_API/badge.svg?branch=ft-challenge-3)](https://coveralls.io/github/ezrogha/SendIT_API?branch=ft-challenge-3)

## Getting Started
```
git clone https://github.com/ezrogha/SendIT_API.git && cd SendIT_API
```

#### Create a [virtual environment](https://virtualenv.pypa.io/en/latest/userguide/)
```
virtualenv venv
source venv/scripts/activate
```
for windows run ```venv\scripts\activate.bat```

#### Install packages
```
pip install -r requirements.txt
```
#### Start app
```
python run.py
```

### Endpoints and Functionality:
| Endpoint                             | Functionality                    |
| ---------                            |---------------                   |
| GET /api/v1/parcels                  | Fetch all delivery orders        |
| POST /api/v1/parcels                 | Create parcel delivery order     |
| GET /api/v1/parcels/<parcelId>       | Fetch a specific delivery order  |
| PUT /api/v1/parcels/<parcelId>/cancel| Cancel specific delivery order   |
| POST /api/v1/users                   | Add user                         |
| GET /api/v1/users                    | Fetch all users                  | 
| GET /api/v1/users/<userId>/parcels   | Fetch orders from a specific user|
| POST /api/v1/users/<userId>/parcels  | Create parcel delivery order     |
 
## Usage

### Fetch all orders

**Definition**

`GET /api/v1/parcels`

**Responses**

- `200 OK` on success

```json
{
    "userId": "<userId>",
    "parcelId": "<parcelId>",
    "p_from": "Parcel's source",
    "to": "Parcel's destination",
    "weight": "parcel weight",
    "price": "parcel price",
    "status": "Delivery status"
}

```

### Creating a new delivery order

**Definitions**

`POST /api/v1/parcels`

**Arguments**

- `"p_from: string"` Parcel's Source
- `"To: string"` Parcel's Destination
- `"weight: int"` Parcel's weight

**Responses** 

- `201 Created` on success
- 

### Fetch specific Parcel Delivery Order

**Definition**

`GET /api/v1/parcels/<parcelId>`

**Responses**

- `200 OK` on success
- `404 Not Found` if the parcel does not exist

```json
{
  "userId": "<userId>",
  "parcelId": "<parcelId>",
  "p_from": "Parcel source",
  "to": "Parcel destination",
  "weight": "parcel weight",
  "price": "delivery price",
  "status": "Not Delivered"
}
```

### Cancel the specific parcel delivery order

**Definition**

`PUT /api/v1/parcels/<parcelId>/cancel`

**Responses**

- `204 No Content` on success
- `404 Not Found` if the parcel does not exist

### Creating a new User

**Definitions**

`POST /api/v1/users`

**Arguments**

- `"Username: string"` User's Lastname
- `"Phone: string"` User's Phone number
- `"email: string"` User's email address
- `"Address: string"` User's Address
- `"Password: string"` User's Password
- `"Role: string"` User's role

**Responses** 
- `201 Created` on success

### Fetch all delivery orders by a specific user

**Definition**

`GET /api/v1/users/<userId>/parcels`

**Responses**

- `200 OK` on success

```json
  {
      "userId": "<userId>",
      "parcelId": "<parcelId>",
      "p_from": "parcel source",
      "to": "parcel destination",
      "weight": "parcel weight",
      "price": "delivery price",
      "status": "Delivered status",
      "location": "Parcel location"
  }
```

## Deployment
- [Heroku]

## Technologies
- [Python](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Postgresql](https://www.postgresql.org/)

## Acknoledgements
- [Andela](https://andela.com/)
