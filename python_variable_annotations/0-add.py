#!/usr/bin/env python3
"""Module that provides a type-annotated addition function."""


def add(a: float, b: float) -> float:
    """Return the sum of two floats.

    Args:
        a: The first float.
        b: The second float.

    Returns:
        The sum of a and b as a float.
    """
    return a + b
