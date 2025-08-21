from enum import unique

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Publisher(Base):
    __tablename__= "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__="book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), nullable=False)
    id_publisher = relationship(Publisher, backref="books")

class Shop(Base):
    __tablename__="shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Stock(Base):
    __tablename__="stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = relationship(Book, backref="stocks")
    id_shop = relationship(Shop, backref="stocks")
    count = sq.Column(sq.Integer)

class Sale(Base):
    __tablename__="sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date)
    id_stock = relationship(Stock, backref="sales")
    count = sq.Column(sq.Integer)



def create_tales(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)