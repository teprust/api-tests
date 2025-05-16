import logging

import requests
from requests import Response

from utils.logger_api import log_response

logger = logging.getLogger("test_api")

class StoreClient:
    def __init__(self, url: str):
        self.url = url
        self.requests = requests

    _REGISTER = "/api/register"
    _AUTH = "/api/auth"
    _ADD_USER = "/api/user"

    def register(self, body: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._REGISTER}", json=body)
        log_response(response=res, request_body=body)
        return res

    def auth(self, body: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._AUTH}", json=body)
        log_response(response=res, request_body=body)
        return res

    def add_user(self, body: dict, header: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._ADD_USER}", json=body, headers=header)
        log_response(response=res, request_body=body)
        return res
