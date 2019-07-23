from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from admin import Admin,eng
from login import Login,eng
from tokenAuthentication import token_required
delete_admin=Blueprint('delete_admin',__name__)

@delete_admin.route('/deleteAdmin',methods=['DELETE'])
@token_required
def delad():
	try:
	    aemail=request.form['aemail']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    de = ses.query(Admin).filter_by(aemail=aemail).first()
	    le = ses.query(Login).filter_by(email=aemail).first()

	    ses.delete(de)
	    ses.delete(de)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage':str(e)}
	return jsonify(response)
    