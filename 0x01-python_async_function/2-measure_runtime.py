#!/usr/bin/env python3
"""An asynchronous coroutine measure_time"""
import asyncio
import time

wait_n = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    start = time.perf_counter()
    asyncio.gather(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time/n
