from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
from sqlalchemy import JSON, create_engine
from services.scans.scan_model import Scan, ScanResponse,ScanRequest, SubfinderRequest, TokenRequest,CollectionRequest
from services.scans.scan_controller import scan_controller
from bson import json_util, ObjectId
import json

router = APIRouter()

@router.post("/getScanCollections")
def getScanCollections(token_request:TokenRequest):
    print(token_request.token)
    scans = scan_controller.getCollections()
    ab = []
    for x in scans:
        print(x)
        ab.append(x)

    
    return {"data":json.loads(json_util.dumps(ab))}

@router.post("/getCollectionsNucleiScan")
def getCollectionsNucleiScan(collection_request:CollectionRequest):
    print(collection_request.token)
    scans = scan_controller.getCollectionsNucleiScan(collection_request)
    ab = []
    for x in scans:
        print(x)
        ab.append(x)

    
    return {"data":json.loads(json_util.dumps(ab))}

###

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

@router.get("/getScanById/{org_id}", response_model=ScanResponse)
def getScanById(org_id: int):
    scan = scan_controller.getScanById(org_id)
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return scan

class SubfinderResponse(BaseModel):
    result: str

@router.post("/subfinder", response_model=SubfinderResponse)
def run_subfinder(request: SubfinderRequest):
    print(f"Received Subfinder request: {request}")
    result = scan_controller.handle_subfinder_request(request)
    return SubfinderResponse(result=result)