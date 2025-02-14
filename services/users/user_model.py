from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from services.users.database import Base
from datetime import datetime, timezone
from typing import Optional

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(256), nullable=False)
    updated_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
    created_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")
    status: Mapped[int] = mapped_column(Integer, nullable=False)
    auth: Mapped[int] = mapped_column(Integer, nullable=False)

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

class UserResponse(BaseModel):
    id: int
    username: str
    password: str
    email: str
    updated_date: datetime
    created_date: datetime
    status: int
    auth: int

    class Config:
        from_attributes = True

class UserRequest(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    updated_date: Optional[datetime] = None
    created_date: Optional[datetime] = None
    status: Optional[int] = None
    auth: Optional[int] = None

    class Config:
        from_attributes = True
