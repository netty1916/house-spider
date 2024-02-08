#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import os
from lib.auxiliary.config import *


def create_data_path():
    root_path = get_root_path()
    data_path = root_path + DATA_RELATIVE_PATH
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    return data_path


def create_site_path(site):
    data_path = create_data_path()
    site_path = data_path + "/" + site
    if not os.path.exists(site_path):
        os.makedirs(site_path)
    return site_path


def create_city_path(site, city):
    site_path = create_site_path(site)
    city_path = site_path + "/" + city
    if not os.path.exists(city_path):
        os.makedirs(city_path)
    return city_path


def create_date_path(site, city, date):
    city_path = create_city_path(site, city)
    date_path = city_path + "/" + date
    if not os.path.exists(date_path):
        os.makedirs(date_path)
    return date_path


if __name__ == "__main__":
    create_date_path("lianjia", "sh", "20160912")
    create_date_path("anjuke", "bj", "20160912")
