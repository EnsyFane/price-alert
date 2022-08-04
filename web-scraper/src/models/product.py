import hashlib
from sqlalchemy import Boolean, Column, Float, Integer, String, Table, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product:
    def __init__(self, fullName: str, price: float, currency: str, image_url: str, link: str, hash: str = None):
        self.fullName = fullName
        self.price = price
        self.currency = currency
        self.image_url = image_url
        self.link = link

        if hash is None:
            hash_string = str(self.price) + self.currency + self.link
            self.hash = hashlib.sha256(hash_string.encode('utf-8')).hexdigest()

    def __str__(self) -> str:
        return f'{self.fullName} - {self.price} {self.currency}'


class DbProduct(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    fullName = Column(String)
    price = Column(Float)
    currency = Column(String)
    image_url = Column(String)
    link = Column(String)
    hash = Column(String)
    tracked = Column(Boolean)

    __table_args__ = (UniqueConstraint('hash', name='_hash_uc'),)
