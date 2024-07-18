from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from sqlalchemy import create_engine
from services.scans.scan_model import Scan, ScanResponse,ScanRequest
from services.scans.scan_controller import scan_controller

router = APIRouter()
    
@router.get("/getAllScans", response_model=List[ScanResponse])
def getAllScans():
    scans = scan_controller.getAllScans()
    return scans

@router.post("/addScan", response_model=ScanResponse)
def getAllScans(scan: ScanRequest):
    scan = scan_controller.addScan(scan.dict())
    return scan

@router.get("/getScanById/{org_id}", response_model=ScanResponse)
def getScanById(org_id:int):
    scan = scan_controller.getScanById(org_id)
    if not scan:
        raise HTTPException(status_code=404,detail="Scan not found")
    return scan

@router.delete("/deleteScan/{org_id}")
def deleteScan(org_id: int):
    success = scan_controller.deleteScan(org_id)
    if not success:
        raise HTTPException(status_code=404, detail="Scan not found")
    return {"message": "Scan deleted successfully"}