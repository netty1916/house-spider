#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import threading
from lib.zone.city import lianjia_cities, beike_cities
from lib.utility.date import *
from lib.auxiliary.logger import LoggerStream
import random
from lib.auxiliary.config import RANDOM_DELAY, LIANJIA_SPIDER, BEIKE_SPIDER, SPIDER_NAME


class BaseSpider(LoggerStream):
    @staticmethod
    def random_delay():
        if RANDOM_DELAY:
            time.sleep(random.randint(0, 16))

    def __init__(self, name):
        super().__init__('')

        self.name = name
        if self.name == LIANJIA_SPIDER:
            self.cities = lianjia_cities
        elif self.name == BEIKE_SPIDER:
            self.cities = beike_cities
        else:
            self.cities = None
        # 准备日期信息，爬到的数据存放到日期相关文件夹下
        self.date_string = get_date_string()
        print('Today date is: %s' % self.date_string)

        self.total_num = 0  # 总的小区个数，用于统计
        print("Target site is {0}.com".format(SPIDER_NAME))
        self.mutex = threading.Lock()  # 创建锁

    def create_prompt_text(self):
        """
        根据已有城市中英文对照表拼接选择提示信息
        :return: 拼接好的字串
        """
        city_info = list()
        count = 0
        for en_name, ch_name in self.cities.items():
            count += 1
            city_info.append(en_name)
            city_info.append(": ")
            city_info.append(ch_name)
            if count % 4 == 0:
                city_info.append("\n")
            else:
                city_info.append(", ")
        return 'Which city do you want to crawl?\n' + ''.join(city_info)

    def get_chinese_city(self, en):
        """
        拼音拼音名转中文城市名
        :param en: 拼音
        :return: 中文
        """
        return self.cities.get(en, None)
