from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

Base=declarative_base()

class Todo_base(Base):
    __tablename__='falcon_api'
    id = Column(Integer,primary_key=True)
    active = Column(Boolean,default=True)
    status = Column(Boolean,default=True)
    text = Column(String(100))
    date_added=Column(String(100))
    
    