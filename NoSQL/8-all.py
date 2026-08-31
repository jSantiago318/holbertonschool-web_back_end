#!/usr/bin/env python3
"""Module listing every document of a MongoDB collection."""


def list_all(mongo_collection):
    """Return the list of all the documents of mongo_collection.

    An empty list is returned when the collection holds no document.
    """
    return list(mongo_collection.find())
