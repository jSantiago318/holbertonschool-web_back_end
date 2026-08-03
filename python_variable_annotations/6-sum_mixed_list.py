#!/usr/bin/env python3
"""Module that provides a type-annotated mixed list summing function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list holding integers and floats.

    Args:
        mxd_lst: The list of integers and floats to add together.

    Returns:
        The sum of every number in mxd_lst, as a float.
    """
    return float(sum(mxd_lst))
