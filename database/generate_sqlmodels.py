# coding: utf-8
from sqlalchemy import CHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CheckOperation(Base):
    __tablename__ = 'check_operation'

    id = Column(Integer, primary_key=True)
    payment = Column(Integer, nullable=False)


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    fullname = Column(CHAR)
    phone = Column(Integer, nullable=False)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR)
    price = Column(Integer, nullable=False)
    numb = Column(Integer, nullable=False)


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    address = Column(CHAR)
    income = Column(Integer, nullable=False)
    products = Column(CHAR)


class Storage(Base):
    __tablename__ = 'storage'

    id = Column(Integer, primary_key=True)
    numofgoods = Column(Integer)
    products = Column(CHAR)


class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    fullname = Column(CHAR)
    passport = Column(Integer, nullable=False)
    jobrank = Column(CHAR)
    salary = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    clientid = Column(ForeignKey('client.id'), nullable=False)
    paymentmethod = Column(CHAR)

    client = relationship('Client')


class Provisioner(Base):
    __tablename__ = 'provisioner'

    id = Column(Integer, primary_key=True)
    storageid = Column(ForeignKey('storage.id'), nullable=False)
    companyname = Column(CHAR)
    address = Column(CHAR)
    phone = Column(Integer, nullable=False)

    storage = relationship('Storage')
