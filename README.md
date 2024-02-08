# Crawler for second-hand house on Beike.com
- **Query second-hand house information on Beike.com**
- **Output content to Excel**
- **Records include the following fields:"**
  - 提取日期,区域,街道,房屋概述,小区链接,房屋总价,小区名称,其所楼层,总楼层数,房间布局,建筑面积,房屋朝向,发布多久,关注人数,满五年否,总体描述,建筑类型,房屋总数,楼栋总数,绿化率,容积率,交易权属,建成年代,供暖类型,用水类型,用电类型,物业费,附近门店,物业公司,开发商,房屋链接,户型结构,套内面积,所在楼层,建筑结构,装修情况,梯户比例,供暖方式,配备电梯,挂牌时间,上次交易,房屋用途,房屋年限,产权所属,抵押信息,房本备件

- **This code is for learning and communication only, please do not use it for commercial purposes, and consequences are self-inflicted.**

- **If it’s useful, please click the star to support!！**

# Get started
- pip install -r requirements.txt
- python second_hand_house.py tj
  - “tj” stands for querying second-hand houses in Tianjin.

# Option settings.
- Refer to lib/auxiliary/config.py.


# Update records.
- **2024/02/08**
  - Based on the original code, additional community information and detailed house information have been added, assembled into a complete Excel record, and stored.