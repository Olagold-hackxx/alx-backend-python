#!/usr/bin/env python3
"""A type-annotated function concat"""


def concat(str1: str, str2: str) -> str:
    """function concat that takes a string str1 and a string str2,
    returns a concatenated string
    """
    return "{}{}".format(str1, str2)
