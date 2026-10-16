"""
Soroush Plus utility functions for PYConnection.

Provides helper functions and configuration for the spluslib integration.
"""

import sys
from typing import Dict, Any


def ensure_spluspy_import() -> None:
    """
    Ensure the spluspy module is available in sys.modules.

    This is needed because spluslib internally imports from spluspy,
    which is vendored within spluslib._base. This function registers
    spluslib._base as spluspy in sys.modules so internal imports work.
    """
    import spluslib as _spluslib

    if "spluspy" not in sys.modules:
        sys.modules["spluspy"] = _spluslib._base_pkg


def get_splus_client(
    api_id: int,
    api_hash: str,
    phone_number: str,
    session_name: str = "pyconnection_session",
) -> "SplusClient":
    """
    Create and return a spluslib SplusClient instance.

    Args:
        api_id: Soroush Plus API ID
        api_hash: Soroush Plus API hash
        phone_number: Phone number for authentication
        session_name: Name of the session file

    Returns:
        SplusClient instance
    """
    ensure_spluspy_import()
    from spluslib import SplusClient

    return SplusClient(
        api_id=api_id,
        api_hash=api_hash,
        phone_number=phone_number,
        session_name=session_name,
    )


def is_user_authenticated(client: "SplusClient") -> bool:
    """
    Check if a soroush Plus client is authenticated.

    Args:
        client: SplusClient instance

    Returns:
        True if the user is authenticated, False otherwise
    """
    try:
        return client.is_user_authenticated()
    except Exception:
        return False