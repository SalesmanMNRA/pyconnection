"""
PYConnection - Combined SDK merging spluslib and requests

A unified library for Soroush Plus userbot connectivity and HTTP requests.
Created by DarkMaster.

This SDK combines:
- `spluslib`: Soroush Plus userbot library (Telethon fork)
- `requests`: Modern HTTP client for Python

Provides a single unified client for both MTProto/Soroush Plus connections
and general HTTP operations.
"""

__version__ = "2.0.0"
__author__ = "DarkMaster"
__email__ = "darkmaster@example.com"

# Core exports
from .client import PYConnectionClient

__all__ = [
    "PYConnectionClient",
    "__version__",
]

# Convenience re-exports of frequently used components
from . import requests_utils  # noqa: F401
from . import soroush_utils  # noqa: F401

# Convenience functions
from .requests_utils import get, post  # noqa: F401
from .soroush_utils import get_splus_client, is_user_authenticated  # noqa: F401

# Aliases for convenience
http_get = get
http_post = post