from sqlalchemy import Column,Integer,Text, CHAR,ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base

class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    clientid = Column(ForeignKey('client.id'), nullable=False)
    paymentmethod = Column(CHAR)

    client = relationship('Client')