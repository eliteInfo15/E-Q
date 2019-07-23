from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base
from salon import Salon
from treatment import Treatment
class TreatmentDetails(Base):
	__tablename__ = "TreatmentDetails"
	tdid=Column(Integer,primary_key=True)
	sid=Column(Integer,ForeignKey('Salon.sid'))
	tid=Column(Integer,ForeignKey('Treatment.tid'))
	duration=Column(String(30))
	price=Column(Integer)
	def __init__(self,duration,price):
		self.duration=duration
		self.price=price
Base.metadata.bind = eng        
Base.metadata.create_all()  