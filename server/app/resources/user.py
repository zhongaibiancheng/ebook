#!/usr/bin/env python
from calendar import weekheader
import datetime
import psycopg2
from app.database.db_helper import db_helper

from flask import Flask, request,Blueprint
from flask_restful import Resource, Api
from flask import json,g

from flask_cors import CORS, cross_origin

import random, string

import time
import jwt
from app import app

from app.utils.mail import send_mail,send_mail_with_html,send_mail_with_attachment

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

user_bp = Blueprint('user_api', __name__)
user_api = Api(user_bp)

from app.utils.logging import get_logger
logger = get_logger()

import requests

import os
import base64

from flask_cors import CORS, cross_origin
from app.resources.auth import token_auth

class User(Resource):
    def post(self):
        email = request.json.get("email")
        password = request.json.get("password")
        if not email:
            pass
        logger.info(email)
        logger.info(password)

        response = app.response_class(
            response=json.dumps({
                'error_code':'login.error.emailInvalid,login.error.passwordLength',
                'code': 200,
                'status':'success'
                }),
            status=201,
            mimetype='application/json')

        return response

    def get(self):
        email = request.args.get("email")
        password = request.args.get("password")
        logger.info(email)
        logger.info(password)

        response = app.response_class(
            response=json.dumps({
                'error_code':'login.error.emailInvalid,login.error.passwordLength',
                'code': 200,
                'status':'success'
                }),
            status=200,
            mimetype='application/json')

        return response

class UserRegist(Resource):
    def post(self):
        # send_mail("zhongaibiancheng@outlook.com","test","hello text mail")

        # send_mail_with_html("zhongaibiancheng@outlook.com")
        send_mail_with_attachment("zhongaibiancheng@outlook.com")

        response = app.response_class(
            response=json.dumps({
                'code': 200,
                'status':'success'
                }),
            status=201,
            mimetype='application/json')

        return response
    
    def get(self):
        return self.post()

user_api.add_resource(User,"/login",methods=['POST','GET'])
user_api.add_resource(UserRegist,"/signin",methods=['POST','GET'])
