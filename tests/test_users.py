import unittest
from run import app
from datetime import datetime
from time import mktime

class TestParcels(unittest.TestCase):

  def test_users(self):
      dt = datetime.now()
      user_id = str(int(mktime(dt.timetuple())))
      tester = app.test_client(self)
      response_get = tester.get("/api/v1/users", content_type="html/text")
      response_post = tester.post(
          "/api/v1/users",
          data=dict(
              userId=user_id,
              firstname="Trashin",
              lastname="Nasimolo",
              email="nasimol@gmail.com",
              phone="0777579402",
              address="Nsambya",
              password="trasj"
          )
      )
      message = b"No Users currently available"
      self.assertEqual(response_get.status_code, 200)
      self.assertTrue(message in response_get.data)
      self.assertTrue(b"Hello Trashin" in response_post.data)
