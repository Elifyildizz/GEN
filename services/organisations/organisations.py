from fastapi import APIRouter, HTTPException
from services.organisations.organisation_model import  OrganisationResponse, OrganisationWithTokenRequest, TokenRequest
from services.organisations.organisation_controller import organisation_controller

router = APIRouter()

@router.post("/getAllOrganisations")
def getAllOrganisations(token: TokenRequest):
    organisations = organisation_controller.getAllOrganisations(token=token.token)
    return organisations

@router.post("/addOrganisation")
def getAllOrganisations(organisation: OrganisationWithTokenRequest):
    new_organisation = {
        "organisation":organisation.organisation,
        "phone":organisation.phone,
        "email":organisation.email
    }
    organisation = organisation_controller.addOrganisation(organisation=new_organisation,token=organisation.token)
    return organisation

### buradan sonrası kontrol edilmedi henüz



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
    