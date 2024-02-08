#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import time
import threading
from pymongo import MongoClient
from lib.auxiliary.logger import LoggerStream
from lib.auxiliary.config import MONGO_LINK


class MongoConnector(LoggerStream):
    instance_count = 0

    global_lock = threading.Lock()

    def __init__(self, db_name, connection_name, url=MONGO_LINK):
        self.instance_id = MongoConnector.instance_count
        super().__init__(f'Mongo{[self.instance_id]}')

        MongoConnector.instance_count += 1
        self.zone_info_cache = dict()
        self.connection_lock = threading.Lock()  # 用于线程安全的连接锁
        self.client = None
        self.db = None
        self.collection = None
        self.url = url
        self.db_name = db_name    # spider_bk_data
        self.db_connection = connection_name   # spider_bk_data_html
        self.connect()

    def connect(self):
        with self.connection_lock:  # 使用锁确保线程安全
            while True:
                try:
                    self.client = MongoClient(self.url)
                    self.db = self.client[self.db_name]
                    self.collection = self.db[self.db_connection]
                    self.info("成功连接到MongoDB")
                    break
                except Exception as e:
                    self.error(f"连接到MongoDB失败： {e}")
                    self.error("正在重试...")
                    time.sleep(5)  # 在重试之间等待5秒

    def close(self):
        with self.connection_lock:
            # 确保在对象被销毁时关闭MongoClient连接
            if self.client:
                self.client.close()
                self.info("已断开与MongoDB的连接")
                self.client = None

    def write(self, key, data):
        with self.connection_lock:  # 使用锁确保线程安全
            while True:
                try:
                    self.collection.insert_one(
                        {'key': key, 'data': data})
                    break
                except Exception as e:
                    self.error(f"写入data<{key}>到DB出错： {e}")
                    self.error("正在重试...")
                    time.sleep(5)  # 在重试之间等待5秒
                    # 如果连接失败，尝试重新连接
                    if not self.client:
                        self.connect()

    def read(self, key, tag=''):
        # 尝试获取HTML内容
        try:
            document = self.collection.find_one({'key': key})
            if document:
                data = document['data']
                self.debug(f"Get from Mongo： {tag} {key}")
                return data
            else:
                return None
        except Exception as e:
            self.error(f"从MongoDB中读取data<{tag} {key}>时出错： {e}")
            # 如果连接失败，尝试重新连接
            if not self.client:
                self.connect()
            return None
