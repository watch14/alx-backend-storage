#!/usr/bin/env python3
""" inster() """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ inserting """
    return mongo_collection.insert_one(kwargs).inserted_id
