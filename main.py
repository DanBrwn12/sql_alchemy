import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from password import password, login
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from urllib.parse import quote_plus



DSN = f"postgresql://{login}:{quote_plus(password)}@localhost:5432/postgres"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open("tests_data.json", 'r') as tests:
    data = json.load(tests)

for record in data:
    model = {
        "publisher": Publisher,
        "shop": Shop,
        "book": Book,
        "stock": Stock,
        "sale": Sale,
    }[record.get("model")]
    session.add(model(id=record.get("pk"), **record.get("fields")))
session.commit()




def input_publisher():
    publisher = input("Введите имя или идентификатор издателя: ")
    if publisher.isdigit():
        pub = session.query(Publisher).filter(Publisher.id == int(publisher)).first()
    else:
        pub = session.query(Publisher).filter(Publisher.name == publisher).first()

    if pub is None:
        print("Такого издателя не существует")
        return
    for book in pub.books:
        for stock in book.stocks:
            for sale in stock.sales:
                print(f"{book.title} | {stock.shop.name} | {sale.count} | {sale.date_sale}")


input_publisher()

