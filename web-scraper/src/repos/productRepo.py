from importlib import resources
from sqlalchemy import Integer, create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Product, DbProduct, Base


class ProductRepo:
    def __init__(self):
        with resources.path(
            "data", "price-notifier.db"
        ) as sqlite_filepath:
            engine = create_engine(f"sqlite:///{sqlite_filepath}")
        Base.metadata.create_all(engine)

        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

    def getProductsWithName(self, name: str) -> list[Product]:
        db_products = self.session.query(DbProduct).filter(
            func.lower(DbProduct.fullName).contains(name.lower())).all()

        return [self.__dbToProduct(db_prod) for db_prod in db_products]

    def getProductByHash(self, hash: str) -> Product | None:
        db_prod = self.session.query(DbProduct).filter(
            DbProduct.hash == hash).first()

        if db_prod is None:
            return None

        return self.__dbToProduct(db_prod)

    def getProductById(self, id: Integer) -> Product | None:
        db_prod = self.session.query(DbProduct).filter(
            DbProduct.id == id).first()

        if db_prod is None:
            return None

        return self.__dbToProduct(db_prod)

    def addProduct(self, product: Product) -> bool:
        existing_prod = self.getProductByHash(product.hash)
        if (existing_prod is not None):
            return False

        db_product = self.__productToDb(product)

        self.session.add(db_product)
        self.session.commit()
        return True

    def __productToDb(self, product: Product) -> DbProduct:
        db_product = DbProduct()
        db_product.fullName = product.fullName
        db_product.price = product.price
        db_product.currency = product.currency
        db_product.image_url = product.image_url
        db_product.link = product.link
        db_product.hash = product.hash
        db_product.tracked = False
        return db_product

    def __dbToProduct(self, db_product: DbProduct) -> Product:
        return Product(db_product.fullName, db_product.price, db_product.currency, db_product.image_url, db_product.link, db_product.hash)
