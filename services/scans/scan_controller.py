import paramiko
from services.scans.database import db, Base
from services.scans.scan_model import Scan,ScanResponse,ScanRequest, SubfinderRequest, Scan,CollectionRequest
from fastapi import HTTPException
from services.scans.mongodb_connection import mongodb_connection

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



 ########################################################### mongodb
    @staticmethod
    def getCollections():
        scan = None
        try:
            scan = mongodb_connection.querry(search_querry={},table_name="scan_collections")
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            print("finally")
        
        return scan
    
    @staticmethod
    def getCollectionsNucleiScan(collection_request: CollectionRequest):
        collection_request.collection_name
        scan = None
        try:
            scan = mongodb_connection.querry(search_querry={"collection_name":collection_request.collection_name},table_name="nuclei_scans")
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            print("finally")
        
        return scan


 ###########################################################


    @staticmethod
    def nmap_scan(ip: str) -> str:
        querry = f"nmap -sV -p- --open {ip} -vvv -oX test.xml"
        result = scan_controller.execute_ssh(querry)
        return result

    @staticmethod
    def execute_ssh(querry: str) -> str:
        hostname = '192.168.85.129'
        username = 'kali'
        password = 'kali'

        try:
            print(f"Connecting to {hostname} with username {username}")

            # SSH istemcisi oluştur
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Bağlantı kur
            client.connect(hostname, username=username, password=password)
            print(f"Connected to {hostname}")

            # ifconfig komutunu çalıştır
            stdin, stdout, stderr = client.exec_command(querry)
            ifconfig_output = stdout.read().decode()
            print("output:", ifconfig_output)

            # Hataları kontrol et
            errors = stderr.read().decode()
            if errors:
                print("Errors:", errors)
                raise HTTPException(status_code=500, detail=f"Errors: {errors}")

            # Bağlantıyı kapat
            client.close()
            print("Connection closed")

            return ifconfig_output

        except Exception as e:
            print(f"An error occurred: {e}")
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")