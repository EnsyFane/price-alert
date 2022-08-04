from bs4 import BeautifulSoup
from models.Product import Product
from scrapers.EmagScraper import EmagScraper
from urllib.parse import quote

import requests


class EmagSearcher:
    BASE_SEARCH_URL = 'https://www.emag.ro/search/'
    SEARCH_URL_END = '?ref=effective_search'
    DEFAULT_LIST_ITEMS = 1

    def search(self, query) -> list[Product]:
        sanitized_query = quote(query)
        search_url = self.BASE_SEARCH_URL + sanitized_query + self.SEARCH_URL_END

        page = requests.get(search_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        cards = soup.select("div[class='card-v2']")

        emagScraper = EmagScraper()
        products: list[Product] = []

        products_in_list = 0
        for tag in cards:
            info = tag.find(
                'div', {'class': 'card-v2-info'}).find('a').get('href')
            product = emagScraper.scrape(info)
            if product is not None:
                products.append(product)
                products_in_list += 1

            if products_in_list >= self.DEFAULT_LIST_ITEMS:
                break

        return products
