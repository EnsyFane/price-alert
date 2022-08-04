import os
from serpapi import GoogleSearch


class GoogleSearcher:
    def __get_params(self, query) -> dict:
        return {
            'q': query,
            'location_requested': 'Baia Mare, Maramures County, Romania',
            'location_used': 'Baia Mare,Maramures County,Romania',
            'google_domain': 'google.ro',
            'hl': 'ro',
            'gl': 'ro',
            'api_key': os.environ['SERPAPI_KEY']
        }

    def search(self, query) -> dict:
        params = self.__get_params(query)
        result = GoogleSearch(params)
        results = result.get_dict()
        return results['organic_results']
