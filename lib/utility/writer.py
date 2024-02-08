#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.

from lib.utility.path import *


def write_urls_to_file(file_name, urls):
    file_name = DATA_PATH + "/" + file_name
    txt_file = open(file_name, 'w')
    for url in urls:
        txt_file.write(url+"\n")
    txt_file.close()
