from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ExamServer.modelFiles import db

# model contains SQLAlchemy classes that describe database

# 05% Create a model for cars
class Cars(db.Model):
    __tablename__ = 'cars'

    license = Column(String, primary_key=True)
    model = Column(String)
    price = Column(Integer)
    producer = Column(String)

    # 05% Add a relation between cars and customers so that a car can be assigned to a customer
    customer_number = Column(String, ForeignKey('customers.customerNumber'), nullable=True)
    customer = relationship('Customers', back_populates='cars')


# 05% Create a model for customers
class Customers(db.Model):
    __tablename__ = 'customers'

    customerNumber = Column(String, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)

    # 05% Add a relation between cars and customers so that a car can be assigned to a customer
    cars = relationship('Cars', back_populates='customer')
