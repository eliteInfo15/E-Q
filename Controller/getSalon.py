from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from salon import Salon,eng
from tokenAuthentication import token_required
get_salon=Blueprint('get_salon',__name__)
@get_salon.route('/getSalon', methods=['POST'])
@token_required
def get_sa():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = ses.query(Salon).all()
        cols = Salon.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.sid
            details[cols[1]] = record.sname
            details[cols[2]] = record.semail
            details[cols[3]] = record.spassword
            details[cols[4]] = record.sphone
            details[cols[5]] = record.saddress
            details[cols[6]] = record.sarea
            detail.append(details)
        print(detail)
        return json.dumps(detail)