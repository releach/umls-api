import requests

class API:
    BASE_URL = 'https://uts-ws.nlm.nih.gov/rest'

    def __init__(self, api_key, version, **kwargs):
        self._api_key = api_key
        self._version = version
        self.params = {'apiKey': self._api_key, **kwargs}

    def get_cui(self, cui):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}'
        return self._get(url=url, params=self.params)

    def get_tui(self, tui):
        url = (f'{self.BASE_URL}/semantic-network/{self._version}/TUI/{tui}')
        return self._get(url=url, params=self.params)

    def get_definitions(self, cui, **kwargs):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}/definitions'
        params = {**kwargs, **self.params}
        return self._get(url=url, params=params)

    def get_codes(self, code, source, **kwargs):
        url = f'{self.BASE_URL}/content/{self._version}/source/{source}/{code}'
        params = {**kwargs, **self.params}
        return self._get(url=url, params=params)

    def get_cui_relations(self, cui, **kwargs):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}/relations'
        params = {**kwargs, **self.params}
        return self._get(url=url, params=params)

    def get_cui_atoms(self, cui, **kwargs):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}/atoms'
        params = {**kwargs, **self.params}
        return self._get(url=url, params=params)

    def _get(self, url, params):
        resp = requests.get(url, params=params)
        return resp.json()

    def list_cui_names(self, resp):
        for value in resp['result']:
            print(value['name'])
