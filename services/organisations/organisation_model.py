from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from services.organisations.database import Base
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

class OrganisationWithTokenRequest(BaseModel):
    organisation: str
    token: str
    phone: int
    email: str
    #updated_time: datetime
    #created_time: datetime

    class Config:
        from_attributes = True

class Token(Base):
    __tablename__ = 'tokens'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    token: Mapped[str] = mapped_column(String(500), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    expired: Mapped[bool] = mapped_column(Boolean, nullable=False) 
    created_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")
    updated_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
   

class TokenRequest(BaseModel):
    token: Optional[str] = None
    
    class Config:
        from_attributes = True