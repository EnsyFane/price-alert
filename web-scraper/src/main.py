from searchers.EmagSearcher import EmagSearcher
from scrapers.EmagScraper import EmagScraper

emag_scraper = EmagScraper()
emag_searcher = EmagSearcher()

# raw_query = input('Search text: ')
raw_query = 'hdd extern 1tb'

products = emag_searcher.search(raw_query)

# product = emagScraper.scrape(
#     'hdd-extern-wd-elements-portable-1tb-2-5-usb-3-0-negru-wdbuzg0010bbk/pd/D2JCXBBBM/?path=hdd-extern-wd-elements-portable-1tb-2-5-usb-3-0-negru-wdbuzg0010bbk/pd/D2JCXBBBM')
