#!/usr/bin/env python3
""" 101-main """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students
