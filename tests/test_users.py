import unittest
from run import app
from datetime import datetime
from time import mktime

class TestParcels(unittest.TestCase):


  def test_get_users(self):
      tester = app.test_client()
      response_get = tester.get("/api/v1/users", content_type="application/json")
      message = b"No Users currently available"
      self.assertEqual(response_get.status_code, 200)
      self.assertTrue(message in response_get.data)


  def test_set_users(self):
    tester = app.test_client()
    dt = datetime.now()
    user_id = str(int(mktime(dt.timetuple())))
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
    self.assertTrue(b"Hello Trashin" in response_post.data)


  def test_get_user_parcels(self):
    tester = app.test_client()
    response_get = tester.get(
        "/api/v1/users/1541802758/parcels", content_type="application/json")
    self.assertIn(b"User with this id 1541802758 was not found...", response_get.data)

  
  def test_set_user_parcels(self):
    tester = app.test_client()
    response_post = tester.post(
        "/api/v1/users/1234567/parcels",
        data=dict(
            p_from="Kampala, Uganda",
            to="khartuom, Sudan",
            weight="1.8"
        )
    )
    self.assertIn(b"User with this id 1234567 was not found...", response_post.data)
    

    
    
