from repos import ProductRepo
from searchers import EmagSearcher
from scrapers import EmagScraper

repo = ProductRepo()
emag_scraper = EmagScraper()
emag_searcher = EmagSearcher()

# raw_query = input('Search text: ')
raw_query = 'hdd extern 1tb'

products = emag_searcher.search(raw_query)
result = repo.addProduct(products[0])
if result:
    print('Product added successfully!')
else:
    print('Product with hash already exists!')

print(repo.getProductsWithName('Hdd')[0])

repo.getProductById(0)
