from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from booking import Booking,eng
from tokenAuthentication import token_required

get_booking=Blueprint('get_booking',__name__)



@get_booking.route('/getBooking', methods=['POST'])
@token_required
def get_bo():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = ses.query(Booking).all()
        cols = Booking.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.bid
            date1=record.bdate
            d=date1.strftime("%m/%d/%y")
            details[cols[1]] = d
            details[cols[2]] = record.QueueNo
            tim=record.time
            t=tim.strftime("%H:%M:%S")
            details[cols[3]] = t
            details[cols[4]] = record.tid
            details[cols[5]] = record.sid
            details[cols[6]] = record.cemail
            detail.append(details)
        print(detail)
        return jsonify(detail)