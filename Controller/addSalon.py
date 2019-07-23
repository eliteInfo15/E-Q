from flask import Flask,request,Blueprint,jsonify
from passlib.hash import sha256_crypt as algo
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')




add_salon=Blueprint('add_salon',__name__)
from app import app
from salon import Salon,eng
from tokenAuthentication import token_required
@add_salon.route('/addSalon',methods=['POST'])
@token_required
def add_sal():
    try:
        if request.method=='POST':
            sname=request.form['sname']
            semail = request.form['semail']
            spassword = request.form['spassword']
            sphone = request.form['sphone']
            saddress = request.form['saddress']
            sarea = request.form['sarea']

            spassword = algo.encrypt(spassword)
            Session = sessionmaker(bind=eng)
            ses = Session()
            su = Salon(sname,semail,spassword,sphone,saddress,sarea )
            ses.add_all([su])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)