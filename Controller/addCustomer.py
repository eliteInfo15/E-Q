from flask import Blueprint,jsonify,request
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from passlib.hash import sha256_crypt as algo





add_Customer=Blueprint('add_Customer',__name__)
from app import app
from customer import Customer,eng
from login import Login
from tokenAuthentication import token_required
@add_Customer.route('/addCustomer',methods=['POST'])
@token_required
def add_cu():
    try:
        if request.method=='POST':
            cname=request.form['cname']
            cpassword = request.form['cpassword']
            cemail = request.form['cemail']
            locality = request.form['locality']
            state= request.form['state']
            gender=request.form['gender']
            age=request.form['age']
            cphone=request.form['cphone']

            cpassword = algo.encrypt(cpassword)
            Session = sessionmaker(bind=eng)
            ses = Session() 

            su = Customer(cname,cpassword,cemail,locality,state,gender,age,cphone)
            pa= Login (cemail,cpassword,'Customer')
            ses.add_all([su,pa])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response = {'status': 0, 'statusMessage': str(e)}
    return jsonify(response)
       

