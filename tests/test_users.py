import unittest
from run import app

class TestParcels(unittest.TestCase):
  
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
      message = b"No Users are currently available"
      self.assertEqual(response_get.status_code, 200)
      self.assertTrue(message in response_get.data)
      self.assertIn(b"Hello Trashin", response_post.data)
