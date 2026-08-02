#!/usr/bin/env python3
"""Module measuring the average runtime of the wait_n coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average execution time of one wait_n coroutine.

    Runs wait_n(n, max_delay) with asyncio.run, measures the total
    elapsed time and divides it by n.

    Args:
        n: The number of times wait_random is spawned by wait_n.
        max_delay: The upper bound of each random delay, in seconds.

    Returns:
        The total execution time divided by n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
