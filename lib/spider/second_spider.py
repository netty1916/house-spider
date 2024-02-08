#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 爬取二手房数据的爬虫派生类

import re
import threadpool

from lib.item.second_hand import SecondHandHouse
from lib.zone.city import get_city
from lib.spider.base_spider import *
from lib.utility.date import *
from lib.utility.path import create_date_path

from lib.zone.area import *
from lib.zone.district import *

from lib.zone.area import get_areas
from lib.zone.district import area_dict, chinese_area_dict, get_districts, get_chinese_district

from lib.utility.log import *
from lib.spider.base_spider import BaseSpider
import time
from lib.auxiliary.logger import logger, init_logger_manager
from lib.auxiliary.config import SAVE_RESULT_TO_EXCEL, THREAD_POOL_SIZE
from lib.auxiliary.config import SPIDER_NAME, TIANJIN_ALL_DISTRICTS
from lib.auxiliary.souputil import SoupUtil
from lib.auxiliary.keutil import BeikeUtil
import threading


class SecondHandSpider(BaseSpider):
    house_keys = []
    global_lock = threading.Lock()

    @staticmethod
    def build_house_list(city_name, area_name, soup_util: SoupUtil, ke_util: BeikeUtil):
        """
        通过爬取页面获得城市指定版块的二手房信息
        :param city_name: 城市
        :param area_name: 版块
        :return: 二手房数据列表
        """
        total_page = 1
        district_name = area_dict.get(area_name, "")
        chinese_district = get_chinese_district(district_name)  # 中文区县
        chinese_area = chinese_area_dict.get(area_name, "")  # 中文版块

        second_hand_list = list()
        # page = 'http://{0}.{1}.com/ershoufang/{2}/'.format(city_name, SPIDER_NAME, area_name)
        page = f'http://{city_name}.{SPIDER_NAME}.com/ershoufang/{area_name}/'
        logger.info(page)  # 打印版块页面地址
        soup1 = soup_util.build_soup(str(page).strip())

        # 获得总的页数，通过查找总页码的元素信息
        try:
            page_box = soup1.find_all('div', class_='page-box')[0]
            matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
            total_page = int(matches.group(1))
        except Exception as e:
            logger.error(f"\tWarning: only find one page for {area_name} {e}")

        # 从第一页开始,一直遍历到最后一页
        for num in range(1, total_page + 1):
            # page = 'http://{0}.{1}.com/ershoufang/{2}/pg{3}'.format(city_name, SPIDER_NAME, area_name, num)
            page = f'http://{city_name}.{SPIDER_NAME}.com/ershoufang/{area_name}/pg{num}'
            soup2 = soup_util.build_soup(str(page).strip(), 'Page')

            # 获得有小区信息的panel
            house_elements = soup2.find_all('li', class_="clear")
            logger.info(f'{page} with {len(house_elements)} elements')
            for house_elem in house_elements:
                t1 = time.time()  # 开始计时
                # 1-获取房屋基础信息
                house_basic = ke_util.build_house_basic(
                    page, house_elem, soup_util)
                t2 = time.time()
                logger.debug(f"Cost {t2 - t1} s to build basic {house_basic['房屋概述']}.")

                # 2-获取所属小区信息
                qsite = house_basic['小区链接'] if house_basic else None
                zone_info = ke_util.build_zone_info_cache(
                    str(qsite).strip(), soup_util, house_basic['房屋概述']) if qsite else {}
                t3 = time.time()
                logger.debug(f"Cost {t3 - t2} s to build zone {house_basic['房屋概述']}.")

                # 3-尝试解析房屋详细信息: https://tj.ke.com/ershoufang/101122578346.html?fb_expo_id=806998587732062210
                elem = house_elem.find(
                    'a', class_="img VIEWDATA CLICKDATA maidian-detail")
                data_action = str(BeikeUtil.get_expo_id(
                    elem.get('data-action').strip()))
                house_site = f'{elem.get("href").strip()}?fb_expo_id={data_action}'
                house_detail = ke_util.build_house_detail(
                    str(house_site).strip(), soup_util, house_basic['房屋概述']) if house_site else {}
                # end

                t4 = time.time()
                logger.debug(f"Cost {t4 - t3:.3f} s to build detail {house_basic['房屋概述']}.")

                # 4-合并
                house_info = {'区域': chinese_district,
                              '街道': chinese_area,
                              '房屋链接': house_site}
                house_merge = {**house_info, **house_basic,
                               **zone_info, **house_detail}

                if not SecondHandSpider.house_keys:
                    with SecondHandSpider.global_lock:
                        SecondHandSpider.house_keys = house_merge.keys()

                # 作为对象保存
                second_hand_house = SecondHandHouse(house_merge)
                second_hand_list.append(second_hand_house)
                t5 = time.time()
                logger.info(f"Cost {t5 - t1:.2f} s with basic-{len(house_basic)},zone-{len(zone_info)},detail-{len(house_detail)},all-{len(house_merge)} to build entity {house_basic['房屋概述']}.")
        return second_hand_list

    # 线程内调用
    def build_areas_data(self, city_name, area_name, fmt="csv"):
        """
        对于每个板块,获得这个板块下所有二手房的信息,并且将这些信息写入文件保存
        :param city_name: 城市
        :param area_name: 板块
        :param fmt: 保存文件格式
        :return: None
        """
        soup_util = SoupUtil()  # 每个线程一份
        ke_util = BeikeUtil()

        district_name = area_dict.get(area_name, "")
        csv_file = self.today_path + f"/{district_name}_{area_name}.csv"
        logger.info(f'csv_file: {csv_file}')

        with open(csv_file, "w", newline='', encoding='utf-8-sig') as f:
            # 开始获得需要的板块数据
            house_list = self.build_house_list(
                city_name, area_name, soup_util, ke_util)

            # 锁定，多线程读写
            if self.mutex.acquire(1):
                self.total_num += len(house_list)
                self.mutex.release()  # 释放

            if fmt == "csv":
                if SecondHandSpider.house_keys:
                    f.write('提取日期' + "," + ','.join(str(value)
                            for value in SecondHandSpider.house_keys) + "\n")

                for house in house_list:
                    logger.info(f'ershou: {house.text()}')
                    if SAVE_RESULT_TO_EXCEL:
                        f.write(self.date_string + "," + house.text() + "\n")

        logger.info(f"Done crawl area: {area_name} , save to : {csv_file}")
        soup_util.close()

    def start(self):
        t1 = time.time()  # 开始计时

        city = get_city()
        self.today_path = create_date_path(
            f"{SPIDER_NAME}/ershou", city, self.date_string)

        # 获得城市有多少区列表, district: 区县
        districts = get_districts(city, TIANJIN_ALL_DISTRICTS)
        logger.info(f'City: {city}')
        logger.info(f'Districts: {districts}')

        # 获得每个区的板块, area: 板块
        areas = list()
        for district in districts:
            areas_of_district = get_areas(city, district)
            logger.info(f'{district}: Area list:  {areas_of_district}')

            # 将areas_of_district的全部元素添加到areas的尾部
            areas.extend(areas_of_district)
            # 使用一个字典来存储区县和板块的对应关系, 例如{'beicai': 'pudongxinqu', }
            for area in areas_of_district:
                area_dict[area] = district

        logger.info(f"Area: {areas}")
        logger.info(f"District and areas:{area_dict}")

        # 准备线程池用到的参数
        # areas = areas[0: 1]   # For debugging
        nones = [None for i in range(len(areas))]
        city_list = [city for i in range(len(areas))]
        args = zip(zip(city_list, areas), nones)

        # 针对每个板块写一个文件,启动一个线程来操作
        pool = threadpool.ThreadPool(THREAD_POOL_SIZE)
        my_requests = threadpool.makeRequests(self.build_areas_data, args)
        [pool.putRequest(req) for req in my_requests]
        pool.wait()
        pool.dismissWorkers(THREAD_POOL_SIZE, do_join=True)  # 完成后退出

        # 计时结束，统计结果
        t2 = time.time()
        logger.info(f"Total crawl {len(areas)} areas.")
        logger.info(f"Total cost {t2 - t1} s to crawl {self.total_num} items.")


if __name__ == '__main__':
    pass
