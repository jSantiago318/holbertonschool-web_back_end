#!/usr/bin/env python3
"""Module that provides a type-annotated floor function."""
import math


def floor(n: float) -> int:
    """Return the floor of a float as an integer.

    Args:
        n: The float to round down.

    Returns:
        The largest integer less than or equal to n.
    """
    return math.floor(n)
