#!/usr/bin/env python3
""" get from nginx """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"method {method}: {count}")

    stat = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{stat} status check")
