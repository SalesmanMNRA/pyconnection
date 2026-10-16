"""
Requests utility functions for PYConnection.

Provides helper functions and configuration for the requests integration.
"""

import logging
from typing import Dict, Any, Optional, Union

logger = logging.getLogger(__name__)


def configure_session(
    session: "requests.Session",
    timeout: float = 30.0,
    headers: Optional[Dict[str, str]] = None,
    **kwargs: Any,
) -> None:
    """
    Configure a requests.Session with sensible defaults.

    Args:
        session: requests.Session to configure
        timeout: Default timeout in seconds for all requests
        headers: Default headers to apply to all requests
        **kwargs: Additional session configuration options
    """
    if headers:
        session.headers.update(headers)

    session.timeout = timeout

    # Set default User-Agent if not already set
    if "User-Agent" not in session.headers:
        session.headers.update(
            {
                "User-Agent": (
                    "PYConnection/2.0.0 "
                    "(compatible; soroush-plus-client)"
                )
            }
        )

    logger.debug("Requests session configured with timeout=%s", timeout)


def get(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: Optional[float] = None,
    **kwargs: Any,
) -> "requests.Response":
    """
    Send a GET request with optional default configuration.

    Args:
        url: URL to request
        params: Query parameters
        headers: Request headers
        timeout: Override default timeout
        **kwargs: Additional arguments for requests.get

    Returns:
        requests.Response object
    """
    import requests as _requests

    merged_headers = {**(headers or {}), **kwargs.pop("_headers", {})}
    _timeout = timeout if timeout is not None else kwargs.pop("_timeout", 30.0)

    return _requests.get(
        url, params=params, headers=merged_headers, timeout=_timeout, **kwargs
    )


def post(
    url: str,
    data: Optional[Union[Dict[str, Any], str]] = None,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: Optional[float] = None,
    **kwargs: Any,
) -> "requests.Response":
    """
    Send a POST request with optional default configuration.

    Args:
        url: URL to request
        data: Form data
        json: JSON data to send
        headers: Request headers
        timeout: Override default timeout
        **kwargs: Additional arguments for requests.post

    Returns:
        requests.Response object
    """
    import requests as _requests

    merged_headers = {**(headers or {}), **kwargs.pop("_headers", {})}
    _timeout = timeout if timeout is not None else kwargs.pop("_timeout", 30.0)

    return _requests.post(
        url,
        data=data,
        json=json,
        headers=merged_headers,
        timeout=_timeout,
        **kwargs,
    )


def put(
    url: str,
    data: Optional[Union[Dict[str, Any], str]] = None,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: Optional[float] = None,
    **kwargs: Any,
) -> "requests.Response":
    """
    Send a PUT request.

    Args:
        url: URL to request
        data: Form data
        json: JSON data to send
        headers: Request headers
        timeout: Override default timeout
        **kwargs: Additional arguments for requests.put

    Returns:
        requests.Response object
    """
    import requests as _requests

    merged_headers = {**(headers or {}), **kwargs.pop("_headers", {})}
    _timeout = timeout if timeout is not None else kwargs.pop("_timeout", 30.0)

    return _requests.put(
        url, data=data, json=json, headers=merged_headers, timeout=_timeout, **kwargs
    )


def delete(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    timeout: Optional[float] = None,
    **kwargs: Any,
) -> "requests.Response":
    """
    Send a DELETE request.

    Args:
        url: URL to request
        headers: Request headers
        timeout: Override default timeout
        **kwargs: Additional arguments for requests.delete

    Returns:
        requests.Response object
    """
    import requests as _requests

    merged_headers = {**(headers or {}), **kwargs.pop("_headers", {})}
    _timeout = timeout if timeout is not None else kwargs.pop("_timeout", 30.0)

    return _requests.delete(
        url, headers=merged_headers, timeout=_timeout, **kwargs
    )