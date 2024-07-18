from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None
        self.SessionLocal = None

    def connect(self):
        try:
            self.engine = create_engine(
                f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            )
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            print("Bağlantı başarılı!")
        except Exception as e:
            print(f"Bağlantı hatası: {e}")

    def get_session(self):
        if not self.SessionLocal:
            raise Exception("Veritabanına bağlanılmamış. Lütfen 'connect' metodunu çağırın.")
        return self.SessionLocal()

# Docker-compose dosyanızdaki MySQL servisinin ağ içindeki IP adresi ve portu
user = "gen"
password = "n!G4l1WjOoIL8HC4"
host = "mysql"  # Docker ağında MySQL konteynerinin ismi
port = "3306"  # MySQL portu, 3307:3306 olarak expose edilmiş
database = "gen"

# Database sınıfını kullanarak bir nesne oluşturun ve bağlanın
db = Database(user, password, host, port, database)
db.connect()

