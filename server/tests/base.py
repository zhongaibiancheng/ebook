import sys

sys.path.append("../")

from flask_testing import TestCase
from app.config import load_config
from praya_institue import app
 
# from src.database import db, init_db
 
 
class BaseTestCase(TestCase):
  def create_app(self):
    app.config.from_object(load_config("TEST"))
    return app
 
  def setUp(self):
    self.app = self.app.test_client()
    # db.create_all()
    # db.session.commit()
 
  def tearDown(self):
    # db.session.remove()
    # db.drop_all()
    pass