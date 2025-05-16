import logging

import pytest

from api_client.client import StoreClient
from api_client.models.register import RegisterModel

logger = logging.getLogger("test_api")

def pytest_addoption(parser):
    parser.addoption("--api-url", action="store", default="http://158.160.87.146:5000",
                     help="foo: bar or baz")

@pytest.fixture(scope="session")
def api_client(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start application on address {url}")
    client = StoreClient(url=url)
    return client

@pytest.fixture
def register_user(api_client) -> dict:
    body = RegisterModel().random()
    response_register = api_client.register(body=body)
    assert response_register.status_code == 200
    return body


@pytest.fixture
def auth_user(api_client, register_user):
    # register
    body = RegisterModel().random()
    response_register = api_client.register(body=body)
    assert response_register.status_code == 200, f"Check register request, status code is {response_register.status_code}"

    # auth
    response_auth = api_client.auth(body=body)
    assert response_auth.status_code == 200, "Check auth request"
    assert response_auth.json()['token'] is not None, "Check response"

    # add new user
    token = response_auth.json()['token']
    header = {"Authorization": f"Bearer {token}"}

    return header