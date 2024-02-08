#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


class SecondHandHouse(object):
    def __init__(self, data: dict):
        self.data = data

    def text(self):
        return ','.join(str(value) for value in self.data.values())
