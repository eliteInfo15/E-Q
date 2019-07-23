from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from treatmentDetails import TreatmentDetails,eng

from tokenAuthentication import token_required
update_tdetails=Blueprint('update_tdetails',__name__)

@update_tdetails.route('/updateTreatmentDetails',methods=['PUT'])
@token_required
def uptd():
    try:
        tdid=request.form['tdid']
        sid=request.form['sid']
        tid = request.form['tid']
        duration = request.form['duration']
        price = request.form['price']
        Session = sessionmaker(bind=eng)
        ses = Session() 

        tdetails = ses.query(TreatmentDetails).filter_by(tdid=tdid).update(dict(sid= sid,tid=tid,duration=duration,price=price))
        ses.commit()
        response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)