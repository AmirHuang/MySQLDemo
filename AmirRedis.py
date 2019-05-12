# _*_ coding: utf-8 _*_
# @time     : 2019/03/07
# @Author   : Amir
# @Site     : 
# @File     : AmirRedis.py
# @Software : PyCharm

import redis


class AmirRedis:
    def __init__(self, host="localhost", port=6397, password=""):
        self.__redis = redis.StrictRedis(host=host,
                                         port=port,
                                         password=password)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""

