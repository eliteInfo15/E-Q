from flask import Flask,request,Blueprint,jsonify

from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')



add_Treatment=Blueprint('add_Treatment',__name__)

from app import app
from treatment import Treatment,eng
from tokenAuthentication import token_required
@add_Treatment.route('/addTreatment',methods=['POST'])
@token_required
def add_tr():
    try:
        if request.method=='POST':
            tname=request.form['tname']
            Session = sessionmaker(bind=eng)
            ses = Session()
            su = Treatment(tname)
            ses.add_all([su])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response = {'status': 0, 'statusMessage': str(e)}
    return jsonify(response)
       

