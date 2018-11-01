from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


# Write your classes here :
class Product(Base):
    __tablename__='table'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    price=Column(Integer)
    info=Column(String)
    pass
