from sqlalchemy import Column,Integer,Text, CHAR,ForeignKey
from sqlalchemy.orm import relation, relationship

from .base_meta import Base

class Shop(Base):
    __tablename__ = 'shop'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    address = Column(CHAR)
    income = Column(Integer)
    product = Column(CHAR)
    #workers = relationship("Worker", back_populates="shop")

    def __str__(self):
        return f"Точка {self.id}: {self.adress}; Доход: {self.profit};"

    def __repr__(self):
        return str(self)