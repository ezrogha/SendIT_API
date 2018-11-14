import unittest
from run import app

class TestParcels(unittest.TestCase):
  
  def test_home(self):
    tester = app.test_client()
    response = tester.get("/api/v1/", content_type="html/text")
    message = b"Welcome to SendIT api"
    self.assertTrue(message in response.data)

  def test_parcels(self):
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
    response = tester.get("/api/v1/parcels", content_type="html/text")
    message_post = b"UserId not defined"
    message = b"No Parcels currently available"
    self.assertIn(message_post, response_post.data,)
    self.assertEqual(response.status_code, 200)
    self.assertIn(message, response.data)


  def test_get_parcel(self):
    tester = app.test_client(self)
    response = tester.get(
        "/api/v1/parcels/1541802758_0", content_type="html/text")
    self.assertIn(b"The Parcel with this id 1541802758_0 was not found...", response.data)

  
  def test_cancel_parcel(self):
    tester = app.test_client(self)
    response = tester.put(
        "/api/v1/parcels/1541802758_0/cancel", content_type="html/text")
    # response2 = tester.put(
    #     "/api/v1/parcels/444444/cancel", content_type="html/text")
    # self.assertEqual(response.status_code, 200)
    # self.assertIn(b"Order 1541802758_0 has been cancelled", response.data)
    self.assertIn(b"Parcel with this id 1541802758_0 was not found...", response.data)