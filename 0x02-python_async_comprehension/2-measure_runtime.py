#!/usr/bin/env python3
"""A coroutine"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
