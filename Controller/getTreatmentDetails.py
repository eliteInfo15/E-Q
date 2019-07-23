from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from treatmentDetails import TreatmentDetails,eng
from tokenAuthentication import token_required


get_tdetails=Blueprint('get_tdetails',__name__)

@get_tdetails.route('/getTdetails', methods=['POST'])
@token_required
def get_td():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = ses.query(TreatmentDetails).all()
        cols = TreatmentDetails.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.tdid
            details[cols[1]] = record.sid
            details[cols[2]] = record.tid
            details[cols[3]] = record.duration
            details[cols[4]] = record.price
            detail.append(details)
        print(detail)
        return json.dumps(detail)















