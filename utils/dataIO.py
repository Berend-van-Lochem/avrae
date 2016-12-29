'''
Created on Dec 28, 2016

@author: andrew
'''

import os
import redis

class DataIO:
    '''
    A simple class to interface with the redis database.
    '''

    def __init__(self):
        self.db = redis.from_url(os.environ.get("REDIS_URL"))
        
    def get(self, key, default=None):
        encoded_data = self.db.get(key)
        return encoded_data.decode() if encoded_data is not None else default
    
    def set(self, key, value):
        return self.db.set(key, value)
    
    def set_dict(self, key, dictionary):
        return self.db.hmset(key, dictionary)
    
    def get_dict(self, key, dict_key):
        return self.db.hget(key, dict_key).decode()
    
    def get_whole_dict(self, key, default):
        encoded_dict = self.db.hgetall(key)
        if encoded_dict is None: return default
        out = {}
        for k in encoded_dict.keys():
            out[k.decode()] = encoded_dict[k].decode()
        return out