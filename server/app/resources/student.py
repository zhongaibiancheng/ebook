from calendar import weekheader
import psycopg2
from app.database.db_helper import db_helper
from flask import Flask, request,Blueprint,jsonify
from flask_restful import Resource, Api
from flask import json,g

import requests
import xmltodict
import hashlib
import random
import string
from datetime import datetime
from flask_cors import CORS, cross_origin
import os
import time
from werkzeug.utils import secure_filename

from app import app

import shutil

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

student_bp = Blueprint('student_api', __name__)
student_api = Api(student_bp)

from app.utils.logging import get_logger
logger = get_logger()

from app.resources.auth import token_auth

class CourseResource(Resource):
    def get(self):
        courses = {
            "en":[
                {"title":"2024 AMC K12","id":1},
                {"title":"2024 AMC K10","id":2},
                {"title":"2024 Kangroo Math K6","id":4},
            ],            
            "zh_j":[
                {"title":"2024 美国数学竞赛 K12","id":1},
                {"title":"2024 美国数学竞赛 K10","id":2},
                {"title":"2024 袋鼠数学 K6","id":4},
            ],
            "zh_f":[
                {"title":"2024 美國數學競賽 K12","id":1},
                {"title":"2024 美國數學競賽 K10","id":2},
                {"title":"2024 袋鼠數學 K6","id":4},
            ],
        }
        response = app.response_class(
            response=json.dumps({
                'courses':courses,
                'code': 200,
                'status':'success'
                }),
            status=200,
            mimetype='application/json')

        return response
###### url mapping
student_api.add_resource(CourseResource,"/courses",methods=['GET'])
