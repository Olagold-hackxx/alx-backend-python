#!/usr/bin/env python3
"""A type-annotated function sum_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> str:
    """function sum_mixed_list which takes a list mxd_lst of integers and floats
    returns their sum as a float"""
    result: float = sum(mxd_lst)
    return result