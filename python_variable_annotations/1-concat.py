#!/usr/bin/env python3
"""Module that provides a type-annotated concatenation function."""


def concat(str1: str, str2: str) -> str:
    """Return the concatenation of two strings.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        The string str1 followed by the string str2.
    """
    return str1 + str2
