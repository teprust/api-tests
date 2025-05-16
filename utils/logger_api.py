import logging

from requests import Response

logger = logging.getLogger("test_api")

def log_response(response: Response, request_body: dict = None):
    method = response.request.method
    url = response.url
    status_code = response.status_code

    logger.info(f"HTTP {method}, request to URL {url}")

    if request_body is not None:
        logger.info(f"Request body: {request_body}")

    logger.info(f"Status code is {status_code}")

    try:
        logger.info(f"Response body: {response.json()}")
    except ValueError:
        logger.info(f"Response isn't JSON, {response.text}")