from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')

Base = declarative_base()
 
class Admin(Base):
	__tablename__ = "Admin"
	aname=Column(String(30),primary_key=True)
	aemail=Column(String(30))
	apassword=Column(String(100))
	apriority=Column(String(30))
	def __init__(self,aname,aemail,apassword,apriority):
		self.aname=aname
		self.aemail=aemail
		self.apassword=apassword
		self.apriority=apriority
Base.metadata.bind = eng        
Base.metadata.create_all()  