import os
import sys
from sqlalchemy import Column, ForeignKey, Integer,Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'

	id = Column(Integer,primary_key=True)
	name = Column(String(250),nullable=False)
	address = Column(String(250))
	city = Column(String(100))
	state = Column(String(50))
	zipCode = Column(String(10))
	website = Column(String)


class Puppy(Base):
	__tablename__ = 'puppy'

	id = Column(Integer,primary_key=True)
	name = Column(String(250),nullable=False)
	gender Column(String(6), nullable=False)
	dateOfBirth = Column(Date)
	picture = Column(String)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	weight =Column(Numeric)
	
engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)

