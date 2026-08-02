#!/usr/bin/env python3
"""Module wrapping the wait_random coroutine into an asyncio task."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio task running wait_random.

    Schedules wait_random(max_delay) on the running event loop with
    asyncio.Task and returns the task without awaiting it.

    Args:
        max_delay: The upper bound of the random delay, in seconds.

    Returns:
        The asyncio.Task wrapping the wait_random coroutine.
    """
    return asyncio.Task(wait_random(max_delay))
