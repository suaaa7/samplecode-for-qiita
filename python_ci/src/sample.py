import requests


class Sample:
    def fetch_json(self, url: str) -> dict:
        response = self._get_response(url)
        return response.json()

    def _get_response(self, url: str) -> requests.models.Response:
        return requests.get(url)
