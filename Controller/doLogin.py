from flask import Flask,request,Blueprint,jsonify
import jwt
from sqlalchemy.orm import sessionmaker
import sys
import datetime
sys.path.append('../model')
from passlib.hash import sha256_crypt as algo
do_login=Blueprint('do_login',__name__)
from app import app
from login import Login,eng


@do_login.route('/doLogin',methods=['POST'])

def do_lg():
    try:
        if request.method=='POST':
            email=request.form['email']
            password=request.form['password']
            role=request.form['role']
            Session = sessionmaker(bind=eng)
            ses = Session()
            data=ses.query(Login).filter_by(email=email).first()
            if algo.verify(password, data.password) and email==email and role=='Admin':
                token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
                response = {'status': 1, 'statusMessage': 'Login Successful', 'token': token.decode('UTF-8')}
            elif role=='Customer':
                response = {'status': 1, 'statusMessage': 'Login Successful'}
            else:
                response = {'status': 0, 'statusMessage': 'Invalid Details'}
            
       

    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)