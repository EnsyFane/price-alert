from bs4 import BeautifulSoup
from scrapers import BaseScraper
from models import Product


class EmagScraper(BaseScraper):
    BASE_EMAG_URL = 'https://www.emag.ro/'

    def __init__(self):
        super().__init__(self.BASE_EMAG_URL)

    def scrape(self, product_url) -> Product:
        product_url = self.__shortenUrl(product_url)
        if self.BASE_EMAG_URL not in product_url:
            product_url = self.BASE_EMAG_URL + product_url

        print('Processing: ' + product_url)
        soup = self._getSoupFromUrl(product_url)

        product = self.__processSoup(soup, product_url)
        print(f'Parsed the following product: {product}')

        return product

    def __shortenUrl(self, url: str) -> str:
        if ('?X-Search-Id' in url):
            return url.split('?X-Search-Id')[0]

    def __processSoup(self, soup: BeautifulSoup, product_url: str) -> Product:
        name_soup = soup.find('h1', {'class': 'page-title'})
        price_soup = soup.find('p', {'class': 'product-new-price'})
        image_soup = soup.find(
            'a', {'class': 'product-gallery-image'}).select_one('img')

        if (name_soup is None or price_soup is None or image_soup is None):
            # This means that the product is not in stock.
            return None

        full_name = name_soup.text.strip()
        full_price = price_soup.text.strip()
        price = float(full_price.split(' ')[0].replace(',', '.'))
        currency = full_price.split(' ')[1]
        image = image_soup.get('src').strip()

        return Product(full_name, price, currency, image, product_url)
