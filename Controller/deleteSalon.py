from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from salon import Salon,eng
from tokenAuthentication import token_required

delete_salon=Blueprint('delete_salon',__name__)

@delete_salon.route('/deleteSalon',methods=['DELETE'])
@token_required
def delsa():
	try:
	    sid = request.form['sid']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    sa = ses.query(Salon).filter_by(sid=sid).first()
	    ses.delete(sa)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage': str(e)}
	return jsonify(response)  