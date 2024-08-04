import json

from tests.base import BaseTestCase
from praya_institue import app
 
class TestUserAPI(BaseTestCase):
  def test_post_user_login_no_email(self):
    params = {
        'email':'email',
        'password':'password'
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    print(response)
    self.assert_200(response)
    # self.assert_status(response, 201)
 
    # data = json.loads(response.get_data())
    # id = data['id']
    # response = self.app.get(f'/hoges/{id}')
    # self.assert_status(response, 200)

 