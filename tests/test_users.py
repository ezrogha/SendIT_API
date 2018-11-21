import unittest
import json
from run import app
from api.models.database import DBConnection
from api.models.users import deleteTables


class TestUsers(unittest.TestCase):

    test_user_register_data = {
        "username": "EZRogha",
        "password": "1234567",
        "email": "rtimbiti@gmail.com",
        "phone": "0777579402",
        "address": "Wakiso"
    }

    def setUp(self):
        # To run before each function in the test class
        self.db = DBConnection()

    def tearDown(self):
        # To run after each function in the test class
        deleteTables()


    def test_signup(self):
        # Test GET and POST requests on the signup page
        tester = app.test_client()
        response_get = tester.get(
            "/api/v2/signup",
            content_type="application/json")
        response_post = tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(self.test_user_register_data)
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertTrue(b"Please Register" in response_get.data)
        self.assertEqual(response_post.status_code, 201)
        self.assertTrue(b"Account has been created" in response_post.data)


    def test_login(self):
        """ Test GET and POST requests for valid login
            First we send test data through signup route """

        tester = app.test_client()
        tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(self.test_user_register_data))
        response_get = tester.get(
            "/api/v2/login",
            content_type="application/json")
        response_post = tester.post(
            "/api/v2/login",
            content_type="application/json",
            data=json.dumps({
                "username": "EZRogha",
                "password": "1234567"
            })
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertTrue(b"Please Login" in response_get.data)
        self.assertEqual(response_post.status_code, 200)
        self.assertTrue(b"Welcome EZRogha" in response_post.data)


    def test_invalid_login(self):
        """ Test GET and POST requests for valid login
            First we send test data through signup route """

        tester = app.test_client()
        tester.post(
            "/api/v2/signup",
            content_type="application/json",
            data=json.dumps(self.test_user_register_data))
        response_get = tester.get(
            "/api/v2/login",
            content_type="application/json")
        response_post = tester.post(
            "/api/v2/login",
            content_type="application/json",
            data=json.dumps({
                "username": "EZogha",
                "password": "123567"
            })
        )
        self.assertTrue(b"User doesnot exist" in response_post.data)


        