from .database import Base

from sqlalchemy import CheckConstraint, Column, Integer, String, Boolean, SmallInteger, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    mobile = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    __table_args__ = (
        CheckConstraint('(email IS NOT NULL OR mobile IS NOT NULL)', name='email_or_mobile_check'),
    )