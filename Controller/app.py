from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']='abc123'

from addAdmin import add_admin
from addCustomer import add_Customer
from addBooking import add_Booking
from addTreatment import add_Treatment
from addTreatmentDetails import add_tdetails
from addSalon import add_salon
from addEmployee import add_employee
from doLogin import do_login
from getCustomer import get_cust
from getSalon import get_salon
from getTreatmentDetails import get_tdetails
from getEmployee import get_employee
from getAdmin import get_admin
from getBooking import get_booking
from getTreatment import get_treatment
from updateAdmin import update_admin
from updateBooking import update_booking
from updateEmployee import update_employee
from updateTreatment import update_treatment
from updateTreatmentDetails import update_tdetails
from updateSalon import update_salon
from updateCustomer import update_customer
from deleteAdmin import delete_admin
from deleteCustomer import delete_customer
from deleteSalon import delete_salon
from deleteTreatment import delete_treatment
from deleteTreatmentDetails import delete_tdetails
from deleteEmployee import delete_employee
from deleteBooking import delete_booking


app.register_blueprint(add_admin)
app.register_blueprint(add_Customer)
app.register_blueprint(add_Booking)
app.register_blueprint(add_Treatment)
app.register_blueprint(add_tdetails)
app.register_blueprint(add_salon)
app.register_blueprint(add_employee)
app.register_blueprint(do_login)
app.register_blueprint(get_cust)
app.register_blueprint(get_salon)
app.register_blueprint(get_tdetails)
app.register_blueprint(get_employee)
app.register_blueprint(get_admin)
app.register_blueprint(get_booking)
app.register_blueprint(get_treatment)
app.register_blueprint(update_admin)
app.register_blueprint(update_booking)
app.register_blueprint(update_employee)
app.register_blueprint(update_salon)
app.register_blueprint(update_treatment)
app.register_blueprint(update_tdetails)
app.register_blueprint(update_customer)
app.register_blueprint(delete_admin)
app.register_blueprint(delete_salon)
app.register_blueprint(delete_customer)
app.register_blueprint(delete_tdetails)
app.register_blueprint(delete_treatment)
app.register_blueprint(delete_booking)
app.register_blueprint(delete_employee)



if __name__ == '__main__':
	app.run()