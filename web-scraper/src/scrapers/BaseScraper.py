from bs4 import BeautifulSoup
from models.Product import Product
import requests


class BaseScraper:
    def __init__(self, baseUrl):
        self.base_url = baseUrl

    def scrape(self, productId) -> Product:
        pass

    def _getSoupFromUrl(self, url) -> BeautifulSoup:
        page = requests.get(url)
        if (page.status_code != 200):
            raise Exception('Could not get page')

        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def _getSoup(self, product_url) -> BeautifulSoup:
        if (self.base_url not in product_url):
            product_url = self.base_url + product_url

        return self._getSoupFromUrl(product_url)
