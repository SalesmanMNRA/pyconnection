"""
Core client for PYConnection SDK.

Combines spluslib (Soroush Plus userbot) and requests (HTTP client)
into a unified interface.
"""

import logging
from typing import Optional, Dict, Any, Union, List, Callable

import requests

from . import soroush_utils
from . import requests_utils

logger = logging.getLogger(__name__)


class PYConnectionClient:
    """
    Unified client that combines Soroush Plus connectivity (via spluslib)
    and HTTP request capabilities (via requests).

    Example usage::

        from pyconnection import PYConnectionClient

        client = PYConnectionClient(
            api_id=12345,
            api_hash="your_api_hash",
            phone_number="+989123456789",
        )

        # Make HTTP requests
        response = client.http_get("https://httpbin.org/get")

        # Soroush Plus operations
        await client.send_message("username", "Hello!")
    """

    def __init__(
        self,
        api_id: Optional[int] = None,
        api_hash: Optional[str] = None,
        phone_number: Optional[str] = None,
        session_name: str = "pyconnection_session",
        **kwargs: Any,
    ) -> None:
        """
        Initialize the PYConnection client.

        Args:
            api_id: Soroush Plus API ID (optional for HTTP-only usage)
            api_hash: Soroush Plus API hash (optional for HTTP-only usage)
            phone_number: Phone number for authentication (optional for HTTP-only usage)
            session_name: Name of the session file
            **kwargs: Additional arguments passed to underlying clients
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.session_name = session_name
        self.kwargs = kwargs

        # Initialize the spluslib client internally
        self._splus_client = None
        self._requests_session = requests.Session()

        # Setup requests session defaults
        requests_utils.configure_session(self._requests_session, **kwargs)

    @property
    def splus_client(self):
        """Lazily load and return the spluslib SplusClient."""
        if self._splus_client is None:
            from spluslib import SplusClient

            self._splus_client = SplusClient(
                api_id=self.api_id,
                api_hash=self.api_hash,
                phone_number=self.phone_number,
                session_name=self.session_name,
            )
        return self._splus_client

    @property
    def http(self) -> "RequestHandler":
        """Get the HTTP request handler."""
        return RequestHandler(self._requests_session)

    async def send_message(self, username: str, message: str) -> Any:
        """
        Send a message via Soroush Plus.

        Args:
            username: Target username
            message: Message to send

        Returns:
            Result from spluslib
        """
        client = self.splus_client
        return await client.send_message(username, message)

    async def get_me(self) -> Any:
        """Get current user info from Soroush Plus."""
        client = self.splus_client
        return await client.get_me()

    def http_get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Perform an HTTP GET request.

        Args:
            url: URL to request
            params: Query parameters
            headers: Request headers
            **kwargs: Additional arguments for requests.get

        Returns:
            requests.Response object
        """
        return self.http.get(url, params=params, headers=headers, **kwargs)

    def http_post(
        self,
        url: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Perform an HTTP POST request.

        Args:
            url: URL to request
            data: Form data
            json: JSON data to send
            headers: Request headers
            **kwargs: Additional arguments for requests.post

        Returns:
            requests.Response object
        """
        return self.http.post(url, data=data, json=json, headers=headers, **kwargs)


class RequestHandler:
    """
    Handler for HTTP requests using the requests library.

    Provides convenient methods for common HTTP operations
    with sensible defaults and logging.
    """

    def __init__(self, session: requests.Session) -> None:
        self.session = session

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a GET request."""
        merged_headers = {**(headers or {}), **self.session.headers}
        return self.session.get(url, params=params, headers=merged_headers, **kwargs)

    def post(
        self,
        url: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a POST request."""
        merged_headers = {**(headers or {}), **self.session.headers}
        return self.session.post(
            url, data=data, json=json, headers=merged_headers, **kwargs
        )

    def put(
        self,
        url: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a PUT request."""
        merged_headers = {**(headers or {}), **self.session.headers}
        return self.session.put(
            url, data=data, json=json, headers=merged_headers, **kwargs
        )

    def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """Send a DELETE request."""
        merged_headers = {**(headers or {}), **self.session.headers}
        return self.session.delete(url, headers=merged_headers, **kwargs)


# Convenience functions
def http_get(url: str, **kwargs: Any) -> requests.Response:
    """Quick HTTP GET request."""
    import requests as _requests
    return _requests.get(url, **kwargs)


def http_post(url: str, **kwargs: Any) -> requests.Response:
    """Quick HTTP POST request."""
    import requests as _requests
    return _requests.post(url, **kwargs)