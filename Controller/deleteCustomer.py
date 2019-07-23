from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from customer import Customer,eng
from login import Login
from tokenAuthentication import token_required
delete_customer=Blueprint('delete_customer',__name__)

@delete_customer.route('/deleteCustomer',methods=['DELETE'])
@token_required
def delcus():
	try:
	    cemail = request.form['cemail']
	    Session = sessionmaker(bind=eng)
	    ses = Session()
	    de = ses.query(Customer).filter_by(cemail=cemail).first()
	    le = ses.query(Login).filter_by(email=cemail).first()
	    ses.delete(de)
	    ses.delete(le)
	    ses.commit()
	    response = {'status': 1, 'statusMessage': "Data Deleted Successfully"}
	except Exception as e:
		response = {'status': 0, 'statusMessage':str(e)}
	return jsonify(response)
    