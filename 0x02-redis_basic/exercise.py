#!/usr/bin/env python3
"""
redis
"""
import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count INCR """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

class Cache():
    """ cache class """
    def __init__(self):
        """ init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store date """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, None]:
        """ make the data to its origin type """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_int(self, key):
        """ get int """
        return self.get(key, int)

    def get_str(self, key):
        """ get str """
        val = self._redis.get(key)
        return val.decode('utf-8')
