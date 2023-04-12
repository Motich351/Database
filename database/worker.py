from sqlalchemy import Column,Integer,Text, CHAR,ForeignKey
from sqlalchemy.orm import relation

from .base_meta import Base

class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    fullname = Column(CHAR)
    passport = Column(Integer, nullable=False)
    jobrank = Column(CHAR)
    salary = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)

    def __str__(self):
        return f"Работник {self.id}: {self.fullname}; профессия: {self.jobrank}; {self.phone}"

    def __repr__(self):
        return str(self)