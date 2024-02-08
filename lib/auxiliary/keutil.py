#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


import time
import os
import re
from lib.auxiliary.comutils import CommonUtil
from lib.auxiliary.logger import LoggerStream
from lib.auxiliary.souputil import SoupUtil
from lib.auxiliary.logger import logger
from lib.auxiliary.config import HTML_OUT_FOLDER
from bs4.element import Tag


class BeikeUtil(LoggerStream):
    global zinfo_cache
    zinfo_cache = dict()

    def __init__(self):
        super().__init__('BKEU')

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

    def build_zone_info_cache(self, site, soup_util: SoupUtil, tag=''):
        t1 = time.time()  # 开始计时
        if site not in zinfo_cache:
            pairs = self.build_zone_info(site, soup_util, tag)
            t2 = time.time()
            self.debug(
                f"Cost {t2 - t1} s to New Zone {tag} {site} with {len(pairs)}.")
            zinfo_cache[site] = pairs
            return pairs
        else:
            t2 = time.time()
            self.debug(
                f"Cost {t2 - t1} s to Get Zone {tag} {site} cache {len(zinfo_cache)}.")
            return zinfo_cache[site]

    # 获取房屋基本信息
    def build_house_basic(self, psite, elem: Tag, soup_util: SoupUtil):
        logger.debug(f'elem type {type(elem)}')
        house_basic = dict()
        # 1-名称,价格
        name = elem.find('div', class_='title').text.strip()
        price = elem.find('div', class_="totalPrice").text.strip()

        # 2-小区页面、小区名称
        pos_elem = elem.find('div', class_="positionInfo").find('a')
        qsite = pos_elem.get('href').strip()
        qname = pos_elem.text.strip()

        # 3-楼层、布局、面积、朝向
        desc = elem.find('div', class_="houseInfo")
        parts = desc.text.replace("\n", "").replace(
            '(', '|').replace(')', '|').strip().split('|')
        elements = [part.strip().replace(',', '，')
                    for part in parts if part.strip() != '']
        floor = elements[0] if len(elements) >= 1 else ''  # 所在楼层
        total_floors = elements[1] if len(
            elements) >= 2 else ''  # 总楼层，注意去掉结尾的括号
        layout = elements[2] if len(elements) >= 3 else ''  # 布局
        size = elements[3] if len(elements) >= 4 else ''  # 面积
        direction = elements[4] if len(elements) >= 4 else ''  # 朝向，注意去掉结尾的括号

        # 4-发布及客户看房情况
        followInfo = elem.find('div', class_="followInfo")
        publish_infos = followInfo.text.strip().replace("\n", "").split('/')
        publish = publish_infos[1] if len(publish_infos) >= 2 else ''
        focus = publish_infos[0] if len(publish_infos) >= 1 else ''

        # 5-是否满五年
        taxelem = elem.find('span', class_="taxfree")
        result = re.search(
            r'<span class="taxfree">(.*?)</span>', str(taxelem))
        taxfree = result.group(1) if result else ''  # 输出： 满五年

        # 6-描述信息
        descelem = elem.find('a', class_="img").find('img', class_='lj-lazy')
        desc = descelem.get("alt").strip()

        house_basic['小区链接'] = qsite
        house_basic['房屋概述'] = name
        # house_basic['页面链接'] = psite
        # house_basic['页面文件'] = BeikeUtil.page_url_to_filename(psite)
        # house_basic['小区文件'] = BeikeUtil.page_url_to_filename(qsite)
        house_basic['房屋总价'] = price
        house_basic['小区名称'] = qname
        house_basic['其所楼层'] = floor
        house_basic['总楼层数'] = total_floors
        house_basic['房间布局'] = layout
        house_basic['建筑面积'] = size
        house_basic['房屋朝向'] = direction
        house_basic['发布多久'] = publish
        house_basic['关注人数'] = focus
        house_basic['满五年否'] = taxfree
        house_basic['总体描述'] = desc

        return CommonUtil.strip_dict(house_basic)

    def build_zone_info(self, site, soup_util: SoupUtil, tag=''):
        zone_info = {
            '建筑类型': '',
            '房屋总数': '',
            '楼栋总数': '',
            '绿化率': '',
            '容积率': '',
            '交易权属': '',
            '建成年代': '',
            '供暖类型': '',
            '用水类型': '',
            '用电类型': '',
            '物业费': '',
            '附近门店': '',
            '物业公司': '',
            '开发商': ''
            # '房屋文件': BeikeUtil.page_url_to_filename(site)
        }

        t1 = time.time()
        # soup = BeautifulSoup(str2, 'html.parser')
        soup = soup_util.build_soup(str(site).strip(), tag)

        t2 = time.time()
        self.debug(f"build_zone_info Cost {t2 - t1} s to build_soup {tag} ")

        xiaoqu_info_items = soup.find_all('div', class_='xiaoquInfoItem')

        spans_label = []
        spans_value = []
        for item in xiaoqu_info_items:
            spans = item.find_all('span', class_='xiaoquInfoLabel')
            spans_label.extend(spans)
            spans = item.find_all('span', class_='xiaoquInfoContent')
            spans_value.extend(spans)

        logger.debug(f'spans_label {len(spans_label)}')
        logger.debug(f'spans_value {len(spans_value)}')

        for id, span in enumerate(spans_label):
            label = span.text.strip().replace("\n", '')
            value = spans_value[id].get_text(strip=True).replace("\n", '')

            if spans_value[id]:
                for child in spans_value[id].contents:
                    if child.name == 'span' and child.get("mendian"):
                        value1 = {
                            'name': child.get_text(strip=True),
                            'mapInfo': child.get("mendian").strip().replace(',', '，'),
                            'location': value
                        }
                        value = value1
                        break

            logger.debug(f'{label} : {value}')

            if label in zone_info:
                zone_info[label] = value

        t3 = time.time()
        self.debug(
            f"build_zone_info Cost {t3 - t2} s to  retrive element {tag} ")

        # 提取结果
        return CommonUtil.strip_dict(zone_info)

    def build_house_detail(self, site, soup_util: SoupUtil, tag=''):
        '''
        尝试解析房屋详细信息: https://tj.ke.com/ershoufang/101122578346.html?fb_expo_id=806998587732062210
        '''
        soup = soup_util.build_soup(site, tag)
        introContent = soup.find('div', class_="introContent")

        # 初始化一个字典来存储提取的信息
        house_detail = {
            '户型结构': '',
            '套内面积': '',
            '所在楼层': '',
            '建筑结构': '',
            '装修情况': '',
            '梯户比例': '',
            '供暖方式': '',
            '配备电梯': '',
            '挂牌时间': '',
            '交易权属': '',
            '上次交易': '',
            '房屋用途': '',
            '房屋年限': '',
            '产权所属': '',
            '抵押信息': '',
            '房本备件': '',
        }

        if not introContent:
            logger.error(
                f'No detail for {site} with name {BeikeUtil.page_url_to_filename(site)}')
            return house_detail

        # 查找包含信息的数据
        for item in introContent.find_all('li'):
            label = item.find('span', class_='label').text.strip()
            value = item.get_text(strip=True).replace(
                "\n", '').replace(label, '')
            logger.debug(f'{label} : {value}')
            if label in house_detail:
                house_detail[label] = value

        # 提取结果
        # return CommonUtil.strip_dict({k: v for k, v in house_detail.items() if v})
        return CommonUtil.strip_dict(house_detail)
