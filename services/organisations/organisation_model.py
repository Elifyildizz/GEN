from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from organisations.database import Base
from datetime import datetime, timezone
from typing import Optional

class Organisation(Base):
    __tablename__ = 'organisations'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    organisation: Mapped[str] = mapped_column(String(300), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    updated_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
    created_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")

class OrganisationResponse(BaseModel):
    id: int
    organisation: str
    phone: int
    email: str
    updated_time: datetime
    created_time: datetime

    class Config:
        from_attributes = True

class OrganisationRequest(BaseModel):
    organisation: str
    phone: int
    email: str
    updated_time: datetime
    created_time: datetime

    class Config:
        from_attributes = True
