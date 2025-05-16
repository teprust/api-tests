import logging

import pytest

from api_client.client import StoreClient

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