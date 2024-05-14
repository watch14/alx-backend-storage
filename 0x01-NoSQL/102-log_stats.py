#!/usr/bin/env python3
""" get from nginx """
from pymongo import MongoClient
from collections import Counter

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    stat = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{stat} status check")

    print("IPs:")
    ips = collection.distinct("ip")
    ip_counts = Counter(ips).most_common(10)
    for ip, count in ip_counts:
        print(f"\t{ip}: {count}")
