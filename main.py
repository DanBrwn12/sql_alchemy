from itertools import count

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from password import password, login
from models import create_tales, Publisher, Shop, Book, Stock, Sale
from urllib.parse import quote_plus



DSN = f"postgresql://{login}:{quote_plus(password)}@localhost:5432/postgres"
engine = sqlalchemy.create_engine(DSN)
create_tales(engine)
Session = sessionmaker(bind=engine)
session = Session()

def input_publisher():
    publisher = input("Введите имя или идентификатор издателя: ")
    if publisher.isdigit():
        pub = session.query(Publisher).filter(Publisher.id == int(publisher)).first()
    else:
        pub = session.query(Publisher).filter(Publisher.name == str(publisher)).first()

    if pub is None:
        print("Такого издателя не существует")
        return
    for book in pub.books:
        for stock in book.stocks:
            for sale in stock.sales:
                print(f"{book.title} | {stock.shop.name} | {sale.count} | {sale.date_sale}")

pub_1 = Publisher(name="Пушкин")
pub_2 = Publisher(name="Достоевский")

book_1 = Book(title="Капитанская дочка", publisher=pub_1)
book_2 = Book(title="Руслан и Людмила", publisher=pub_1)

book_3 = Book(title="Евгений Онегин", publisher=pub_2)

shop_1 = Shop(name="Буквоед")
shop_2 = Shop(name="Книжный дом")
shop_3 = Shop(name="Графит")

stock_b1_1 = Stock(book=book_1, shop=shop_1, count=600)
stock_b1_2 = Stock(book=book_1, shop=shop_2, count=700)
stock_b1_3 = Stock(book=book_1, shop=shop_3, count=800)

stock_b2_1 = Stock(book=book_2, shop=shop_1, count=600)
stock_b2_2 = Stock(book=book_2, shop=shop_2, count=500)
stock_b2_3 = Stock(book=book_2, shop=shop_3, count=400)

stock_b3_1 = Stock(book=book_3, shop=shop_1, count=900)
stock_b3_2 = Stock(book=book_3, shop=shop_2, count=1000)
stock_b3_3 = Stock(book=book_3, shop=shop_3, count=100)

sale_1 = Sale(stock=stock_b1_1, count= 5, price=100, date_sale="2025-11-11")
sale_2 = Sale(stock=stock_b1_2, count= 10, price=200, date_sale="2025-11-11")
sale_3 = Sale(stock=stock_b1_3, count= 15, price=300, date_sale="2025-11-11")

sale_4 = Sale(stock=stock_b2_1, count= 20, price=400, date_sale="2025-11-11")
sale_5= Sale(stock=stock_b2_2, count= 25, price=500, date_sale="2025-11-11")
sale_6 = Sale(stock=stock_b2_3, count= 30, price=600, date_sale="2025-11-11")

sale_7 = Sale(stock=stock_b3_1, count= 35, price=700, date_sale="2025-11-11")
sale_8 = Sale(stock=stock_b3_2, count= 40, price=800, date_sale="2025-11-11")
sale_9 = Sale(stock=stock_b3_3, count= 45, price=900, date_sale="2025-11-11")

session.add_all([pub_1, pub_2])
session.commit()

input_publisher()

