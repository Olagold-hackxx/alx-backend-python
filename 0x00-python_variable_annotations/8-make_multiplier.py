#!/usr/bin/env python3
"""A type-annotated function to_kv"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier that takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier"""
    def multiply(multiply_by: float) -> float:
        return multiply_by * multiplier
    return multiply
