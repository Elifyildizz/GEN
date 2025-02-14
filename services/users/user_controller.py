import secrets
from services.users.database import db, Base
from services.users.user_model import Token, User,UserResponse,UserRequest
from hashlib import sha256

class user_controller:
    @staticmethod
    def getAllUsers():
        session = db.get_session()
        users = []
        try:
            users = session.query(User).all()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()

        return users
    
    @staticmethod
    def login(email: str, password: str):
        session = db.get_session()
        res = {"status":"error"}
        try:
            query = session.query(User).filter(User.email==email, User.password==sha256(password.encode('utf-8')).hexdigest())
            result = query.first()
            if result:
                token = secrets.token_hex(30)
                print(token)
                new_token = Token(
                    token=token,
                    user_id=result.id,
                    expired=False
                )
                session.add(new_token)
                session.commit()
                res = {"status":"success","token":token}
            else:
                res = {"status":"user_not_found"}
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
            res = {"status":"error"}
        finally:
            session.close()
        return res

    @staticmethod
    def addUser(user : UserRequest):
        session = db.get_session()
        new_user = User(**user)
        try:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return new_user
    
    @staticmethod
    def getUserById(user_id: int):
        session = db.get_session()
        user = None
        try:
            user = session.query(User).filter(User.id == user_id).first()
        except Exception as e:
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return user
    
    @staticmethod
    def deleteUserById(user_id: int):
        session = db.get_session()
        success = False
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                success = True
        except Exception as e:
            session.rollback()
            print(f"Veritabanı işlemi hatası: {e}")
        finally:
            session.close()
        return success