#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Return a list of an object's available attributes.

    Args:
        obj (object): The object to look up.

    Returns:
        list: List of available attributes and methods.
    """
    return (dir(obj))
