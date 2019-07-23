from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from treatment import Treatment,eng
from tokenAuthentication import token_required

delete_treatment=Blueprint('delete_treatment',__name__)

@delete_treatment.route('/deleteTreatment',methods=['DELETE'])
@token_required
def deltr():
	try:
	    tid = request.form['tid']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    tr = ses.query(Treatment).filter_by(tid=tid).first()
	    ses.delete(tr)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage': str(e)}
	return jsonify(response)  