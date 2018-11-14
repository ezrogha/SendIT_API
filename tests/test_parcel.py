import unittest
from run import app

class TestParcels(unittest.TestCase):
  
  def test_get_parcels(self):
    tester = app.test_client()
    response = tester.get("/api/v1/", content_type="html/text")
    message = b"Welcome to SendIT api"
    self.assertTrue(message in response.data)