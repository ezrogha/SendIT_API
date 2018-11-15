import unittest
from run import app

class TestParcels(unittest.TestCase):
  
  def test_home(self):
    tester = app.test_client()
    response = tester.get("/api/v1/", content_type="application/json")
    message = b"Welcome to SendIT api"
    self.assertTrue(message in response.data)

  def test_get_parcels(self):
    tester = app.test_client()
    response = tester.get("/api/v1/parcels", content_type="application/json")
    message = b"No Parcels currently available"
    self.assertEqual(response.status_code, 200)
    self.assertIn(message, response.data)


  def test_set_parcel(self):
    tester = app.test_client()
    response_post = tester.post(
        "/api/v1/parcels",
        data=dict(
            userId = "",
            p_from="Kampala, Uganda",
            to="khartuom, Sudan",
            weight="1.8"
        )
    )
    response_post2 = tester.post(
        "/api/v1/parcels",
        data=dict(
            userId = "1234567",
            p_from="Kampala, Uganda",
            to="khartuom, Sudan",
            weight="1.8"
        )
    )
    message_post = b"UserId not defined"
    message_post2 = b"User with 1234567 not defined"
    self.assertIn(message_post, response_post.data,)
    self.assertIn(message_post2, response_post2.data)

  def test_get_parcel(self):
    tester = app.test_client(self)
    response = tester.get(
        "/api/v1/parcels/1541802758_0", content_type="application/json")
    self.assertIn(b"The Parcel with this id 1541802758_0 was not found...", response.data)

  
  def test_cancel_parcel(self):
    tester = app.test_client(self)
    response = tester.put(
        "/api/v1/parcels/1541802758_0/cancel", content_type="application/json")
    response2 = tester.put(
        "/api/v1/parcels/444444/cancel", content_type="html/text")
    self.assertIn(b"Parcel with this id 444444 was not found...", response2.data)
    self.assertIn(b"Parcel with this id 1541802758_0 was not found...", response.data)