#!/usr/bin/env python3
"""Module that measures the length of every element of an iterable."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each element of an iterable paired with its length.

    Args:
        lst: An iterable of sequences, such as a list of strings.

    Returns:
        A list of tuples holding each element and its length.
    """
    return [(i, len(i)) for i in lst]
