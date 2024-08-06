import json

from tests.base import BaseTestCase
from ebook import app
 
from app.database.db_helper import db_helper
from werkzeug.security import generate_password_hash

class TestUserAPI(BaseTestCase):
  def init_db(self):
    password = generate_password_hash('password')
    with db_helper.get_resource(app.config,autocommit=False) as (cur,conn):
      try:
        sql = "insert into users(username,password,created_at,updated_at)values('abcdef','%s',now(),now())"%(password)
        cur.execute(sql)
        conn.commit()
      except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()

  def clean(self):
    with db_helper.get_resource(app.config,autocommit=False) as (cur,conn):
      try:
        sql = "delete from users"
        cur.execute(sql)
        conn.commit()
      except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()

  def setUp(self):
    super().setUp()
    self.init_db()
  
  def tearDown(self):
    super().tearDown()
    self.clean()
  
  def test_post_user_login_username_not_exist_in_params(self):
    params = {
        'username':'',
        'password':'password'
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['username'] == '请输入用户名'

  def test_post_user_login_username_len_2(self):
    params = {
        'username':'ab',
        'password':'password'
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['username'] == '用户名长度应该大于 3'

  def test_post_user_login_password_len_5(self):
    params = {
        'username':'abc',
        'password':'pass'
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['password'] == '密码长度应该大于 6'

  def test_post_user_login_password_not_exist_in_params(self):
    params = {
        'username':'abc',
        'password':''
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['password'] == '请输入密码'

  def test_post_user_login_username_exist_in_db_password_wrong(self):
    # self.init_db()
    params = {
        'username':'abcdef',
        'password':'passwordq'
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 200 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['code'] == 404
    assert data['message'] == '用户名或者密码错误'

  def test_post_user_login_ok(self):
    params = {
        'username':'abcdef',
        'password':'password'
    }
    response = self.app.post(
        '/api/user/login',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 200 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['code'] == 200

    assert data['user']['username'] == 'abcdef'

  ###################################################
  ###################################################
  #####################signin########################
  ###################################################
  ###################################################
  def test_post_user_sign_password_not_equal_configpassword(self):
    params = {
        'username':'username1',
        'password':'password',
        'confirm_password':'password_'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 200 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['code'] == 400
    assert data['message'] == '密码和确认密码不一致'

  def test_post_user_sign_no_username(self):
    params = {
        'username':'',
        'password':'password',
        'confirm_password':'password_'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['username'] == '请输入用户名'

  def test_post_user_sign_username_len_1(self):
    params = {
        'username':'a',
        'password':'password',
        'confirm_password':'password_'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['username'] == '用户名长度应该大于 3'

  def test_post_user_sign_no_password(self):
    params = {
        'username':'abc',
        'password':'',
        'confirm_password':'password_'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['password'] == '请输入密码'

  def test_post_user_sign_password_len_4(self):
    params = {
        'username':'abc',
        'password':'aass',
        'confirm_password':'password_'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['password'] == '密码长度应该大于 6'

  def test_post_user_sign_no_confirm_password(self):
    params = {
        'username':'abc',
        'password':'abcdef',
        'confirm_password':''
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['confirm_password'] == '请输入确认密码'

  def test_post_user_sign_confirm_password_len_5(self):
    params = {
        'username':'abc',
        'password':'aassdw',
        'confirm_password':'ade23'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['confirm_password'] == '确认密码长度应该大于 6'

  def test_post_user_sign_password_not_equal_confirm_password(self):
    params = {
        'username':'abcdefqw',
        'password':'aassdw',
        'confirm_password':'ade2s3'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 200 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message'] == '密码和确认密码不一致'

  def test_post_user_sign_password_or_username(self):
    params = {
        'username':'',
        'password':'',
        'confirm_password':'ade2s3'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 400 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['message']['username'] == '请输入用户名'
    assert data['message']['password'] == '请输入密码'

  def test_post_user_sign_OK(self):
    params = {
        'username':'abcdefde',
        'password':'aassdw',
        'confirm_password':'aassdw'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 200 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['user']['username'] == 'abcdefde'

  def test_post_user_sign_username_exists(self):
    params = {
        'username':'abcdef',
        'password':'abcdef',
        'confirm_password':'abcdef'
    }
    response = self.app.post(
        '/api/user/signin',
        data=json.dumps(params),
        content_type='application/json')

    assert response.status_code == 200 

    data = response.data.decode('utf-8')
    data = json.loads(data)

    assert data['code'] == 400
    assert data['message'] == '用户名:abcdef已经存在了'