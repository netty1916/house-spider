#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import logging
from lib.auxiliary.config import LOG_FILE, LOG_LEVEL

# 配置日志记录器
logger = logging.getLogger('my_logger')
LOGGER_INITED = False


def truncate_log():
    with open(LOG_FILE, 'w') as file:
        file.truncate()


def init_logger_manager():
    global logger
    global LOGGER_INITED
    if not LOGGER_INITED:
        logger.setLevel(LOG_LEVEL)  # 设置日志记录器的级别

        '''
        # 添加控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOG_LEVEL)  # 设置控制台处理器的级别
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        '''

        truncate_log()
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(LOG_LEVEL)  # 设置文件处理器的级别
        formatter = logging.Formatter('%(asctime)s [%(threadName)s] %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        print(f'logger {type(logger),id(logger)}')
        LOGGER_INITED = True

        # threading.get_ident()


class LoggerStream():
    def __init__(self, tag: str):
        self.tag = tag

    def info(self, text):
        logger.info(f"{self.tag} ... {text}")

    def debug(self, text):
        logger.debug(f"{self.tag} ... {text}")

    def error(self, text):
        logger.error(f"{self.tag} ... {text}")


init_logger_manager()
