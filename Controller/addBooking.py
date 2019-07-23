from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')





add_Booking=Blueprint('add_Booking',__name__)
from app import app
from booking import Booking,eng
from tokenAuthentication import token_required
@add_Booking.route('/addBooking',methods=['POST'])
@token_required
def add_b():
    try:
        if request.method=='POST':
            bdate = request.form['bdate']
            QueueNo=request.form['QueueNo']
            time=request.form['time']
            tid=request.form['tid']
            sid=request.form['sid']
            cemail=request.form['cemail']
            

            Session = sessionmaker(bind=eng)
            ses = Session()


            su = Booking(bname,bdate,gender,age,bphone,QueueNo,time,tid,sid,cemail)
            ses.add_all([su])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response = {'status': 0, 'statusMessage': str(e)}
    return jsonify(response)
       

