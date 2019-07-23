from flask import Flask,request,Blueprint,jsonify
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../model')



add_employee=Blueprint('add_employee',__name__)
from app import app
from tokenAuthentication import token_required
from employee import Employee,eng
@add_employee.route('/addEmployee',methods=['POST'])
@token_required
def add_emp():
    try:
        if request.method=='POST':
            ename=request.form['ename']
            ephone = request.form['ephone']
            photo = request.form['photo']
            experience = request.form['experience']
            sid = request.form['sid']
            tid = request.form['tid']
            Session = sessionmaker(bind=eng)
            ses = Session()

            su = Employee(ename, ephone, photo, experience,sid,tid)
            ses.add_all([su])
            ses.commit()
            response={'status':1,"statusMessage":"Data Inserted"}
    except Exception as e:
        response={'status':0,"statusMessage": str(e)}
    return jsonify(response)