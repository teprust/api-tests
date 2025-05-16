import logging

import requests
from requests import Response

logger = logging.getLogger("test_api")

class StoreClient:
    def __init__(self, url: str):
        self.url = url
        self.requests = requests

    _REGISTER = "/api/register"

    def register(self, body: dict) -> Response:
        logger.info(f"Register new user with body {body}")
        res = self.requests.post(url=f"{self.url}{self._REGISTER}", json=body)
        logger.info(f"Status code is {res.status_code}, response body is {res.json()}")
        return res
