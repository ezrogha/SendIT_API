from app import app
import unittest


class TestApp(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Welcome to SendIT api" in response.data)

    def test_users(self):
        tester = app.test_client(self)
        response_get = tester.get("/api/v1/users", content_type="html/text")
        response_post = tester.post(
            "/api/v1/users",
            data=dict(
                firstname="Trashin",
                lastname="Nasimolo",
                email="nasimol@gmail.com",
                phone="0777579402",
                address="Nsambya",
                password="trasj"
            )
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertIn(b"Hello Trashin", response_post.data)

    def test_parcels(self):
        tester = app.test_client(self)
        response_get = tester.get("/api/v1/parcels", content_type="html/text")
        response_post = tester.post(
            "/api/v1/parcels",
            data=dict(
                userId="1541802758",
                p_from="Accra, Ghana",
                to="Tunis, Tunisia",
                weight="1.8"
            )
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertIn(b"A parcel is created by user 1541802758",
                      response_post.data)

    def test_get_parcel(self):
        tester = app.test_client(self)
        response = tester.get(
            "/api/v1/parcels/1541802758_0", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"1541802758_0", response.data)

    def test_get_user_parcels(self):
        tester = app.test_client(self)
        response_get_null_user = tester.get(
            "/api/v1/users/22222/parcels", content_type="html/text")
        response_get = tester.get(
            "/api/v1/users/1541802758/parcels", content_type="html/text")
        response_post = tester.post(
            "/api/v1/users/1541802758/parcels",
            data=dict(
                p_from="Kampala, Uganda",
                to="khartuom, Sudan",
                weight="1.8"
            )
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertIn(b"User with this id 22222 was not found...", response_get_null_user.data)
        self.assertIn(b"A new parcel has been created by user 1541802758", response_post.data)

    def test_cancel_parcel(self):
        tester = app.test_client(self)
        response = tester.put(
            "/api/v1/parcels/1541802758_0/cancel", content_type="html/text")
        response2 = tester.put(
            "/api/v1/parcels/444444/cancel", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Order 1541802758_0 has been cancelled", response.data)
        self.assertIn(b"Parcel with this id 444444 was not found...", response2.data)
        

if __name__ == "__main__":
    unittest.main()
