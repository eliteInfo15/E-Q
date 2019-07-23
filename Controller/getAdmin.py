from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from datetime import datetime
from admin import Admin,eng
from tokenAuthentication import token_required

get_admin=Blueprint('get_admin',__name__)
@get_admin.route('/getAdmin', methods=['POST'])
@token_required
def get_ad():
    if request.method == 'POST':
        Session = sessionmaker(bind=eng)
        ses = Session()
        data = ses.query(Admin).all()
        cols = Admin.__table__.columns.keys()
        detail = []
        print(data)

        for record in data:
            details = {}
            details[cols[0]] = record.aname
            details[cols[1]] = record.aemail
            details[cols[2]] = record.apassword
            details[cols[3]] = record.apriority
            detail.append(details)
        print(detail)
        return json.dumps(detail)