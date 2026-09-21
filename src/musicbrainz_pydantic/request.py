import logging
import time
from collections.abc import Callable
from typing import Any
from urllib.parse import urlencode

import requests

from musicbrainz_pydantic import USER_AGENT, logger as main_logger
from musicbrainz_pydantic.exceptions import MBRequestError


last_request = 0.0


def request(resource: str, id: str = "", logger: logging.Logger = main_logger, **params) -> dict[str, Any]:
    # Some rudimentary param sorting to help with the caching:
    if "inc" in params:
        inc = params.pop("inc")
        if inc:
            if not isinstance(inc, list):
                inc = str(inc).split(" ")
            params["inc"] = " ".join(sorted(inc))

    params["fmt"] = "json"
    params = {k: params[k] for k in sorted(params) if params[k]}
    query = urlencode(params)
    url = f"https://musicbrainz.org/ws/2/{resource}/{id}?{query}"

    response = _request(url, logger=logger)
    if response.status_code >= 400:
        raise MBRequestError(response)

    return response.json()


def _request(
    url: str,
    method: str = "get",
    logger: logging.Logger = main_logger,
    **kwargs,
) -> requests.Response:
    def sleep_if_needed():
        global last_request

        seconds = 1 - time.time() + last_request

        if seconds > 0:
            logger.debug(f"Sleeping for {int(seconds * 1000)} ms to avoid rate limiting...")
            time.sleep(seconds)

        last_request = time.time()

    sleep_if_needed()

    return _retry_request(
        url,
        method=method,
        timeout=10,
        headers={"User-Agent": USER_AGENT},
        on_retry=sleep_if_needed,
        logger=logger,
        **kwargs,
    )


def _retry_request(
    url: str,
    method: str = "get",
    retries: int = 5,
    logger: logging.Logger = main_logger,
    on_retry: Callable[[], None] | None = None,
    **kwargs,
) -> requests.Response:
    retry = 0

    while True:
        logger.info(f"{method.upper()} {url}" + (f" (retry #{retry})" if retry else ""))
        try:
            return requests.request(method, url, **kwargs)
        except Exception as e:
            logger.warning(f"*** {e}")
            if on_retry:
                on_retry()
            retry += 1
            if retry >= retries:
                raise e
