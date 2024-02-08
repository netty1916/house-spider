#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import os
import re
from lib.auxiliary.config import HTML_OUT_FOLDER
from lib.auxiliary.logger import logger


class CommonUtil():
    @staticmethod
    def page_url_to_filename(url):
        filename = re.sub(r'[^\w\.\-]+', '_', url).replace(' ',
                                                           '_').replace(',', '_')+'.html'
        return os.path.join(HTML_OUT_FOLDER, filename)

    @staticmethod
    def get_expo_id(text):
        match = re.search(r'fb_expo_id=(\d+)', text)
        if match:
            fb_expo_id = match.group(1)
            return fb_expo_id
        else:
            logger.error("fb_expo_id not found in string.")
            return ''

    @staticmethod
    def strip_dict(dict_local: dict):
        for key, value in dict_local.items():
            if value is None:
                dict_local[key] = ''
            if isinstance(value, str):
                dict_local[key] = value.strip().replace("\n", "").replace(
                    ',', '，').replace("：", '').replace('"', '')
            elif isinstance(value, dict):
                for key1, value1 in value.items():
                    if value1 is None:
                        value[key1] = ''
                    else:
                        value[key1] = str(value1).strip().replace("\n", "").replace(
                            ',', '，').replace("：", '').replace('"', '')
                        logger.debug(f'dict value {value[key1]}')

                dict_local[key] = '，'.join(
                    str(f"'{key2}' : '{value2}'") for key2, value2 in value.items())
        logger.debug(f'dict {dict_local}')
        return dict_local
