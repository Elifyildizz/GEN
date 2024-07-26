from services.organisations.database import db, Base
from services.organisations.organisation_model import Organisation, Token , OrganisationWithTokenRequest
class organisation_controller:

    @staticmethod
    def getAllOrganisations(token: str):
        session = db.get_session()
        organisations = []
        try:
            valid_token = session.query(Token).filter(Token.token == token, Token.expired == False).first()
            
            if valid_token:
                organisations = session.query(Organisation).all()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return organisations

    @staticmethod
    def addOrganisation(organisation: dict,token:str):
        res = {
            "status":"error"
        }
        session = db.get_session()
        new_organisation = Organisation(**organisation)
        try:
            valid_token = session.query(Token).filter(Token.token == token, Token.expired == False).first()
            
            if valid_token:
                session.add(new_organisation)
                session.commit()
                session.refresh(new_organisation)
                res = {
                    "status":"success"
                }
            else:
                res = {
                    "status":"token_not_found"
                }

            
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return res

    @staticmethod
    def getOrganisationById(org_id: int):
        session = db.get_session()
        organisation = None
        try:
            organisation = session.query(Organisation).filter(Organisation.id == org_id).first()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return organisation

    @staticmethod
    def deleteOrganisation(org_id: int):
        session = db.get_session()
        success = False
        try:
            organisation = session.query(Organisation).filter(Organisation.id == org_id).first()
            if organisation:
                session.delete(organisation)
                session.commit()
                success = True
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return success