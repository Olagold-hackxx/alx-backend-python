#!/usr/bin/env python3
"""A type-annotated function element_length"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotated function"""
    return [(i, len(i)) for i in lst]
