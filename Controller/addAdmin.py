from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from passlib.hash import sha256_crypt as algo
add_admin=Blueprint('add_admin',__name__)
from app import app
from admin import Admin,eng
from login import Login

@add_admin.route('/addAdmin',methods=['POST'])

def add_ad():
    try:
        if request.method=='POST':
            aname=request.form['aname']
            aemail = request.form['aemail']
            apassword = request.form['apassword']
            apriority = request.form['apriority']
            

            apassword = algo.encrypt(apassword)



            Session = sessionmaker(bind=eng)
            ses = Session()
            
            su = Admin(aname,aemail,apassword,apriority )
            pa= Login (aemail,apassword,'Admin')
            ses.add_all([su,pa])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)