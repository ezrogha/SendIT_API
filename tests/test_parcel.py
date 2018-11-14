import unittest
from run import app

class TestParcels(unittest.TestCase):
  
  def test_home(self):
    tester = app.test_client()
    response = tester.get("/api/v1/", content_type="html/text")
    message = b"Welcome to SendIT api"
    self.assertTrue(message in response.data)

  def test_get_parcels(self):
    tester = app.test_client()
    response_post = tester.post(
        "/api/v1/users/parcels",
        data=dict(
            p_from="Kampala, Uganda",
            to="khartuom, Sudan",
            weight="1.8"
        )
    )
    response = tester.get("/api/v1/parcels", content_type="html/text")
    message1 = b"UserId not defined"
    message2 = b"No Parcels currently available"
    self.assertIn(message1 in response_post.data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(message2 in response.data)