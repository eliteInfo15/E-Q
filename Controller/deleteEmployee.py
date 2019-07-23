from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from employee import Employee,eng
from tokenAuthentication import token_required
delete_employee=Blueprint('delete_employee',__name__)

@delete_employee.route('/deleteEmployee',methods=['DELETE'])
@token_required
def delemp():
	try:
	    eid = request.form['eid']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    de = ses.query(Employee).filter_by(eid=eid).first()
	    ses.delete(de)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage':str(e)}
	return jsonify(response)
    