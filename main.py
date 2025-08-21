import sqlalchemy
from sqlalchemy.orm import sessionmaker
from password import password
from models import create_tales, Publisher, Shop, Book, Stock, Sale



DSN = f"postgresql://postgres:{password}@localhost:5432/sql_alchemy"
engine = sqlalchemy.create_engine(DSN)
create_tales(engine)
Session = sessionmaker(engine)
session = Session()


