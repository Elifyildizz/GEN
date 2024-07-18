from services.organisations.database import db, Base
from services.organisations.organisation_model import Organisation,OrganisationResponse,OrganisationRequest
class organisation_controller:

    @staticmethod
    def getAllOrganisations():
        session = db.get_session()
        organisations = []
        try:
            organisations = session.query(Organisation).all()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return organisations

    @staticmethod
    def addOrganisation(organisation: dict):
        session = db.get_session()
        new_organisation = Organisation(**organisation)
        try:
            session.add(new_organisation)
            session.commit()
            session.refresh(new_organisation)
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return new_organisation

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