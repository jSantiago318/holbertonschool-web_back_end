#!/usr/bin/env python3
"""Module that pairs a string with the square of a number."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple holding a string and the square of a number.

    Args:
        k: The string placed first in the tuple.
        v: The integer or float whose square is placed second.

    Returns:
        A tuple whose first element is k and whose second element is
        the square of v.
    """
    return (k, v ** 2)
