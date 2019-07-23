from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base
from salon import Salon
from treatment import Treatment
class Employee(Base):
	__tablename__ = "Employee"
	eid=Column(Integer,primary_key=True)
	ename=Column(String(30))
	ephone=Column(String(30))
	photo=Column(String(30))
	experience=Column(String(30))
	sid=Column(Integer,ForeignKey('Salon.sid'))
	tid=Column(Integer,ForeignKey('Treatment.tid'))
	def __init__(self,eid,ename,ephone,photo,experience,sid,tid):
		self.eid=eid
		self.ename=ename
		self.ephone=ephone
		self.photo=photo
		self.experience=experience
		self.sid=sid
		self.tid=tid
Base.metadata.bind = eng        
Base.metadata.create_all()  