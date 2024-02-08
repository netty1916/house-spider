#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.

from lib.auxiliary.config import SPIDER_NAME
from lib.spider.second_spider import SecondHandSpider

if __name__ == "__main__":
    spider = SecondHandSpider(SPIDER_NAME)
    spider.start()
