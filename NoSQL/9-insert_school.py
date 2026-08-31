#!/usr/bin/env python3
"""Module inserting a document in a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert kwargs as a new document of mongo_collection.

    Return the _id of the inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
