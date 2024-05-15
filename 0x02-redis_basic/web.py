#!/usr/bin/env python3
""" web """
import requests
import redis


def get_page(url: str) -> str:
    """ page """
    redis_conn = redis.Redis()

    url_count_key = f"count:{url}"
    redis_conn.incr(url_count_key)

    cached_content = redis_conn.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    page_content = response.text

    redis_conn.setex(url, 10, page_content)

    return page_content


if __name__ == "__main__":
    url = ("http://slowwly.robertomurray.co.uk/"
           "delay/1000/url/"
           "https://www.example.com")
    print(get_page(url))
