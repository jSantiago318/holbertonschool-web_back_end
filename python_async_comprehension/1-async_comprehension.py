#!/usr/bin/env python3
"""Module collecting random numbers with an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return ten random floats gathered from async_generator.

    Uses an async comprehension over async_generator to collect the
    ten random numbers it yields, then returns them as a list.
    """
    return [number async for number in async_generator()]
