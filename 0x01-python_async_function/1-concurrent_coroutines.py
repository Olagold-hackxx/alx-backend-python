#!/usr/bin/env python3
"""An asynchronous coroutine wait_n"""
from typing import List, Callable
wait_random = __import__(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2 int arguments
    (in this order):n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays in asc order (float values)
    """
    delays = []
    for i in range(n):
        delay: float = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
