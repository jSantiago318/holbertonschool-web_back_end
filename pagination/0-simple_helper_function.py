#!/usr/bin/env python3
"""Module that computes index ranges for pagination parameters."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a given page.

    Args:
        page: The 1-indexed page number.
        page_size: The number of items contained in a page.

    Returns:
        A tuple holding the start index and the end index of the range
        of indexes to return for those pagination parameters.
    """
    start = (page - 1) * page_size
    return (start, start + page_size)
