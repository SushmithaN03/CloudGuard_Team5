"""Subscription model."""
from sqlalchemy import Column, Integer, String
from src.core.database import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)

    subscription_id = Column(String, unique=True)
    subscription_name = Column(String)

    tenant_id = Column(String)

    status = Column(String, default="ACTIVE")
