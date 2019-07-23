from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from booking import Booking,eng
from tokenAuthentication import token_required

delete_booking=Blueprint('delete_booking',__name__)

@delete_booking.route('/deleteBooking',methods=['DELETE'])
@token_required
def delbo():
	try:
	    bid = request.form['bid']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    be = ses.query(Booking).filter_by(aid=aid).first()
	    ses.delete(be)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage': str(e)}
	return jsonify(response)  