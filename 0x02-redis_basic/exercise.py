#!/usr/bin/env python3
"""
redis
"""
import redis
import uuid
from typing import Union


class Cache():
    """ cache class """
    def __init__(self):
        """ init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store date """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
