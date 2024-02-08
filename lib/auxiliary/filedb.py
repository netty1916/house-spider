#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import os
import re
import time
import threading
from lib.auxiliary.logger import LoggerStream


class FileDB(LoggerStream):
    dir_create_lock = threading.Lock()

    def __init__(self, output_dir):
        super().__init__('FILE')
        self.connection_lock = threading.Lock()  # 用于线程安全的连接锁
        self.output_dir = output_dir

    def sanitize_filename(self, filename):
        # 替换 URL 中的 /、空格、逗号等字符为下划线
        # 同时，确保替换后的字符串能作为一个合法的文件名
        # 替换所有非字母数字字符，但保留下划线和点（因为它们通常是文件扩展名的一部分）
        filename = re.sub(r'[^\w\.\-]+', '_', filename)
        filename = filename.replace(' ', '_').replace(',', '_')
        return filename

    def read(self, key, tag=''):
        # 尝试获取HTML内容
        try:
            t1 = time.time()
            filename = os.path.join(
                self.output_dir, self.sanitize_filename(key))+'.html'
            with open(filename, 'rb') as f:
                data = f.read()

            t2 = time.time()
            self.debug(f"Cost {t2 - t1} s to Read {tag}.")

            if data:
                self.debug(f"Get {tag} {key} <-- {filename}")
                return data
            else:
                return None
        except Exception as e:
            self.error(f"从文件{filename}中读取< {tag} {key}>内容时出错： {e}")
            return None

    def write(self, key, data):
        filename = self.sanitize_filename(key)+'.html'

        with FileDB.dir_create_lock:
            # 确保输出文件夹存在
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)

        with self.connection_lock:  # 使用锁确保线程安全
            try:
                # 将 HTML 内容写入到文件中
                with open(os.path.join(self.output_dir, filename), 'wb') as file:
                    file.write(data)
                    self.debug(f"HTML内容已写入到文件：{key}, {filename}")
            except Exception as e:
                self.error(f"失败,写入HTML到磁盘出错：{key}, {e}")
