from flask import Flask,request,Blueprint,jsonify

from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')

from admin import Admin,eng
from login import Login
from tokenAuthentication import token_required
from passlib.hash import sha256_crypt as algo
update_admin=Blueprint('update_admin',__name__)

@update_admin.route('/updateAdmin',methods=['PUT'])
@token_required
def Up():
    try:
        if request.method=="PUT":
         
            aname=request.form['aname']
            aemail = request.form['aemail']
            curremail=request.form['curremail']
            apassword = request.form['apassword']
            apriority = request.form['apriority']
            apassword = algo.encrypt(apassword)
            Session = sessionmaker(bind=eng)
            ses = Session()
            admin = ses.query(Admin).filter_by(aemail=curremail).update(dict(aname=aname,aemail=aemail, apassword= apassword,apriority=apriority))
            print(admin)
            login = ses.query(Login).filter_by(email=curremail).update(dict(email=aemail, password= apassword,role='Admin'))
            print(login)
            ses.commit()
            
            response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)
