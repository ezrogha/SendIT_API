from app import app
import unittest


class TestApp(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Welcome to SendIT api" in response.data)

    def test_users(self):
        tester = app.test_client(self)
        response_get = tester.get("/api/v1/users", content_type="html/text")
        response_post = tester.post(
            "/api/v1/users",
            data=dict(
                firstname="Roghashin",
                lastname="Timbiti",
                email="rtimbiti@gmail.com",
                phone="0777579402",
                address="Nsambya",
                password="Roghashin19"
            )
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertIn(b"Welcome Roghashin", response_post.data)

    def test_parcels(self):
        tester = app.test_client(self)
        response_get = tester.get("/api/v1/parcels", content_type="html/text")
        response_post = tester.post(
            "/api/v1/parcels",
            data=dict(
                userId="1541802758",
                p_from="Kampala, Uganda",
                to="Kigali, Rwanda",
                weight="1.2"
            )
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertIn(b"A parcel is created by user 1541802758",
                      response_post.data)

    def test_get_parcel(self):
        tester = app.test_client(self)
        response = tester.get(
            "/parcels/1541802758_0", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"1541802758_0", response.data)

    def test_get_user_parcels(self):
        tester = app.test_client(self)
        response_get = tester.get(
            "/users/1541802758/parcels", content_type="html/text")
        response_post = tester.post(
            "/users/1541802758/parcels",
            data=dict(
                p_from="Kampala, Uganda",
                to="khartuom, Sudan",
                weight="1.8"
            )
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertIn(b"list of 1541802758 parcels", response_post.data)

    def def test_cancel_parcel(self):
        tester = app.test_client(self)
        response = tester.put(
            "/parcels/1541802758_0/cancel", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Content for 1541802758_0 Not Found", response.data)


if __name__ == "__main__":
    unittest.main()
