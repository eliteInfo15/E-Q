from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base

class Salon(Base):
	__tablename__ = "Salon"
	sid=Column(Integer,primary_key=True)
	sname=Column(String(30))
	semail=Column(String(30))
	spassword=Column(String(100))
	sphone=Column(String(30))
	saddress=Column(String(30))
	sarea=Column(String(30))

	bookings=relationship('Booking')
	
	emp=relationship('Employee')
	details=relationship('TreatmentDetails')
	def __init__(self,sname,semail,spassword,sphone,saddress,sarea):
		self.sname=sname
		self.semail=semail
		self.spassword=spassword
		self.sphone=sphone
		self.saddress=saddress
		self.sarea=sarea
Base.metadata.bind = eng        
Base.metadata.create_all()  