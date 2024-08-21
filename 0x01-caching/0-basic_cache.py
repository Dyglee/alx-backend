#!/usr/bin/env python3
"""
Module that defines a simple cache system (BasicCache)
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that has no limit on its storage.
    It inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item to the cache with the given key.
        If the key or item is None, the method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by the given key.
        If the key is None or does not exist in the cache, return None.
        """
        return self.cache_data.get(key, None)
