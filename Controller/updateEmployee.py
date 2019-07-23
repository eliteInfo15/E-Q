from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')
from employee import Employee,eng

from tokenAuthentication import token_required
update_employee=Blueprint('update_employee',__name__)

@update_employee.route('/updateEmployee',methods=['PUT'])
@token_required
def upe():
    try:
        eid=request.form['eid']
        ename=request.form['ename']
        ephone = request.form['ephone']
        photo = request.form['photo']
        experience = request.form['experience']
        sid = request.form['sid']
        tid = request.form['tid']
        Session = sessionmaker(bind=eng)
        ses = Session() 

        admin = ses.query(Employee).filter_by(eid=eid).update(dict(ename= ename, ephone=ephone, photo= photo,experience=experience, sid=sid,tid=tid))
        ses.commit()
        response={'status':1,'statusMessage':"Data Updated Successfully"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)