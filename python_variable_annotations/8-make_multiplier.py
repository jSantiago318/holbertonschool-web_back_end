#!/usr/bin/env python3
"""Module that builds multiplier functions."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier: The float every argument is multiplied by.

    Returns:
        A function taking a float and returning it multiplied by
        multiplier.
    """
    def multiply(value: float) -> float:
        """Return value multiplied by the captured multiplier."""
        return value * multiplier
    return multiply
