#!/usr/bin/env python3
"""Update all topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics to set
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
