from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base
class Login(Base):
	__tablename__ = "Login"
	lid=Column(Integer,primary_key=True)
	email=Column(String(30))
	password=Column(String(100))
	role=Column(String(30))

	
	def __init__(self,email,password,role):
		self.email=email
		self.password=password
		self.role=role
Base.metadata.bind = eng        
Base.metadata.create_all()  