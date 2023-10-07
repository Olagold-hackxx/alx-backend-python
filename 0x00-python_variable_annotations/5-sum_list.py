#!/usr/bin/env python3
"""A type-annotated function sum_list"""
from typing import List


def sum_list(n: List[float]) -> float:
    """function sum_list which takes a list input_list of floats as argument,
    returns their sum as a float"""
    result: float = sum(n)
    return result