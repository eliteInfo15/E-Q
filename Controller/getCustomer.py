from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from customer import Customer,eng
from tokenAuthentication import token_required

get_cust=Blueprint('get_cust',__name__)
@get_cust.route('/getCustomer',methods=['POST'])
@token_required
def get():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = ses.query(Customer).all()
        cols = Customer.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.cname
            details[cols[1]] = record.cpassword
            details[cols[2]] = record.cemail
            details[cols[3]] = record.locality
            details[cols[4]] = record.state
            details[cols[5]] = record.gender
            details[cols[6]] = record.cphone
            detail.append(details)
        print(detail)
        return jsonify(detail)