#!/usr/bin/env python3
"""Module that provides a type-annotated list summing function."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list: The list of floats to add together.

    Returns:
        The sum of every float in input_list.
    """
    return sum(input_list)
