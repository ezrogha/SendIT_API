import unittest
import json
from run import app
from api.models.database import DBConnection
from api.models.users import deleteTables
from flask_jwt_extended import get_jwt_identity 
from tests.data import *

class TestUsers(unittest.TestCase):

    def setUp(self):
        # To run before each function in the test class
        self.db = DBConnection()

    def tearDown(self):
        # To run after each function in the test class
        deleteTables()


    def register_user(self):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(test_user_register_data))
        return response

    def post_username(self):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(username_signup))
        return response

    def post_password(self):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(password_signup))
        return response

    def post_address(self):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(address_signup))
        return response


    def register_admin(self):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(test_admin_register_data))
        return response


    def invalid_login(self):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/login",
            content_type="application/json",
            data=json.dumps({
                "username": "EZogha",
                "password": "000000"
            })
        )
        return response


    def get_token(self):
        tester = app.test_client()
        token = tester.post(
            "/api/v2/login",
            content_type="application/json",
            data=json.dumps({
                "username": "EZRogha",
                "password": "1234567"
            })
        )
        return token


    def get_admin_token(self):
        tester = app.test_client()
        token = tester.post(
            "/api/v2/login",
            content_type="application/json",
            data=json.dumps({
                "username": "Timbiti",
                "password": "22222"
            })
        )
        return token
        
    def set_parcel(self, token):
        tester = app.test_client()
        response = tester.post(
            "/api/v2/parcels",
            content_type="application/json",
            data=json.dumps(test_create_parcel),
            headers={'Authorization': token})
        return response

    # def test_signup_username():


    def test_signup(self):
        """
         Test GET and POST requests on the signup page
        """
        tester = app.test_client()
        response_get = tester.get(
            "/api/v2/signup",
            content_type="application/json")
        response_post = self.register_user()
        self.assertEqual(response_get.status_code, 200)
        self.assertTrue(b"Please Register" in response_get.data)
        self.assertEqual(response_post.status_code, 201)
        self.assertTrue(b"Account has been created" in response_post.data)


    def test_username_post(self):
        response = self.post_username()
        self.assertEqual(response.status_code, 400)

    def test_password_post(self):
        response = self.post_password()
        self.assertEqual(response.status_code, 400)

    def test_address_post(self):
        response = self.post_address()
        self.assertEqual(response.status_code, 400)


    def test_login(self):
        """ Test GET and POST requests for valid login
            First we send test data through signup route """

        tester = app.test_client()
        self.register_user()
        response_get = tester.get(
            "/api/v2/login",
            content_type="application/json")
        response_post = self.get_token()
        self.assertEqual(response_get.status_code, 200)
        self.assertTrue(b"Please Login" in response_get.data)
        self.assertEqual(response_post.status_code, 200)


    def test_invalid_login(self):
        """ Test GET and POST requests for valid login
            First we send test data through signup route """

        tester = app.test_client()
        self.register_user()
        response_get = tester.get(
            "/api/v2/login",
            content_type="application/json")

        response_post = self.invalid_login()
        self.assertTrue(b"User doesnot exist" in response_post.data)
        self.assertTrue(b"Please Login" in response_get.data)


    def  test_userParcels(self):
        tester = app.test_client()
        self.register_user()

        response = self.get_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response_get = tester.get(
            "/api/v2/users/1/parcels",
            content_type="application/json",
            headers = {'Authorization': token })
        self.assertEqual(response_get.status_code, 200)
        

    def test_allUsers(self):
        tester = app.test_client()
        self.register_admin()

        response = self.get_admin_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response_get = tester.get(
            "/api/v2/users",
            content_type="application/json",
            headers = {'Authorization': token })
        self.assertEqual(response_get.status_code, 200)
        

    def test_allParcels(self):
        tester = app.test_client()
        self.register_admin()

        response = self.get_admin_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response_get = tester.get(
            "/api/v2/parcels",
            content_type="application/json",
            headers = {'Authorization': token })
        self.assertEqual(response_get.status_code, 200)


    def test_parcel(self):
        tester = app.test_client()
        self.register_user()

        response = self.get_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response = self.set_parcel(token)
        response_get = tester.get(
            "/api/v2/parcels/1",
            content_type="application/json",
            headers = {'Authorization': token})
        self.assertEqual(response_get.status_code, 200)


    def test_cancelParcel(self):
        tester = app.test_client()
        self.register_user()

        response = self.get_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response = self.set_parcel(token)
        response_get = tester.put(
            "/api/v2/parcels/1/cancel",
            content_type="application/json",
            headers = {'Authorization': token})
        self.assertEqual(response_get.status_code, 200)

    def test_sendParcel(self):
        tester = app.test_client()
        self.register_user()

        response = self.get_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response = self.set_parcel(token)
        response_get = tester.put(
            "/api/v2/parcels/1/send",
            content_type="application/json",
            headers = {'Authorization': token})
        self.assertEqual(response_get.status_code, 200)


    def test_changeDestination(self):
        tester = app.test_client()
        self.register_user()

        response = self.get_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response = self.set_parcel(token)
        response_get = tester.put(
            "/api/v2/parcels/1/destination",
            content_type="application/json",
            data=json.dumps({"destination": "Gulu"}),
            headers = {'Authorization': token})
        self.assertEqual(response_get.status_code, 200)

    
    def test_changeLocation(self):
        tester = app.test_client()
        self.register_admin()

        response = self.get_admin_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response = self.set_parcel(token)
        response_get = tester.put(
            "/api/v2/parcels/1/location",
            content_type="application/json",
            data=json.dumps({"location": "Bushenyi"}),
            headers = {'Authorization': token})
        self.assertEqual(response_get.status_code, 200)

    
    def test_changeStatus(self):
        tester = app.test_client()
        self.register_admin()

        response = self.get_admin_token()
        data = json.loads(response.data.decode())
        token = 'Bearer ' + data["access_token"]
        response = self.set_parcel(token)
        response_get = tester.put(
            "/api/v2/parcels/1/status",
            content_type="application/json",
            data=json.dumps({"status": "Delivered"}),
            headers = {'Authorization': token})
        self.assertEqual(response_get.status_code, 200)