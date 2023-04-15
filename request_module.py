""" REQUESTS """
from requests import Response, get
import configuration

HEADERS: dict = {
    "user-agent": configuration.get_header()
}


def configure_headers(headers: dict = None) -> dict:
    """Configure Headers, default value content user-agent for config.ini"""
    return HEADERS if headers is None else dict(HEADERS, **headers)


def get__(url) -> Response:
    """Get Request"""
    return get(url, headers=HEADERS, timeout=configuration.get_time_out())
