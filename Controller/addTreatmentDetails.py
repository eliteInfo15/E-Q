from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')



add_tdetails=Blueprint('add_tdetails',__name__)

from app import app
from tokenAuthentication import token_required
from treatmentDetails import TreatmentDetails,eng
@add_tdetails.route('/addTDetails',methods=['POST'])
@token_required
def add_tdet():
    try:
        if request.method=='POST':
            sid=request.form['sid']
            tid = request.form['tid']
            duration = request.form['duration']
            price = request.form['price']
            Session = sessionmaker(bind=eng)
            ses = Session()
            su = TreatmentDetails(sid,tid,duration,price)
            ses.add_all([su])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)