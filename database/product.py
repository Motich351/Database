from sqlalchemy import Column,Integer,Text, CHAR,ForeignKey
from sqlalchemy.orm import relation, relationship

from .base_meta import Base

class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    address = Column(CHAR)
    income = Column(Integer)
    product_id = Column(ForeignKey('product.id'), nullable=True)
    worker_count_id = Column(Integer)

    #product = relationship('Product')

    def __str__(self):
        return f"Точка {self.id}: {self.adress}; Доход: {self.profit};"

    def __repr__(self):
        return str(self)