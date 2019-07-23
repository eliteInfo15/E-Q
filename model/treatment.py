from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base
class Treatment(Base):
	__tablename__ = "Treatment"
	tid=Column(Integer,primary_key=True)
	tname=Column(String(30))
	bookings=relationship('Booking')
	details=relationship('TreatmentDetails')
	emp=relationship('Employee')
	
	def __init__(self,tname):
		self.tname=tname
Base.metadata.bind = eng        
Base.metadata.create_all()  