from sqlalchemy import Column, Integer, String
from src.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String(100), unique=True)
    email = Column(String(255), unique=True)

    hashed_password = Column(String(255))

    role = Column(String(50))