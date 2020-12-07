import requests
import allure


class ApiClient:
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def get(self, path="/", params=None, headers=None):
        url = f"{self.host}{path}"
        url_params = ""
        if params:
            url_params = '?' + '&'.join([f"{k}={v}" for k, v in params.items()])

        with allure.step(f'GET request to: {url}{url_params}'):
            return self._s.get(url=url, params=params, headers=headers)
