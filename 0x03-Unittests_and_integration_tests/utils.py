#!/usr/bin/env python3
"""
Utility functions for nested map access, HTTP JSON retrieval, and memoization.
"""

from typing import Any, Mapping, Sequence
import requests
from functools import wraps


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map using a sequence of keys.

    Args:
        nested_map: A dictionary to traverse.
        path: A sequence of keys representing the lookup path.

    Returns:
        The value at the end of the path.

    Raises:
        KeyError: If the path cannot be fully resolved.
    """
    current: Any = nested_map
    for i, key in enumerate(path):
        if not isinstance(current, Mapping):
            # If path continues but current is not a dict
            raise KeyError(key)
        current = current[key]
    return current


def get_json(url: str) -> dict:
    """
    Fetch JSON data from a URL.

    Args:
        url: The URL to fetch from.

    Returns:
        The response JSON as a dictionary.
    """
    response = requests.get(url)
    return response.json()


def memoize(method):
    """
    Decorator to cache a method's result in the instance.

    Args:
        method: The method to memoize.

    Returns:
        The cached result on subsequent calls.
    """
    attr_name = f"_memoized_{method.__name__}"

    @wraps(method)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return property(wrapper)
