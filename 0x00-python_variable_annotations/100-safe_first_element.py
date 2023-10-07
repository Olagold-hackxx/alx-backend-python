#!/usr/bin/env python3
"""A type-annotated function safe_first_element"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotated function"""
    if lst:
        return lst[0]
    else:
        return None
