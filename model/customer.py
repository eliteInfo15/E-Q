from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base
class Customer(Base):
   __tablename__ = "Customer"
   cname = Column(String(100))
   cpassword =Column(String(100))
   cemail = Column(String(200),primary_key=True)
   locality = Column(String(200))
   state= Column(String(10))
   gender=Column(String(10))
   age=Column(Integer)
   cphone=Column(String(10))
   bookings=relationship('Booking')
 
   def __init__(self,cname, cpassword, cemail, locality, state, gender,age,cphone):
       self.cname = cname
       self.cemail = cemail
       self.cpassword = cpassword
       self.locality = locality
       self.state = state
       self.gender = gender
       self.age = age
       self.cphone = cphone
Base.metadata.bind = eng        
Base.metadata.create_all()  