from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from sqlalchemy import create_engine
from services.organisations.organisation_model import Organisation, OrganisationResponse,OrganisationRequest
from services.organisations.organisation_controller import organisation_controller

router = APIRouter()

@router.get("/getAllOrganisations", response_model=List[OrganisationResponse])
def getAllOrganisations():
    organisations = organisation_controller.getAllOrganisations()
    return organisations

@router.post("/addOrganisation", response_model=OrganisationResponse)
def getAllOrganisations(organisation: OrganisationRequest):
    organisation = organisation_controller.addOrganisation(organisation.dict())
    return organisation

@router.get("/getOrganisationById/{org_id}", response_model=OrganisationResponse)
def getOrganisationById(org_id:int):
    organisation = organisation_controller.getOrganisationById(org_id)
    if not organisation:
        raise HTTPException(status_code=404,detail="Organisation not found")
    return organisation

@router.delete("/deleteOrganisation/{org_id}")
def deleteOrganisation(org_id: int):
    success = organisation_controller.deleteOrganisation(org_id)
    if not success:
        raise HTTPException(status_code=404, detail="Organisation not found")
    return {"message": "Organisation deleted successfully"}
    