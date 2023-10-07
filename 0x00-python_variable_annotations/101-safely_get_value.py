#!/usr/bin/env python3
"""A type-annotated function safe_first_element"""
from typing import Optional, Mapping, Any, Union, TypeVar


T = TypeVar('T', bound=Mapping)
def safely_get_value(dct: Mapping, key: Any, default: Optional[T]) -> Union[Any, T]:
    """annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default