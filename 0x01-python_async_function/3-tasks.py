#!/usr/bin/env python3
"""An asynchronous coroutine wait_n"""
import asyncio
from asyncio import Task

wait_random = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[float]:
    """Create a task for wait_random async call"""
    return asyncio.create_task(wait_random(max_delay))
