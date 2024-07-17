from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from users.database import Base
from datetime import datetime, timezone

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
