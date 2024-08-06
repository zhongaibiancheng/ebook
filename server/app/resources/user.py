#!/usr/bin/env python
import psycopg2
import requests
from flask import Flask, request,Blueprint,redirect, url_for
from flask_restful import Resource, Api,reqparse
from flask import json,g
from flask_cors import CORS, cross_origin
from werkzeug.security import check_password_hash, generate_password_hash

from app import app
from app.utils.mail import send_mail,send_mail_with_html,send_mail_with_attachment
from app.database.db_helper import db_helper
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

user_bp = Blueprint('user_api', __name__)
user_api = Api(user_bp)

from app.utils.logging import get_logger
logger = get_logger()

from app.resources.auth import token_auth

def check_username(value, name):
    if len(value) == 0:
        raise ValueError("请输入用户名")

    if len(value) < 3:
        raise ValueError('用户名长度应该大于 3')

    # 如果没有错误，返回有效的值
    return value
    
def check_password(value,name):
    if len(value) == 0:
        raise ValueError("请输入密码")

    if len(value) <6:
        raise ValueError("密码长度应该大于 6")
    
    return value

def check_confirm_password(value,name):
    if len(value) == 0:
        raise ValueError("请输入确认密码")

    if len(value) <6:
        raise ValueError("确认密码长度应该大于 6")
    
    return value

class User(Resource):
    def post(self):
        #输入参数检查
        parser = reqparse.RequestParser(bundle_errors=True)
        
        parser.add_argument(
            "username",
            type=check_username,  # 使用自定义验证器
            required=True,
            )

        parser.add_argument(
            "password",
            type=check_password,
            required=True)

        args = parser.parse_args()

        username = args["username"]
        password = args["password"]

        logger.info(args)

        sql = '''
                select 
                    id,
                    username,
                    email,
                    phone 
                from 
                    users 
                where 
                    username='%s' and 
                    deleted_flg = 0'''%(username)

        with db_helper.get_resource(app.config,autocommit=False) as (cur,conn):
            try:
                logger.info(sql)
                cur.execute(sql)
                
                user = cur.fetchone()

                if not user:
                    response = app.response_class(
                        response=json.dumps({
                            'message':'用户名或者密码错误',
                            'code':404
                            }),
                        status=200,
                        mimetype='application/json'
                    )
                    return response

                sql = '''
                    select 
                        password,
                        id,
                        username 
                    from 
                        users 
                    where 
                        id=%d'''%(user['id'])
                logger.info(sql)
                cur.execute(sql)

                user = cur.fetchone()

                password_db = user['password']
                if check_password_hash(password_db, password):#用户名密码正确配对
                    response = app.response_class(
                    response=json.dumps({
                        'user':user,
                        'code': 200,user
                        }),
                    status=200,
                    mimetype='application/json'
                )
                else:#用户名密码不正确配对
                    message = '用户名或者密码错误'
                    response = app.response_class(
                        response=json.dumps({
                            'message':'用户名或者密码错误',
                            'code':404
                            }),
                        status=200,
                        mimetype='application/json'
                    )
                return response
            except (Exception, psycopg2.DatabaseError) as error:
                logger.info(error)

    def get(self,id):
        
        logger.info("login/user_id="+id)
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
    def _check_exists(self,username):
        sql = "select count(1) as cnt from users where username='%s'"%(username)
        logger.info(sql)
        with db_helper.get_resource(app.config,autocommit=False) as (cur,conn):
            try:
                cur.execute(sql)
                one = cur.fetchone()

                if one['cnt'] == 0:
                    return False
                else:
                    return True
            except (Exception, psycopg2.DatabaseError) as error:
                logger.error(error)
                raise error
        
        return False

    '''
    用户登录 api
    '''
    def post(self):
        #输入参数检查
        parser = reqparse.RequestParser(bundle_errors=True)
        
        parser.add_argument(
            "username",
            type=check_username,  # 使用自定义验证器
            required=True,
            )

        parser.add_argument(
            "password",
            type=check_password,
            required=True)

        parser.add_argument(
            "confirm_password",
            type=check_confirm_password,
            required=True)
        args = parser.parse_args()

        username = args["username"]
        password = args["password"]

        if self._check_exists(username):
            response = app.response_class(
                response=json.dumps({
                    'code': 400,
                    'message':'用户名:%s已经存在了'%(username),
                    }),
            status=200,
            mimetype='application/json')

            return response
        if password == args["confirm_password"]:#insert into db
            with db_helper.get_resource(app.config,autocommit=False) as (cur,conn):
                try:
                    sql = '''
                        insert into users(username,password,created_at,updated_at)values(
                        '%s','%s',now(),now()
                        )RETURNING id
                    '''%(username,generate_password_hash(password))
                    logger.info(sql)

                    cur.execute(sql)

                    id = cur.fetchone()['id']

                    conn.commit()

                    response = app.response_class(
                        response=json.dumps({
                            'code': 200,
                            'user':{
                                'id':id,
                            'username':username
                            },
                            }),
                    status=200,
                    mimetype='application/json')

                    return response
                except (Exception, psycopg2.DatabaseError) as error:
                    logger.error(error)
                    conn.rollback()
                    raise error
        else:
            response = app.response_class(
                response=json.dumps({
                    'code': 400,
                    'message':'密码和确认密码不一致',
                    }),
                status=200,
                mimetype='application/json')

            return response
    
    def get(self):
        return self.post()

user_api.add_resource(User,"/login","/login/<int:id>",methods=['POST','GET'],endpoint='login_api')
user_api.add_resource(UserRegist,"/signin",methods=['POST','GET'])
