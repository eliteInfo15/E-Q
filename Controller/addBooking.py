from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func,and_
import sys
import datetime
sys.path.append('../model')
add_Booking=Blueprint('add_Booking',__name__)
from app import app
from booking import Booking,eng
from tokenAuthentication import token_required
connection=eng.connect()
@add_Booking.route('/addBooking',methods=['POST'])
@token_required
def add_b():
    try:
        if request.method=='POST':
            tid=request.form['tid']
            sid=request.form['sid']
            cemail=request.form['cemail']
            Session = sessionmaker(bind=eng)
            ses = Session()
            x=datetime.datetime.now()
            bdate=x.date()
            time=x.time()
           
            rb=ses.query(Booking).filter(and_(Booking.bdate==bdate,Booking.sid==sid)).count()
            
            print(rb)
            
            QueueNo=0            
            
            if rb==0:
                QueueNo=1
            elif rb>0:
                QueueNo=rb+1
            su = Booking(bdate,QueueNo,time,tid,sid,cemail)
            ses.add_all([su])
            ses.commit()           

           

            response={'status':1,"statusMessage":"Booking Successful","QueueNo":QueueNo}
    except Exception as e:
        response = {'status': 0, 'statusMessage': str(e)}
    return jsonify(response)
       

