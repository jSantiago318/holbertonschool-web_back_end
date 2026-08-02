#!/usr/bin/env python3
"""Module providing a coroutine that waits for a random delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the number of seconds waited.

    Args:
        max_delay: The upper bound of the delay, in seconds.

    Returns:
        The random delay between 0 and max_delay that was awaited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
