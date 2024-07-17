import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from users.user_model import User, Base

# DATABASE_URL'yi ortam değişkenlerinden alıyoruz
DATABASE_URL = f"mysql+pymysql://gen:n!G4l1WjOoIL8HC4@{os.environ.get('MYSQL_HOST', '127.0.0.1')}:3306/gen"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    session = SessionLocal()
    try:
        # Tabloları oluştur
        Base.metadata.create_all(bind=engine)

        # Başlangıç kullanıcıları
        initial_users = [
            User(username="user1", password="password1", email="user1@example.com", status=1, auth=1),
            User(username="user2", password="password2", email="user2@example.com", status=1, auth=1)
        ]

        # Kullanıcıları ekle
        session.add_all(initial_users)
        session.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    init_db()
