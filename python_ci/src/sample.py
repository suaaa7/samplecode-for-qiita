import requests


class Sample:
    def fetch_json(self, url: str) -> dict:
        response = requests.get(url)
        return response.json()
