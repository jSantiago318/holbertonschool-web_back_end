#!/usr/bin/env python3
"""Module spawning several wait_random coroutines concurrently."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in ascending order.

    The delays are collected with asyncio.as_completed, so each one is
    appended as its coroutine finishes. Shorter delays complete first,
    which yields a sorted list without ever calling sort().

    Args:
        n: The number of times wait_random is spawned.
        max_delay: The upper bound of each random delay, in seconds.

    Returns:
        The list of all the delays, in ascending order.
    """
    delays: List[float] = []
    coroutines = [wait_random(max_delay) for _ in range(n)]
    for coroutine in asyncio.as_completed(coroutines):
        delays.append(await coroutine)
    return delays
