from sqlalchemy import Column,Integer,Text, CHAR,ForeignKey
from sqlalchemy.orm import relation

from .base_meta import Base


class Client(Base):
    __tablename__ = 'client'
    __table_args__ = {'extend_existing':True}

    id = Column(Integer, primary_key=True)
    fullname = Column(CHAR)
    phone = Column(Integer, nullable=False)

    def __str__(self):
        return f"Клиент {self.id}: {self.fullname} {self.phone}"

    def __repr__(self):
        return str(self)