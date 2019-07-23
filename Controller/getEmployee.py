from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from employee import Employee,eng
from tokenAuthentication import token_required

get_employee=Blueprint('get_employee',__name__)

@get_employee.route('/getEmployee', methods=['POST'])
@token_required
def get_em():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = ses.query(Employee).all()
        cols = Employee.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.eid
            details[cols[1]] = record.ename
            details[cols[2]] = record.ephone
            details[cols[3]] = record.photo
            details[cols[4]] = record.experience
            details[cols[5]] = record.sid
            details[cols[6]] = record.tid
            detail.append(details)
        print(detail)
        return json.dumps(detail)