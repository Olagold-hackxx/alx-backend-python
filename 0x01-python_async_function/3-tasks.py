#!/usr/bin/env python3
"""A func task_wait_random """
from asyncio import create_task, Task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """Create a task for wait_random async call"""
    return create_task(wait_random(max_delay))
