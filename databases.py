from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, info):
	product_object= Product( name=name, price=price, info= info)
	session.add(product_object)
	session.commit()
  
  

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
  session.query(Product).filter_by(id=id).delete()
  session.commit()

def get_product(id):
  pass

delete_product(1)