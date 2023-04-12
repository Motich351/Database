from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relation

from base_meta import Base

class CheckOperation(Base):
    __tablename__ = 'check_operation'

    id = Column(Integer, primary_key=True)
    payment = Column(Integer, nullable=False)
