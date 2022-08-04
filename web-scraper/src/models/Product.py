import hashlib


class Product:
    def __init__(self, fullName, price, currency, image_url, link):
        self.fullName = fullName
        self.price = price
        self.currency = currency
        self.image_url = image_url
        self.link = link

        hash_string = self.price + self.currency + self.link
        self.hash = hashlib.sha256(hash_string.encode('utf-8')).hexdigest()
        print(self.hash)

    def __str__(self) -> str:
        return f'{self.fullName} - {self.price} {self.currency}'
