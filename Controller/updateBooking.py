from flask import Flask,request,Blueprint,jsonify

from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')

from booking import Booking,eng
from tokenAuthentication import token_required
from passlib.hash import sha256_crypt as algo
update_booking=Blueprint('update_booking',__name__)

@update_booking.route('/updateBooking',methods=['PUT'])
@token_required
def upb():
    try:
        if request.method=="PUT":
            bid=request.form['bid']
            bdate = request.form['bdate']
            QueueNo=request.form['QueueNo']
            time=request.form['time']
            tid=request.form['tid']
            sid=request.form['sid']
            cemail=request.form['cemail']
            

            Session = sessionmaker(bind=eng)
            ses = Session()


            
            booking = ses.query(Booking).filter_by(bid=bid).update(dict(bname=bname,bdate=bdate,gender=gender,age=age,bphone=bphone,QueueNo=QueueNo,time=time,tid=tid,sid=sid,cemail=cemail))
            ses.commit()
            response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)
