from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from treatmentDetails import TreatmentDetails,eng
from tokenAuthentication import token_required
delete_tdetails=Blueprint('delete_tdetails',__name__)

@delete_tdetails.route('/deleteTreatmentDetails',methods=['DELETE'])
@token_required
def deltde():
	try:
	    tdid = request.form['tdid']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    de = ses.query(TreatmentDetails).filter_by(tdid=tdid).first()
	    ses.delete(de)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage':str(e)}
	return jsonify(response)
    