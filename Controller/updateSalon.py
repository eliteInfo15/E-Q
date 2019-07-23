from flask import Flask,request,Blueprint,jsonify

from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')

from salon import Salon,eng
from tokenAuthentication import token_required
from passlib.hash import sha256_crypt as algo
update_salon=Blueprint('update_salon',__name__)

@update_salon.route('/updateSalon',methods=['PUT'])
@token_required
def upb():
    try:
        if request.method=="PUT":
            sid=request.form['sid']
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
            
            salon = ses.query(Salon).filter_by(sid=sid).update(dict(sname=sname,semail=semail,spassword=spassword,sphone=sphone,saddress=saddress,sarea=sarea))
            ses.commit()
            response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)
