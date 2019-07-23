from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from treatment import Treatment,eng

from tokenAuthentication import token_required
update_treatment=Blueprint('update_treatment',__name__)

@update_treatment.route('/updateTreatment',methods=['PUT'])
@token_required
def upt():
    try:
        tid=request.form['tid']
        tname=request.form['tname']
        Session = sessionmaker(bind=eng)
        ses = Session() 

        treatment = ses.query(Treatment).filter_by(tid=tid).update(dict(tname= tname))
        ses.commit()
        response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)