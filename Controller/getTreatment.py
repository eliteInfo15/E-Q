from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from treatment import Treatment,eng
from tokenAuthentication import token_required


get_treatment=Blueprint('get_treatment',__name__)

@get_treatment.route('/getTreatment', methods=['POST'])
@token_required
def get_tr():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = Treatment.query.all()
        cols = Treatment.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.tid
            details[cols[1]] = record.tname
            detail.append(details)
        print(detail)
        return json.dumps(detail)