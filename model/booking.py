from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_ ,Date, DateTime
from sqlalchemy.orm import relationship
eng = create_engine('mysql://root:root@localhost/project')
from admin import Base
from treatment import Treatment
from salon import Salon
from customer import Customer
class Booking(Base):
   __tablename__ = "Booking"
   bid =Column(Integer, primary_key = True)
   bdate=Column(Date)
   QueueNo=Column(Integer)
   
   time=Column(DateTime)
   tid=Column(Integer,ForeignKey('Treatment.tid'))
   sid=Column(Integer,ForeignKey('Salon.sid'))
   cemail=Column(String(200),ForeignKey('Customer.cemail'))
  
   def __init__(self,bdate,QueueNo,time,tid,sid,cemail):
       self.date1=date1
       self.QueueNo=QueueNo
       self.time=time
       self.tid=tid
       self.sid=sid
       self.cemail=cemail
Base.metadata.bind = eng        
Base.metadata.create_all()  