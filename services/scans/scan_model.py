from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from services.scans.database import Base
from datetime import datetime

class Scan(Base):
    __tablename__ = 'scans'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    domain: Mapped[str] = mapped_column(String(300), nullable=False)
    organisation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    subdomains: Mapped[str] = mapped_column(Text, nullable=False)
    ip: Mapped[str] = mapped_column(String(50), nullable=False)
    ports: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)
    scan_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False)
    update_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")

class ScanResponse(BaseModel):
    id: int
    domain: str
    organisation_id: int
    subdomains: str
    ip: str
    ports: str
    status: int
    scan_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True

class ScanRequest(BaseModel):
    domain: str
    organisation_id: int
    subdomains: str
    ip: str
    ports: str
    status: int
    scan_date: datetime

    class Config:
        orm_mode = True