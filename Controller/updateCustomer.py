from flask import Flask,request,Blueprint,jsonify

from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')

from customer import Customer,eng
from login import Login
from tokenAuthentication import token_required
from passlib.hash import sha256_crypt as algo
update_customer=Blueprint('update_customer',__name__)

@update_customer.route('/updateCustomer',methods=['PUT'])
@token_required
def upc():
    try:
        if request.method=="PUT":
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
            customer= ses.query(Customer).filter_by(cemail=cemail).update(dict(cname=cname,cpassword=cpassword,cemail=cemail,locality=locality,state=state,gender=gender,age=age,cphone=cphone))
            login = ses.query(Login).filter_by(email=cemail).update(dict(email=cemail, password= cpassword,role='Customer'))
            ses.commit()
            response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)
