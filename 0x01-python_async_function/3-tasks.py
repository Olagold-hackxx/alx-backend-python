#!/usr/bin/env python3
"""An asynchronous coroutine wait_n"""
from asyncio import create_task, Future

wait_random = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Future[float]:
    """Create a task for wait_random async call"""
    return create_task(wait_random(max_delay))
