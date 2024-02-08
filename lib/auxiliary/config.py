#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import logging
import inspect
import os
import sys


def get_root_path():
    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    parent_path = os.path.dirname(file_path)
    lib_path = os.path.dirname(parent_path)
    root_path = os.path.dirname(lib_path)
    return root_path


THREAD_POOL_SIZE = 100

# spider
# To prevent the crawler from being banned, set a random delay. If you don't want to use delay, set it to False. You can modify the random_delay() function for the specific time, and due to multithreading, it is recommended to set the value to greater than 10.
RANDOM_DELAY = False
LIANJIA_SPIDER = "lianjia"
BEIKE_SPIDER = "ke"
SPIDER_NAME = BEIKE_SPIDER

# location
TIANJIN_ALL_DISTRICTS = False

# storage
SAVE_RESULT_TO_EXCEL = True

SAVE_HTML_DATA_TO_FILE = True
SAVE_HTML_DATA_TO_MONGO = False
SAVE_SITE_URL_TO_MONGO = False

# Mongo
MONGO_DB_NAME = 'spider_bk_data'
MONGO_DATA_HTML = 'spider_bk_data_html'
MONGO_DATA_SITE_URL = 'spider_bk_data_site_url'
MONGO_LINK = 'mongodb://spider:8eaa0901b80a@192.168.1.51:7017/'

# HTML file 
HTML_OUT_FOLDER = './data/html'

# Path settings.
DATA_RELATIVE_PATH = "/data"
ROOT_PATH = get_root_path()
DATA_PATH = ROOT_PATH + DATA_RELATIVE_PATH
SAMPLE_PATH = ROOT_PATH + "/sample"
LOG_PATH = ROOT_PATH + "/log"

# query method for Page data
QUERY_HTML_FROM = 'FILE'   # 'MONGO'

# log
LOG_LEVEL = logging.INFO
LOG_FILE = './app.log'
