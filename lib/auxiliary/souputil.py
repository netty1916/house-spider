#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import time
import requests

from lib.auxiliary.config import HTML_OUT_FOLDER, MONGO_DB_NAME, MONGO_DATA_HTML, MONGO_DATA_SITE_URL
from lib.auxiliary.config import SAVE_HTML_DATA_TO_MONGO, SAVE_HTML_DATA_TO_FILE, SAVE_SITE_URL_TO_MONGO
from lib.auxiliary.config import QUERY_HTML_FROM

from lib.auxiliary.filedb import FileDB
from lib.auxiliary.mongo import MongoConnector
from bs4 import BeautifulSoup, SoupStrainer
from lib.request.headers import create_headers
from lib.spider.base_spider import BaseSpider
from lib.auxiliary.logger import LoggerStream


class SoupUtil(LoggerStream):
    def __init__(self):
        super().__init__('SOUP')
        self.file_db = FileDB(HTML_OUT_FOLDER)
        if QUERY_HTML_FROM == 'MONGO' or SAVE_HTML_DATA_TO_MONGO or SAVE_SITE_URL_TO_MONGO:
            self.mongo_db_html = MongoConnector(MONGO_DB_NAME, MONGO_DATA_HTML)
            self.mongo_db_url = MongoConnector(
                MONGO_DB_NAME, MONGO_DATA_SITE_URL)

    def close(self):
        if QUERY_HTML_FROM == 'MONGO' or SAVE_HTML_DATA_TO_MONGO or SAVE_SITE_URL_TO_MONGO:
            self.mongo_db_html.close()
            self.mongo_db_url.close()

    def write(self, url, content):
        if SAVE_HTML_DATA_TO_MONGO:
            self.mongo_db_html.write(url, content)

        if SAVE_HTML_DATA_TO_FILE:
            self.file_db.write(url, content)

        if SAVE_SITE_URL_TO_MONGO:
            self.mongo_db_url.write(url, content)

    def build_soup(self, url, tag=''):
        t1 = time.time()
        html = None
        if QUERY_HTML_FROM == 'FILE':
            html = self.file_db.read(url, tag)
        else:
            html = self.mongo_db_html.read(url, tag)

        if not html:
            self.info(f"【从外网抓取】：{url}")
            headers = create_headers()
            BaseSpider.random_delay()
            response = requests.get(url, timeout=10, headers=headers)
            self.write(url, response.content)
            response.encoding = 'utf-8'
            html = response.content
        t2 = time.time()
        self.debug(f"Cost {t2 - t1} s to build_soup read {tag}.")

        # only_div_tags = SoupStrainer("div")
        soup = BeautifulSoup(html, 'html.parser', parse_only=None,
                             from_encoding=None, exclude_encodings=None)  # lxml html5lib "html.parser"

        t3 = time.time()
        self.debug(f"Cost {t3 - t2} s to BeautifulSoup {tag}.")
        return soup

    def custom_strainer(self, elem, attrs):
        for attr in attrs:
            print("attr:" + attr + "=" + attrs[attr])

        if elem == 'div' or elem == 'li' or elem == 'span':
            return True
        return False
