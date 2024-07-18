from services.scans.database import db, Base
from services.scans.scan_model import Scan,ScanResponse,ScanRequest
class scan_controller:
    @staticmethod
    def getAllScans():
        session = db.get_session()
        scans = []
        try:
            # Scans tablosundaki tüm kayıtları sorgula
            scans = session.query(Scan).all()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()

        return scans
    
    @staticmethod
    def addScan(scan : ScanRequest):
        session = db.get_session()
        new_scan = Scan(**scan)
        try:
            session.add(new_scan)
            session.commit()
            session.refresh(new_scan)
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return new_scan
    
    @staticmethod
    def getScanById(org_id: int):
        session = db.get_session()
        scan = None
        try:
            scan = session.query(Scan).filter(Scan.id == org_id).first()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return scan

    @staticmethod
    def deleteScan(org_id: int):
        session = db.get_session()
        success = False
        try:
            scan = session.query(Scan).filter(Scan.id == org_id).first()
            if scan:
                session.delete(scan)
                session.commit()
                success = True
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return success