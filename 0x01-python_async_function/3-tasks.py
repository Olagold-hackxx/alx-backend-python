#!/usr/bin/env python3
"""An asynchronous coroutine wait_n"""
from asyncio import ensure_future, Future

wait_random = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Future[float]:
    """Create a task for wait_random async call"""
    return ensure_future(wait_random(max_delay))
