import requests

class API:
    BASE_URL = 'https://uts-ws.nlm.nih.gov/rest'

    def __init__(self, *, api_key, version='current'):
        self._api_key = api_key
        self._version = version

    def get_cui(self, cui):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}'
        return self._get(url=url)

    def get_tui(self, tui):
        url = (f'{self.BASE_URL}/semantic-network/{self._version}/TUI/{tui}')
        return self._get(url=url)

    def get_definition(self, cui):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}/definitions'
        return self._get(url=url)

    def _get(self, url):
        resp = requests.get(url, params={'apiKey': self._api_key})
        
        return resp.json()
