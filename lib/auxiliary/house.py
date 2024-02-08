#!/usr/bin/env python
# coding=utf-8
# author: netty1916@gmail.com
#
# This code is for educational and informative purposes only,
# please do not use it for commercial use.


from bs4 import BeautifulSoup


def build_house_info():
    str = '''
        <div class="introContent">
            <div class="base">
                <div class="name">基本属性</div>
                <div class="content">
                    <ul>
                    <li class="  ">
<span class="label">房屋户型</span>
3室1厅2卫
                </li>
                    <li class="  ">
<span class="label">建筑面积</span>
145.21㎡
                </li>
                    <li class="  ">
<span class="label">户型结构</span>
平层
                </li>
                    <li class="  ">
<span class="label">建筑类型</span>
板楼
                </li>
                    <li class="  ">
<span class="label">所在楼层</span>
高楼层 (共30层)
    <span 
        class="VIEWDATA link showMiniAppQrcode" 
        data-adid="100013158" 
        data-housecode="101118681080"
        data-view-evtid="55831" 
        data-view-event="Module_View"
        data-action="housedel_id=101118681080"
        data-qrevtid="55832"
    >咨询楼层</span>
                </li>
                    <li class="  louceng">
<span class="label">楼层高度</span>
暂无数据
                        <span class="icon-box">
        <span class="icon-img">
            <img src="https://file.ljcdn.com/nebula/ershou/icon_1703726020004.png"/>
        </span>
        <span class="tips">
            <p>实际层高需现场测量，具体数据以实际测量为准</p>
            <span class="tips-icon"></span>
        </span>
    </span>
                            </li>
                    <li class="oneline  ">
<span class="label">套内面积</span>
暂无
                        <span 
        class="VIEWDATA link showMiniAppQrcode" 
        data-adid="100013159" 
        data-housecode="101118681080"
        data-view-evtid="55833" 
        data-view-event="Module_View"
        data-action="housedel_id=101118681080"
        data-qrevtid="55834"
    >咨询套内面积</span>
                </li>
                    <li class="  ">
<span class="label">房屋朝向</span>
南
                </li>
                    <li class="  ">
<span class="label">建筑结构</span>
钢混结构
                </li>
                    <li class="  ">
<span class="label">装修情况</span>
其他
                </li>
                    <li class="  ">
<span class="label">梯户比例</span>
两梯四户
                </li>
                    <li class="  ">
<span class="label">供暖方式</span>
集中供暖
                </li>
                    <li class="  ">
<span class="label">配备电梯</span>
有
                </li>
            </ul>
                </div>
            </div>
            
            <div class="transaction">
                <div class="name">交易属性</div>
                <div class="content">
                    <ul>
            <li class=""><span class="label ">挂牌时间</span>2023年04月02日
</li>
<li class=""><span class="label ">交易权属</span>商品房
</li>
<li class=""><span class="label ">上次交易</span>2018年12月21日
</li>
<li class=""><span class="label ">房屋用途</span>普通住宅
</li>
<li class=""><span class="label ">房屋年限</span>满五年
</li>
<li class=""><span class="label ">产权所属</span>非共有
</li>
    <li><span class="label">抵押信息</span><span
        style="display:inline-block;width:64%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;vertical-align:middle;"
        title="无抵押">无抵押</span></li>
        <li class=""><span class="label ">房本备件</span>已上传房本照片
</li>
                            </ul>
                </div>
            </div>

            <div class="disclaimer" style="padding-top: 10px;">特别提示：本房源所示信息仅供参考，购房时请以该房屋档案登记信息、产权证信息以及所签订合同条款约定为准；本房源公示信息不做为合同条款，不具有合同约束力。</div>

        </div>

        '''

    str = '''
    <!DOCTYPE html><html class="" lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" /><!-- 2017.11.8 市场需求加上新的统计 -->

<script>
  ljConf = {
      city_id: '120000',
      city_abbr: 'tj',
      city_name: '天津',
      channel: 'ershoufang',
      page: 'ershoufang_view',
      pageConfig: {"ajaxroot":"\/\/ajax.api.ke.com\/","imAppid":"BEIKE_WEB_20170105","imAppkey":"2d7e19fe599aa5087b4d46948e552e89"},
      feroot: '//s1.ljcdn.com/pegasus/',
      ferootnew: '//s1.ljcdn.com/pegasus/',
      domainConfig: {"webroot":"\/\/bj.ke.com\/","wwwroot":"\/\/www.ke.com\/","ajaxapiroot":"https:\/\/ajax.api.ke.com\/","apiroot":"\/\/ajax.ke.com\/","festaticroot":"\/\/cms.ke.com\/static\/","videoroot":"\/\/video.ljcdn.com\/","feroot":"\/\/s1.ljcdn.com\/pegasus\/","ferootnew":"\/\/s1.ljcdn.com\/pegasus\/","newsroot":"\/\/news.ke.com\/","userroot":"\/\/user.ke.com\/","fangroot":"\/\/bj.fang.ke.com\/","agentroot":"\/\/agent.lianjia.com\/","version":"202401081627157bd","pageconfig":{"ajaxroot":"\/\/ajax.api.ke.com\/","imAppid":"BEIKE_WEB_20170105","imAppkey":"2d7e19fe599aa5087b4d46948e552e89"},"imgroot":null,"behaviors":[]},
      ucid:'',
      cdn:'0',
  };
</script>

<!-- 2017.7.18 开放全国 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?9152f8221cb6243a53c83b956842be8a";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<script src='//file.ljcdn.com/fee/index.js' crossorigin="anonymous"></script><script type="text/javascript" src="//s1.ljcdn.com/captcha-js-sdk-v2/captcha.js"></script><script type="text/javascript" src="//s1.ljcdn.com/clogin/js/pcLogin.js"></script><script>function evn() {var match = location.href.match(/\:\/\/(dev|test|preview|\d).+/);if (match && match[1]) {return match[1];} else {return 'prod';}}window.dt && dt.set({pid: 'Pegasus',uuid: document.cookie.match(/lianjia_uuid=([^;]+)/) ? document.cookie.match(/lianjia_uuid=([^;]+)/)[1] : '',ucid: '',env: evn() === 'prod' ? "production" : "",is_test: evn() !== 'prod',record: {spa: false,white_screen: { enable: false },time_on_page: true,performance: true,js_error: true,js_error_report_config: {ERROR_RUNTIME: true,ERROR_SCRIPT: true,ERROR_STYLE: true,ERROR_IMAGE: true,ERROR_AUDIO: true,ERROR_VIDEO: true,ERROR_CONSOLE: false,ERROR_TRY_CATCH: true,checkErrorNeedReport: function (desc, stack) {const userAgent = navigator.userAgent;const isIE = /Trident|MSIE/.test(userAgent);if (isIE) {return false;}if (!/\/\/(s1\.ljcdn\.com\/)/.test(desc) &&!/\/\/(s1\.ljcdn\.com\/)/.test(stack)) {return false;}if (/\/\/s1\.ljcdn\.com\/(link\-static\/resource\/plat_framework|web\-im\-sdk|agent\-sj\-sdk|vrlab|tingyun|\$\.|\$ is not defined|no stach)/.test(desc) ||/\/\/s1\.ljcdn\.com\/(link\-static\/resource\/plat_framework|web\-im\-sdk|agent\-sj\-sdk|vrlab|tingyun|\$\.|\$ is not defined|no stach)/.test(stack) ||/\/\/s1\.ljcdn\.com\/(pegasus\/redskull\/images\/(common|ershoufang)\/(beian.png|blank.gif|im-chart@2x.png|loading.gif|partner\/zsyh.png|vrgold.png|default_house_detail.png))/.test(desc) ||/\/\/s1\.ljcdn\.com\/(pegasus\/redskull\/images\/(common|ershoufang)\/(beian.png|blank.gif|im-chart@2x.png|loading.gif|partner\/zsyh.png|vrgold.png|default_house_detail.png))/.test(stack)) {return false;}return true;}}},version: '1.0.0'});function _plog(evtId, data, pageId) {var defData = {'plat_form': navigator.platform,'page_url': window.location.href};data = $.extend(defData, data);dt.notify(evtId,pageId || window.location.href,data);}</script>
<script>
    function RESIZEIMG(b,k,l,m){var c=b.parentNode;var d=parseInt(c.offsetWidth)||k;var e=parseInt(c.offsetHeight)||l;var f=d/e;var g=b.naturalWidth||b.width;var h=b.naturalHeight||b.height;var i=g/h;var j="width";if(f<i){j="height";try{b.style["left"]="-"+parseInt(Math.abs((d-(g*e/h))/2))+"px"}catch(e){}}else if(m){try{b.style["top"]="-"+parseInt(Math.abs((e-(h*d/g))/2))+"px"}catch(e){}};b.style[j]="100%";};
</script>
<script>window.FROM_CHANNEL = 'beike';</script>  <link rel="stylesheet" href="https://s1.ljcdn.com/pegasus/redskull/css/sellDetail/index.css?_v=202401081627157">
<meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc">
  <title>满五唯一通透户型楼层好有电梯交通便利_天津新梅江锦秀里二手房3室1厅145.21平米【天津贝壳找房】</title>
  <meta name="description" content="贝壳天津二手房信息网,为您提供满五唯一通透户型楼层好有电梯交通便利,天津新梅江锦秀里二手房出售信息,3室1厅,145.21平米㎡,37050元/平米等基本信息、房源特色、周边配套.查询新梅江锦秀里二手房房源信息就到天津贝壳找房."/>
  <meta name="keywords" content="满五唯一通透户型楼层好有电梯交通便利,天津新梅江锦秀里二手房,新梅江锦秀里二手房出售信息 "/>
  <link rel="canonical" href="https://tj.ke.com/ershoufang/101118681080.html"/>
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.ke.com/tj/ershoufang/101118681080.html" >
<meta name="mobile-agent" content="format=html5;url=https://m.ke.com/tj/ershoufang/101118681080.html"><link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><!--[if lt IE 9]><script type="text/javascript" src="https://s1.ljcdn.com/pegasus/dep/common-require/html5.js?_v=202401081627157" crossorigin="anonymous"></script><![endif]--></head><!-- htmlRef --><body id="beike">
  <div class="sellDetailPage">
    <div class="banner" style="display: block">
    <div class="container">
        <ul class="channelList">
            <li>
                <a href="//www.ke.com/">首页</a>
            </li>
                            <li                     class="selected">
                    <a href="https://tj.ke.com/ershoufang/" >二手房</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.fang.ke.com/loupan" >新房</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.zu.ke.com/zufang" >租房</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.ke.com/xiaoqu/" >小区</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.ke.com/yezhu/maifang/?channel_id=2004" target="_blank">发布房源</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://research.ke.com/" target="_blank">贝壳研究院</a>
                                                        </li>
                            <li                     class="">
                    <a href="javascript:void(0)" >下载APP</a>
                                                                <div class="appQRCode">
                            <img src="//ajax.api.ke.com/qr/getDownloadQr?location=site_middle">
                        </div>
                                    </li>
                            <li                     class="">
                    <a href="https://open.ke.com/home?source=9" target="_blank">开放平台</a>
                                                        </li>
                    </ul>
        <div class="banner-right">
            <div class="login" id="userInfoContainer">
                <i></i>
                <a href="https://clogin.ke.com/login?service=https%3A%2F%2Fwww.ke.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Ftj.ke.com%252Fershoufang%252F101118681080.html%253Ffb_expo_id%253D806996103652151297" id="loginBtn" rel="nofollow">登录</a>
                /
                <a href="https://clogin.ke.com/register?service=https%3A%2F%2Fwww.ke.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Ftj.ke.com%252Fershoufang%252F101118681080.html%253Ffb_expo_id%253D806996103652151297" id="registerBtn" rel="nofollow">注册</a>
            </div>
            <div class="phone">
                <i></i>
                <span>投诉电话 1010-6188</span>
            </div>
        </div>
    </div>
</div>

    <script type="text/template" id="userInfoTpl">
        <i></i>
        <%if(isAgent){%>
        <a id="userNameContainer" href="<%=ljConf.domainConfig.agentroot%>"><%=username%></a>
        <%}else{%>
        <a id="userNameContainer" href="<%=ljConf.domainConfig.userroot%>" rel="nofollow"><%=username%></a>
        <%}%>
        <span id="tipContainer"></span>
        &nbsp;&nbsp;<a href="<%=logoutUrl%>" target="_self">退出</a>
        <span id="pushNewsListContainer"></span>
    </script>
    <script type="text/template" id="pushNewsListTpl">
        <div class="pushNewsList">
            <%for(var i in group_by_type){%>
            <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
            <a href="<%=pushMsgMap[i].url%>"><%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%></a>
            <%}%>
            <%}%>
        </div>
    </script>


    <div data-component="detailHeader">
    <div class="header">
        <div class="menu clear">
            <div class="menuLeft">
                <a href="/ershoufang/" class="logo"></a>
                <!-- <span class="channelName">二手房</span> -->
                <ul class="typeList">
                                    </ul>
            </div>
            <div class="search">
                <div class="input" log-mod="search">
                    <form action="/ershoufang/rs" id="searchForm">
                        <span class="noArrow" data-bl="switch">
                          <span class="state">在售</span>
                          <i></i>
                        </span>
                        <span class="sstate" data-bl="switch">
                            <span data-state="1">在售</span>
                            <span data-state="2">成交</span>
                            <span data-state="3">小区</span>
                        </span>
                        <input type="text" id="searchInput" placeholder="请输入关键字搜索" autocomplete="off">
                        <button type="submit" class="searchButton" data-bl="search" data-el="search">&nbsp;<i></i>&nbsp;
                        </button>
                    </form>
                    <div class="searchMsg" id="searchMsgContainer"></div>
                </div>
            </div>
        </div>
    </div>
    <div class="detailHeader VIEWDATA">
        <div class="title-wrapper" log-mod="detail_header">
            <div class="content">
                                    <span class="worth_position"></span>
                                <div class="title">
                    <h1 class="main" title="满五唯一通透户型楼层好有电梯交通便利">
                        满五唯一通透户型楼层好有电梯交通便利
                                                                                                </h1>
                    <div class="sub">
                                                    满五唯一南北户型通透楼层好有电梯交通便利次新房交
                                            </div>
                </div>
                                    <div class="btnContainer ">
                        <div>
                            <div class="action">
                                <button id="follow" class="followbtn" data-text="关注房源">
                                    关注房源</button>
                                <span id="favCount" class="count">3</span>人关注
                                <span class="layer-qrcode followLayer" style="display: none;">
                        <span class="icon-qrcode">
                          <img width="100" height="100"
                               src="https://ajax.api.ke.com/qr/getDownloadQr?location=follow_app&jweb_channel_key=ershoufang_view"
                               alt="下载贝壳找房APP">
                        </span>
                        <span class="txt">下载贝壳找房APP</span>
                        <span class="sub-txt">房源动态早知道</span>
                        <span class="icon-close"></span>
                      </span>
                            </div>
                        </div>
                    </div>
                            </div>
        </div>
    </div>
    <div class="intro clear" mod-id="lj-common-bread">
        <div class="container">
            <div class="fl l-txt">
                                                            <a href="/">天津房产</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="/ershoufang/">天津二手房</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="/ershoufang/hexi/">河西二手房</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="/ershoufang/xinmeijiang/">新梅江二手房</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="/ershoufang/c1211063460197/">新梅江锦秀里二手房</a>
                                                                                        </div>
        </div>
    </div>
</div>

                                  

<div data-component="fixedTabs" class="fixedContent">
  <div class="fixedTabs">
    <div class="fixedTabsContent">
              <a href="#introduction">房源信息介绍</a>
              <a href="#layout">户型分间</a>
              <a href="#housePic">房源照片</a>
              <a href="#record">看房记录</a>
              <a href="#resblockCardContainer">小区简介</a>
              <a href="#calculator">税费贷款</a>
              <a href="#around">周边配套</a>
          </div>
  </div>
</div>


      <div data-component="overviewIntro">
  <div class="overview">
    <div class="img" id="topImg">
      <div class="imgContainer">
        <img class="new-default-icon maxWidth" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" alt="满五唯一通透户型楼层好有电梯交通便利-天津新梅江锦秀里二手房" title="新梅江锦秀里">
        <span></span>
                      <div class="vr_animation_logo vr_gold_animation_logo"></div>
                                <div class="vr_zhuangxiu VIEWDATA" data-view-evtid="26532" data-view-event="ItemExpo" data-vrzx="https://open.realsee.com/ke/vLykj3Nqj1dDrG06/jv9ze7JwN5yCjhehoTjlke1SB8gZKpxk/?mode=codecoration&split=1&feedback=1&defrom=2#lianjia" style="background-image:url('https://vrlab-image4.ljcdn.com/vrframework/release/ue4_decoration_plan/08WqRG3aHv8ZmOgj/vrproc-ue4/render/picture.jpg')">
              <div class="vr_zhuangxiu_word">
                设计效果
              </div>
            </div>
                </div>
      <div class="thumbnail" id="thumbnail2" style="display:  block ">
        <div class="pre"><</div>
        <ul class="smallpic">
                            <li data-src="https://vrlab-image4.ljcdn.com/release/auto3dhd/557782ae4b77b3d9274d5ba1c34b4abb/screenshot/1567654802_1/pc0_94UaLHOYo.jpg?imageMogr2/quality/70/thumbnail/1024x" data-size="1420x800" data-vr="https://open.realsee.com/ke/vLykj3Nqj1dDrG06/jv9ze7JwN5yCjhehoTjlke1SB8gZKpxk/#lianjia">
                    <img src="https://vrlab-image4.ljcdn.com/release/auto3dhd/557782ae4b77b3d9274d5ba1c34b4abb/screenshot/1567654802_1/pc0_94UaLHOYo.jpg?imageMogr2/quality/70/thumbnail/1024x"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                </li>
                                                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg" data-size="1420x800"
                      data-desc="客厅" data-pic="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg" data-size="1420x800"
                      data-desc="客厅" data-pic="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg" data-size="1420x800"
                      data-desc="卧室A" data-pic="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_710,h_400,l_bk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png" data-size="1066x800"
                      data-desc="户型图" data-pic="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_1000,h_750,l_bk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg" data-size="1420x800"
                      data-desc="卧室B" data-pic="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg" data-size="1420x800"
                      data-desc="卧室C" data-pic="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg" data-size="1420x800"
                      data-desc="厨房" data-pic="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                <li data-src="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg" data-size="1420x800"
                      data-desc="卫生间A" data-pic="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
                      <img src="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"  alt="满五唯一通透户型楼层好有电梯交通便利" title="新梅江锦秀里户型图实景图">
                  </li>
                                </ul>
        <div class="next">></div>
      </div>
        <div class="trueHouse">
            <a class="icon" href="https://rule.ke.com/#/promise/detail?busiType=1&id=76425" target="_blank">
                <i class="true_icon"></i>
                真实存在，真实在售，真实价格，真实图片，假一赔百元<span class="icon-info"></span>
            </a>
            <span class="report CLICKDATA" data-sourcenum="1" data-type="true" data-click-evtid="11444" data-click-event="WebClick"
                      data-action="source_type=详情页_假一赔百举报入口&housedel_id=101118681080&housedel_source=30201">我要举报</span>        </div>
          </div>
    <div class="content">
      <div class="publisher">
         
          <div class="publisher-org ke-agent-sj-sdk component-agent-id-100011449 VIEWDATA" data-view-evtid="13750" data-view-event="ItemExpo"></div>
        
      </div>
      <span class="sharethis" data-qrcode="/api/gethouseqr?hid=101118681080"><i></i>分享此房源</span>
      <div class="price-container">
        <!-- 价格 -->
        <div class="price ">
                      <span class="total">538</span>
            <span class="unit">
              <span>万</span>
            </span>
                    <div class="text">
            <div class="unitPrice">
                          <span class="unitPriceValue">37050</span>
              <i>元/平米</i>
                        </div>
            <div 
              class="VIEWDATA tax showMiniAppQrcode" 
              data-adid="100013157" 
              data-housecode="101118681080"
              data-view-evtid="55828" 
              data-view-event="Module_View"
              data-action="housedel_id=101118681080"
              data-qrevtid="55829"
            >
              <i></i>
              在线咨询经纪人首付及税费
            </div>
          </div>
          <div class="removeIcon"></div>
          
          <!-- 深圳核验码 -->
          
          <!-- 鼠标悬停 -->
          <div class="all-text">
            <p class="text"></p>
          </div>

        </div>

        <!-- 深圳核验码合规 -->
              </div>
      
            <div class="houseInfo">
        <div class="room">
          <div class="mainInfo">3室1厅</div>
          <div class="subInfo">高楼层/共30层</div>
        </div>
        <div class="type">
          <div class="mainInfo" title="南">南</div>
          <div class="subInfo">平层/其他</div>
        </div>
        <div class="area">
          <div class="mainInfo">145.21平米</div>
          <div class="subInfo noHidden">板楼
                      </div>
        </div>
              </div>
      <div class="aroundInfo">
        <div class="communityName">
          <span class="label">小区名称</span>
                      <a href="/xiaoqu/1211063460197/" class="info no_resblock_a" title="新梅江锦秀里二手房">新梅江锦秀里</a>
            <a href="#around" class="map">地图</a>
                  </div>
        <div class="areaName">
          <span class="label">所在区域</span>
          <span class="info">
                          <a href="/ershoufang/hexi/" target="_blank">河西</a>
            &nbsp;
            <a href="/ershoufang/xinmeijiang/" target="_blank">新梅江</a>&nbsp;
            
          </span>
          <a href="" class="supplement" title="" style="color:#101D37;"></a>
        </div>
        <div class="visitTime">
          <span class="label">看房时间</span>
          <span class="info">可看时间请咨询经纪人</span>
        </div>
        <div class="houseRecord">
          <span class="label">贝壳编号</span>
          <span class="info">101118681080
                          <span class="jubao">
                <a href="javascript:;" class="report CLICKDATA" data-sourcenum="3" data-click-evtid="11450" data-click-event="WebClick"
                     data-action="source_type=详情页_底部举报入口&housedel_id=101118681080&housedel_source=30201">举报</a>
                <a href="//www.ke.com/zhuanti/pfgz" target="blank" class="detail"></a>
              </span>               </span>
        </div>
        <div class="danger-layout">
          <span class="label">风险提示</span>
          <span class="danger-notice">贝壳用户风险提示</span>
        </div>
              </div>
              <div class="brokerInfo ke-agent-sj-sdk component-agent-id-100000144"
             id="zuanzhan"
             data-source-type="二手房详情页_钻展"
             data-agent-info='{"tags":null,"school":"\u5929\u6d25\u8f7b\u5de5\u804c\u4e1a\u6280\u672f\u5b66\u9662","seniority":"1-2\u5e74","responseRate":1,"imRate":0,"phoneRate":1,"imQualified":1,"phoneQualified":1,"allVisitCount":8,"allDealCount":5,"feedbackScore":5,"commentCount":168,"majorBizcircle":"\u65b0\u6885\u6c5f","majorDistrict":"\u6cb3\u897f","allCustomerCount":131,"answerCount":0,"usefulAnswerCount":0,"vipLevel":0,"politicalCode":"9","politicalName":"","politicalImg":null,"source":"MEMBER","ucId":"1000000030031782","userCode":"30031782","reason":null,"agentMark":null,"houseRole":null,"digV":"{\"u\":1000000030031782,\"v\":\"V3\",\"s\":\"MEMBER\",\"adId\":100000144,\"flow\":\"commerce\",\"b\":\"CommerceSynthesizeMEMBERBuilder\",\"p\":\"\",\"g\":\"ab767-1096-3489\",\"sid\":\"10000000300317821211063460197200002_20780099\",\"rid\":\"7018217959563280449\"}","flowType":"commerce","proofComplete":false,"port":"shangyehua_ershou_pc_zhanwei_zuanzhan","name":"\u9a86\u8273\u4e3d","agentDomain":"OTHER","avatar":"https:\/\/img.ljcdn.com\/usercenter\/images\/uc_ehr_avatar\/1f9262ea-5de4-4d19-bf28-e4f40cff8ef5.jpg.480x640.jpg","mobileType":"AGENT","mobile":"","brand":"\u5fb7\u4f51","jobTitle":"\u9ad8\u7ea7\u5e97\u7ecf\u7406","positionCode":"785","positionName":"\u7efc\u5408\u7ecf\u7eaa\u4eba","officeAddress":"120000","officeAddressName":"\u5929\u6d25","compName":"\u5929\u6d25\u5fb7\u4f51","compFullName":"\u5929\u6d25\u5fb7\u4f51","resblockId":null,"bizcircleId":null,"stationId":null,"houseCode":null,"houseId":null,"style":null,"agentToken":"1754554490444558337","shopCode":"TJ_14_1204439","shopName":"\u805a\u661f\u67cf\u7fe0\u56ed\u65d7\u8230\u5e97-\u4e00\u5e97","rentApartmentAgentType":null,"dianpuUrl":"https:\/\/dianpu.ke.com\/1000000030031782?_referSource=100000144&houseCode=101118681080","primaryProof":[],"proofListWithSort":[{"no":"30620201012100000746","creditScore":"","img":"https:\/\/image1.ljcdn.com\/ehr-personnel\/20190108180804890B5IW0ZJU.png","creditGrade":"","creditGradeUrl":"","title":"\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u8bc1","type":2,"jumpQueryUrl":"","originUrl":"","creditEvaluate":"","extField":"","verify":1,"verifyUrl":"","desc":"\u6301\u6709\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u804c\u4e1a\u8d44\u683c\u8bc1\u3002\r\n\u7531\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u9881\u53d1\u4eba\u529b\u8d44\u6e90\u793e\u4f1a\u4fdd\u969c\u90e8\u3001\u4f4f\u623f\u57ce\u4e61\u5efa\u8bbe\u90e8\u76d1\u5236\uff0c\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u7528\u5370\u7684\u76f8\u5e94\u7ea7\u522b\u300a\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4e13\u4e1a\u4eba\u5458\u804c\u4e1a\u8d44\u683c\u8bc1\u4e66\u300b\u5728\u5168\u56fd\u8303\u56f4\u6709\u6548\u3002"},{"img":"https:\/\/img.ljcdn.com\/ehr-personnel\/2297cf3c-d718-45cc-bf03-f8e449cad4e5.jpg","creditEvaluate":"","creditGradeUrl":"","title":"\u8d39\u7387","type":-100,"desc":"","jumpQueryUrl":""}],"agentProofList":[{"no":"30620201012100000746","creditScore":"","img":"https:\/\/image1.ljcdn.com\/ehr-personnel\/20190108180804890B5IW0ZJU.png","creditGrade":"","creditGradeUrl":"","title":"\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u8bc1","type":2,"jumpQueryUrl":"","originUrl":"","creditEvaluate":"","extField":"","verify":1,"verifyUrl":"","desc":"\u6301\u6709\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u804c\u4e1a\u8d44\u683c\u8bc1\u3002\r\n\u7531\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u9881\u53d1\u4eba\u529b\u8d44\u6e90\u793e\u4f1a\u4fdd\u969c\u90e8\u3001\u4f4f\u623f\u57ce\u4e61\u5efa\u8bbe\u90e8\u76d1\u5236\uff0c\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u7528\u5370\u7684\u76f8\u5e94\u7ea7\u522b\u300a\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4e13\u4e1a\u4eba\u5458\u804c\u4e1a\u8d44\u683c\u8bc1\u4e66\u300b\u5728\u5168\u56fd\u8303\u56f4\u6709\u6548\u3002"},{"img":"https:\/\/img.ljcdn.com\/ehr-personnel\/2297cf3c-d718-45cc-bf03-f8e449cad4e5.jpg","creditEvaluate":"","creditGradeUrl":"","title":"\u8d39\u7387","type":-100,"desc":"","jumpQueryUrl":""}],"orgProofList":null,"levelLabel":"\u661f\u5149\u7ecf\u7eaa\u4eba","levelLabelUrl":"https:\/\/image1.ljcdn.com\/baikeimg\/898d7b42422767de8fd43eaf9fe395fc0f49746f.png","specialtyList":["\u8d1d\u58f3\u5206\u4f18\u79c0","\u5ba2\u6237\u63a8\u8350\u524d10%"],"phone400":"4000326815-4808","usefulCount":0,"showingCount":0,"lastShowingTime":null,"qrCodeUrl":null,"sellProperty":{"anchorProperty":[],"allDealCount":5,"allVisitCount":8},"rentProperty":{"allDealCount":53,"allVisitCount":0},"nhProperty":{"anchorProperty":{"level":"","name":""},"lastThirtyCust":6,"lastThirtyVisit":4,"allDealCount":1,"nhKeQualityLevel":0,"allVisitCount":4,"nhExcellentAgentTag":0,"nhKeQuality":0},"keQuality":415,"brandCode":"3","agentLicenseCode":null,"agentLicenseExt":null,"agentLicensePcExt":null,"qualityRank":null,"v5Rank":null,"extAgentProofMap":null,"extAgentProofTitleMap":{"creditGradeTitle":"\u4fe1\u7528\u7b49\u7ea7:","descTitle":"\u8bc1\u4ef6\u8bf4\u660e:","creditScoreTitle":"\u4fe1\u7528\u8bc4\u5206:","originUrlTitle":"\u67e5\u770b\u8be6\u60c5","noTitle":"\u8bc1\u4ef6\u7f16\u53f7:"},"paramTagList":["commerceMemberLevel1"],"isFjh":0,"orgCode":"TJ_15_1204440","orgName":"\u805a\u661f\u67cf\u7fe0\u56ed\u65d7\u8230\u5e97-\u4e00\u5e97\u4e00\u7ec4","exposureNum":null,"cityName":null,"agentName":null,"cityCode":null,"nhExpectSjScore":null,"originalNhExpectSjScore":null,"nhExpectCalcMode":null,"locationId":null,"locationType":null}'
             data-fb-expo-id="806996103652151297">
            <style>.ke-agent-sj-sdk { 
  width: 100%
} 
.ke-agent-sj-sdk-f-0 {
  font-size: 0 
} 
.ke-agent-sj-clear { 
  clear: both 
} 
.component-agent-es-pc-2 { 
  -webkit-user-select: none; 
  -moz-user-select: none; 
  -ms-user-select: none;
  user-select: none;
  position: relative
} 
.component-agent-es-pc-2 .ke-agent-sj-container { 
  width: 400px 
} 
.component-agent-es-pc-2 .ke-agent-sj-fl { 
  float: left 
} 
.component-agent-es-pc-2 .ke-agent-sj-fr { 
  float: right;
} 
.component-agent-es-pc-2 .ke-agent-sj-avatar { 
  display: block; 
  width: 80px; 
  height: 80px; 
  -webkit-border-radius: 50%; 
  border-radius: 50%; 
  overflow: hidden
} 
.component-agent-es-pc-2 .ke-agent-sj-avatar img { 
  width: 100%; height: auto 
} 
.component-agent-es-pc-2 .ke-agent-sj-avatar .ke-agent-sj-avatar-label {
  position: absolute;
  display: block; 
  width: 55px;
  width: 3.4375rem; 
  height: auto; 
  bottom: 0; 
  left: 50%;
  -webkit-transform: translateX(-50%); 
  -ms-transform: translateX(-50%); 
  transform: translateX(-50%)
} 
.component-agent-es-pc-2 .ke-agent-sj-info { 
  width: 300px; 
  margin-top: 6px; 
  line-height: 1; 
  font-size: 12px;
  position: relative;
} 
.component-agent-es-pc-2 .ke-agent-sj-name { 
  vertical-align: middle; 
  font-size: 18px;
  font-weight: 700;
  color: #101d37;
  margin-right: 8px;
  max-width: 140px; 
  display: inline-block; 
  white-space: nowrap; 
  overflow: hidden;
  -o-text-overflow: ellipsis; 
  text-overflow: ellipsis; 
  line-height: 20px;
  cursor: pointer 
} 
.component-agent-es-pc-2 .ke-agent-sj-name:hover {
  text-decoration: underline 
} 
.component-agent-es-pc-2 .ke-agent-sj-profile-card { 
  display: inline-block; 
  margin: 0 3px;
  cursor: pointer 
} 
.component-agent-es-pc-2 .ke-agent-sj-profile-card img { 
  position: relative;
  display: inline-block; 
  width: 24px; 
  height: 18px;
  vertical-align: middle;
  background: #f5f5f6
} 
.component-agent-es-pc-2 .ke-agent-sj-tag { 
  background-color: #f4f7f9; 
  color: #849aae;
  height: 18px; 
  line-height: 18px;
  display: inline-block; 
  padding: 0 4px;
  -webkit-border-radius: 2px;
  border-radius: 2px; 
  max-width: 100px;
  font-size: 12px 
} 
.component-agent-es-pc-2 .ke-agent-sj-desc, .component-agent-es-pc-2 .ke-agent-sj-tag { 
  vertical-align: middle;
  white-space: nowrap; 
  overflow: hidden; 
  -o-text-overflow: ellipsis; 
  text-overflow: ellipsis 
} 
.component-agent-es-pc-2 .ke-agent-sj-desc { 
  font-size: 12px;
  color: #000; 
  letter-spacing: 0; 
  line-height: 12px; 
  padding: 7px 0 9px 0;
} 
.component-agent-es-pc-2 .ke-agent-sj-gr-info { 
  background: rgba(48,114,246,0.05);
  color: #999;
  font-size: 12px;
}

.component-agent-es-pc-2 .ke-agent-sj-gr-info div{
  margin: 8px 0;
  padding: 10px;
}
.component-agent-es-pc-2 .ke-agent-sj-gr-info div:nth-child(2){
  padding-top: 0;
}
.component-agent-es-pc-2 .ke-agent-sj-gr-info div span{
  color: #222;
      /* overflow: hidden;
    white-space: nowrap;
    -o-text-overflow: ellipsis;
    text-overflow: ellipsis;
    display: inline-block;
    max-width: 66px; */
}
.component-agent-es-pc-2 .ke-agent-sj-gr-info div a{
  color: #3072F6;
}



.component-agent-es-pc-2 .ke-agent-sj-gr-img{
  display: inline-block;
    width: 56px;
    height: 24px;
    background-size: 100%;
    text-align: center;
    color: #222;
    font-size: 12px;
    position: relative;
    line-height: 27px;
    padding-left: 15px;
    box-sizing: border-box;
    background-repeat: no-repeat;
}
.component-agent-es-pc-2 .ke-agent-sj-gr-img-des{
    width: 145px;
    height: 24px;
    display: inline-block;
    margin: 10px 0;
}
.component-agent-es-pc-2 .ke-agent-sj-gr-img-des img{
  width: 100%;
  height: 100%;
}
.component-agent-es-pc-2 .ke-agent-sj-im { 
  width: 118px;
  height: 44px;
  line-height: 44px; 
  text-align: center;
  float: right; 
  background: #f4f8fe;
  border: 1px solid #4688f1; 
  -webkit-border-radius: 2px; 
  border-radius: 2px;
  font-size: 14px;
  color: #4688f1; 
  text-decoration: none; 
  cursor: pointer 
} 
.component-agent-es-pc-2 .ke-agent-sj-im .message-icon { 
  padding: 0;
  margin-right: 8px; 
  vertical-align: -3px; 
  width: 16px; 
  height: 16px
} 
.component-agent-es-pc-2 .mr-8 { 
  float: right;
  display: block;
  width: 8px; 
  height: 46px; 
  background: #fff
} 
.component-agent-es-pc-2 .ke-agent-sj-phone { 
  background: #3072f6; 
  -webkit-border-radius: 2px;
  border-radius: 2px; 
  min-width: 252px; 
  height: 46px;
  line-height: 46px; 
  text-align: center;
  font-size: 18px; 
  color: #fff; 
  font-weight: 700 
} 
.component-agent-es-pc-2 .ke-agent-sj-phone span {
  font-size: 14px; 
  padding: 0 4px; 
  line-height: 20px 
} 
.component-agent-es-pc-2 .ke-agent-sj-top {
  height: 60px
}
.component-agent-es-pc-2 .ke-agent-sj-bottom { 
  margin-top: 10px
}
.ke-agent-sj-code {
font-family: PingFangSC-Regular;
font-size: 14px;
color: #101D37;
letter-spacing: 0;
text-align: justify;
  vertical-align: -webkit-baseline-middle;
}
.ke-agent-sj-ext {
  opacity: 1;
  font-size: 12px;
  font-family: PingFangSC, PingFangSC-Regular;
  font-weight: 400;
  text-align: left;
  color: #999999;
  line-height: 14px;
  margin-left: 80px;
  max-width: 300px;
  word-break: break-all;
  margin-top:5px;
}</style> <div style="width: 0;height: 0;" class="ke-agent-data" data-agent='{"agentDomain":"OTHER","agentProofList":[{"no":"30620201012100000746","creditScore":"","img":"https://image1.ljcdn.com/ehr-personnel/20190108180804890B5IW0ZJU.png","creditGrade":"","creditGradeUrl":"","title":"全国房地产经纪人协理证","type":2,"jumpQueryUrl":"","originUrl":"","creditEvaluate":"","extField":"","verify":1,"verifyUrl":"","desc":"持有全国房地产经纪人协理职业资格证。\r\n由中国房地产估价师与房地产经纪人学会颁发人力资源社会保障部、住房城乡建设部监制，中国房地产估价师与房地产经纪人学会用印的相应级别《中华人民共和国房地产经纪专业人员职业资格证书》在全国范围有效。"},{"img":"https://img.ljcdn.com/ehr-personnel/2297cf3c-d718-45cc-bf03-f8e449cad4e5.jpg","creditEvaluate":"","creditGradeUrl":"","title":"费率","type":-100,"desc":"","jumpQueryUrl":""}],"agentToken":"1754554490444558337","allCustomerCount":131,"allDealCount":5,"allVisitCount":8,"answerCount":0,"avatar":"https://img.ljcdn.com/usercenter/images/uc_ehr_avatar/1f9262ea-5de4-4d19-bf28-e4f40cff8ef5.jpg.480x640.jpg","brand":"德佑","brandCode":"3","commentCount":168,"compFullName":"天津德佑","compName":"天津德佑","dianpuUrl":"https://dianpu.ke.com/1000000030031782?_referSource=100000144&houseCode=101118681080","digV":"{\"u\":1000000030031782,\"v\":\"V3\",\"s\":\"MEMBER\",\"adId\":100000144,\"flow\":\"commerce\",\"b\":\"CommerceSynthesizeMEMBERBuilder\",\"p\":\"\",\"g\":\"ab767-1096-3489\",\"sid\":\"10000000300317821211063460197200002_20780099\",\"rid\":\"7018217959563280449\"}","extAgentProofTitleMap":{"creditGradeTitle":"信用等级:","descTitle":"证件说明:","creditScoreTitle":"信用评分:","originUrlTitle":"查看详情","noTitle":"证件编号:"},"feedbackScore":5.0,"flowType":"commerce","imQualified":1,"imRate":0.0,"isFjh":0,"jobTitle":"高级店经理","keQuality":415,"levelLabel":"星光经纪人","levelLabelUrl":"https://image1.ljcdn.com/baikeimg/898d7b42422767de8fd43eaf9fe395fc0f49746f.png","majorBizcircle":"新梅江","majorDistrict":"河西","mobile":"","mobileType":"AGENT","name":"骆艳丽","nhProperty":{"anchorProperty":{"level":"","name":""},"lastThirtyCust":6,"lastThirtyVisit":4,"allDealCount":1,"nhKeQualityLevel":0,"allVisitCount":4,"nhExcellentAgentTag":0,"nhKeQuality":0},"officeAddress":"120000","officeAddressName":"天津","orgCode":"TJ_15_1204440","orgName":"聚星柏翠园旗舰店-一店一组","paramTagList":["commerceMemberLevel1"],"phone400":"4000326815-4808","phoneQualified":1,"phoneRate":1.0,"politicalCode":"9","politicalName":"","port":"shangyehua_ershou_pc_zhanwei_zuanzhan","positionCode":"785","positionName":"综合经纪人","primaryProof":{},"proofComplete":false,"proofListWithSort":[{"$ref":"$.agentProofList[0]"},{"$ref":"$.agentProofList[1]"}],"rentProperty":{"allDealCount":53,"allVisitCount":0},"responseRate":1.0,"school":"天津轻工职业技术学院","sellProperty":{"anchorProperty":{},"allDealCount":5,"allVisitCount":8},"seniority":"1-2年","shopCode":"TJ_14_1204439","shopName":"聚星柏翠园旗舰店-一店","showingCount":0,"source":"MEMBER","specialtyList":["贝壳分优秀","客户推荐前10%"],"ucId":"1000000030031782","usefulAnswerCount":0,"usefulCount":0,"userCode":"30031782","vipLevel":0}'>
</div>
<div class="component-agent-es-pc-2">
  <div class="ke-agent-sj-container">
    <div class="ke-agent-sj-top">
      <div class="ke-agent-sj-fl"><a href="https://dianpu.ke.com/1000000030031782?_referSource=100000144&houseCode=101118681080"
          class="ke-agent-sj-avatar ke-agent-sj-avatar-100000144 ke-agent-sj-avatar-1000000030031782">
          <img src="https://img.ljcdn.com/usercenter/images/uc_ehr_avatar/1f9262ea-5de4-4d19-bf28-e4f40cff8ef5.jpg.480x640.jpg" alt="骆艳丽">
          </a>
       </div>
      <div class="ke-agent-sj-fr">
        <div class="ke-agent-sj-info">
                <a class="ke-agent-sj-name ke-agent-sj-name-100000144 ke-agent-sj-name-1000000030031782"
            title="骆艳丽" href="https://dianpu.ke.com/1000000030031782?_referSource=100000144&houseCode=101118681080" target="_blank"> 骆艳丽 </a>

                    <div class="ke-agent-sj-tag ke-agent-sj-tag-100000144 ke-agent-sj-tag-1000000030031782"> 德佑
            </div>          </div>
                         <div class="ke-agent-sj-gr-info">
                	            
        </div>
      </div>
     
    </div>
     <div class="ke-agent-sj-clear"></div>
        <div class="ke-agent-sj-sdk-f-0 ke-agent-sj-bottom"><a
        class="ke-agent-sj-im ke-agent-sj-im-100000144 ke-agent-sj-im-1000000030031782" data-bl="agentim"
        data-ucid="1000000030031782" data-source-port="shangyehua_ershou_pc_zhanwei_zuanzhan"
        data-source-extends='app_data={"business_dig_v":{"u":1000000030031782,"v":"V3","s":"MEMBER","adId":100000144,"flow":"commerce","b":"CommerceSynthesizeMEMBERBuilder","p":"","g":"ab767-1096-3489","sid":"10000000300317821211063460197200002_20780099","rid":"7018217959563280449"}}'><img
          src="https://s1.ljcdn.com/pegasus/redskull/images/ershoufang/im-chart@2x.png" class="message-icon" /> 在线问
      </a>
      <div class="mr-8"></div>
      <div class="ke-agent-sj-phone "> 4000326815 <span> 转 </span> 4808 </div>
    </div>
  </div>
</div> 
        </div>
      
      <div class="download">
        <div class="qr-code">
          <img width="94" height="94"
               src="https://ajax.api.ke.com/qr/getDownloadQr?location=right&ljweb_channel_key=ershoufang_view"
               alt="下载贝壳找房APP">
          <span class="text">扫描下载APP 随时查看新房源</span>
        </div>
      </div>
    </div>
  </div>


<div class="danger-botice-bg">
  <div class="danger-container">
    <div class="head-layout">
      <div class="head-content">
        <h3>风险提示</h3>
      </div>
      <div class="danger-icon"></div>
      <div class="danger-close"></div>
    </div>
    <div class="desc-layout">
      <div class="danger-desc">
      本站旨在为广大用户提供更丰富的信息，但由于部分信息通过技术手段生成，部分信息由第三方提供，我们持续通过技术和管理手段提升信息的准确度，但<b>我们无法确保信息的真实性、准确性和完整性。房产交易兹事体大，本站信息不应作为您买卖决策的依据，您决策前应与房源业主核实相关信息、并亲自到房屋中核验信息，或以产权证明、政府类网站发布的官方信息为准。本站不对您交易过程中对本网站信息产生的依赖承担任何明示或默示的担保责任或任何责任。</b>
      </div>
      <div class="danger-start">请您详细阅读如下声明：</div>
      <ul>
        <li>
          <div>1、关于参考户型图</div>
          <p>本网呈现的户型图为平台根据已拍摄的VR内容/数据绘制而成的非标准的参考户型图，其中户型结构及房屋面积并非按国家标准进行的测绘专业活动取得，我们会持续改进技术，但因为设备、技术、摄影师人为操作偏差等原因，参考户型图与真实现状一定存在差异，我们无法保障户型图准确性和差异率，<b>户型图仅供参考，不应作为您交易的决策依据，房屋面积的准确信息请您与房源业主核实，并请以产权证明或您委托的专业机构测量结果为准。</b></p>
        </li>
        <li>
          <div>2、关于房屋装修情况</div>
          <p>本网房源图片、VR效果图、视频等呈现出的房屋装修情况可能因为拍摄时间、拍摄角度等原因和实际场景存在出入,<b>仅供参考，不应作为您交易的决策依据，请以您在看房时房源的实际装修情况为准。</b></p>
        </li>
        <li>
          <div>3、关于房屋情况</div>
          <p>本网展示的房源信息、交易信息等（包括但不限于房屋面积、所在楼层、房屋朝向、房屋用途、建成年代、建筑结构、供暖方式、抵押信息、交易权属）由经纪人提供，<b>仅供参考不应作为您交易的决策依据，房源的准确信息请您与房源业主核实，并以房本信息、房屋实际情况、您签订房屋买卖合同中披露的信息为准。</b></p>
        </li>
        <li>
          <div>4、关于房屋周边配套等</div>
          <p>房源介绍中的周边配套、在建设施、规划设施、地铁信息、绿化率、得房率等内容均系第三方提供，<b>仅供参考不应作为您交易的决策依据，房屋周边配套请您与房源业主及主管部门核实，并以房本信息、房屋实际情况、您签订房屋买卖合同中披露的信息为准。</b></p>
        </li>
        <li>
          <div>5、关于距离</div>
          <p>房源介绍中与距离相关的数据均来源于百度地图。</p>
        </li>
      </ul>
    </div>
  </div>
</div>
</div>

    <div class="m-content">
                  <!-- 基本信息 -->
      <div class="newwrap baseinform" id="introduction" data-component="baseinfo">
    <div class="" style="width:700px;">
        <h2>
            <div class="title">房源基本信息</div>
        </h2>
        <div class="introContent">
            <div class="base">
                <div class="name">基本属性</div>
                <div class="content">
                    <ul>
                                                    <li class="  ">
                                <span class="label">房屋户型</span>
                                3室1厅2卫
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">建筑面积</span>
                                145.21㎡
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">户型结构</span>
                                平层
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">建筑类型</span>
                                板楼
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">所在楼层</span>
                                高楼层 (共30层)
                                                                    <span 
                                        class="VIEWDATA link showMiniAppQrcode" 
                                        data-adid="100013158" 
                                        data-housecode="101118681080"
                                        data-view-evtid="55831" 
                                        data-view-event="Module_View"
                                        data-action="housedel_id=101118681080"
                                        data-qrevtid="55832"
                                    >咨询楼层</span>
                                                                                                                            </li>
                                                    <li class="  louceng">
                                <span class="label">楼层高度</span>
                                暂无数据
                                                                                                                                    <span class="icon-box">
                                        <span class="icon-img">
                                            <img src="https://file.ljcdn.com/nebula/ershou/icon_1703726020004.png"/>
                                        </span>
                                        <span class="tips">
                                            <p>实际层高需现场测量，具体数据以实际测量为准</p>
                                            <span class="tips-icon"></span>
                                        </span>
                                    </span>
                                                            </li>
                                                    <li class="oneline  ">
                                <span class="label">套内面积</span>
                                暂无
                                                                                                    <span 
                                        class="VIEWDATA link showMiniAppQrcode" 
                                        data-adid="100013159" 
                                        data-housecode="101118681080"
                                        data-view-evtid="55833" 
                                        data-view-event="Module_View"
                                        data-action="housedel_id=101118681080"
                                        data-qrevtid="55834"
                                    >咨询套内面积</span>
                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">房屋朝向</span>
                                南
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">建筑结构</span>
                                钢混结构
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">装修情况</span>
                                其他
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">梯户比例</span>
                                两梯四户
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">供暖方式</span>
                                集中供暖
                                                                                                                            </li>
                                                    <li class="  ">
                                <span class="label">配备电梯</span>
                                有
                                                                                                                            </li>
                                            </ul>
                </div>
            </div>
            <div class="transaction">
                <div class="name">交易属性</div>
                <div class="content">
                    <ul>
                                                                                                                        <li class=""><span class="label ">挂牌时间</span>2023年04月02日
                                                                            </li>
                                                                                                                                                                                    <li class=""><span class="label ">交易权属</span>商品房
                                                                            </li>
                                                                                                                                                                                    <li class=""><span class="label ">上次交易</span>2018年12月21日
                                                                            </li>
                                                                                                                                                                                    <li class=""><span class="label ">房屋用途</span>普通住宅
                                                                            </li>
                                                                                                                                                                                    <li class=""><span class="label ">房屋年限</span>满五年
                                                                            </li>
                                                                                                                                                                                    <li class=""><span class="label ">产权所属</span>非共有
                                                                            </li>
                                                                                                                                                <li><span class="label">抵押信息</span><span
                                        style="display:inline-block;width:64%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;vertical-align:middle;"
                                        title="无抵押">无抵押</span></li>
                                                                                                                                                    <li class=""><span class="label ">房本备件</span>已上传房本照片
                                                                            </li>
                                                                                                        </ul>
                </div>
            </div>

            <div class="disclaimer" style="padding-top: 10px;">特别提示：本房源所示信息仅供参考，购房时请以该房屋档案登记信息、产权证信息以及所签订合同条款约定为准；本房源公示信息不做为合同条款，不具有合同约束力。</div>

        </div>
    </div>
</div>
      <!-- 周边配套 -->
        <div data-component="aroundMap" class="around" id="around" data-question='{"education":{"kindergarten":[{"isHot":1,"title":"\u5927\u5bb6\u4e00\u822c\u90fd\u4e0a\u54ea\u4e2a\u5e7c\u513f\u56ed\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c45\u6c11\u4e00\u822c\u4e0a\u54ea\u4e2a\u5e7c\u513f\u56ed\uff1f"},{"isHot":0,"title":"\u516c\u7acb\u5e7c\u513f\u56ed\u6709\u51e0\u6240\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u516c\u7acb\u5e7c\u513f\u56ed\u6709\u51e0\u6240\uff1f"}],"primary-school":[{"isHot":0,"title":"\u5927\u5bb6\u4e00\u822c\u90fd\u4e0a\u54ea\u4e2a\u5c0f\u5b66\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c45\u6c11\u4e00\u822c\u4e0a\u54ea\u4e2a\u5c0f\u5b66\uff1f"},{"isHot":0,"title":"\u5c0f\u5b66\u5165\u5b66\u653f\u7b56\u662f\u4ec0\u4e48\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c0f\u5b66\u5165\u5b66\u653f\u7b56\u662f\u4ec0\u4e48\uff1f"}],"middle-school":[{"isHot":0,"title":"\u5927\u5bb6\u4e00\u822c\u90fd\u4e0a\u54ea\u4e2a\u4e2d\u5b66\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c45\u6c11\u4e00\u822c\u4e0a\u54ea\u4e2a\u4e2d\u5b66\uff1f"},{"isHot":0,"title":"\u4e2d\u5b66\u5165\u5b66\u653f\u7b56\u662f\u4ec0\u4e48\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u4e2d\u5b66\u5165\u5b66\u653f\u7b56\u662f\u4ec0\u4e48\uff1f"}],"University":[{"isHot":0,"title":"\u5927\u5bb6\u4e00\u822c\u90fd\u4e0a\u54ea\u6240\u5b66\u6821\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c45\u6c11\u4e00\u822c\u4e0a\u54ea\u6240\u5b66\u6821\uff1f"},{"isHot":0,"title":"\u5468\u8fb9\u6559\u80b2\u8d28\u91cf\u600e\u4e48\u6837\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5468\u8fb9\u6559\u80b2\u8d28\u91cf\u600e\u4e48\u6837\uff1f"}]},"traffic":{"subway":[{"isHot":1,"title":"\u4e0a\u4e0b\u73ed\u65f6\u95f4\u5730\u94c1\u4eba\u591a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u4e0a\u4e0b\u73ed\u65f6\u95f4\u5730\u94c1\u4eba\u591a\u5417\uff1f"},{"isHot":0,"title":"\u6253\u8f66\u65b9\u4e0d\u65b9\u4fbf\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u6253\u8f66\u65b9\u4e0d\u65b9\u4fbf\uff1f"}],"bus":[{"isHot":0,"title":"\u4e0a\u4e0b\u73ed\u65f6\u95f4\u516c\u4ea4\u4eba\u591a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u4e0a\u4e0b\u73ed\u65f6\u95f4\u516c\u4ea4\u4eba\u591a\u5417\uff1f"},{"isHot":0,"title":"\u6253\u8f66\u65b9\u4e0d\u65b9\u4fbf\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u6253\u8f66\u65b9\u4e0d\u65b9\u4fbf\uff1f"}]},"medical":{"hospital":[{"isHot":1,"title":"\u5c0f\u533a\u5468\u56f4\u6709\u4e09\u7532\u533b\u9662\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5468\u56f4\u6709\u4e09\u7532\u533b\u9662\u5417\uff1f"},{"isHot":0,"title":"\u5c31\u8fd1\u7684\u513f\u7ae5\u533b\u9662\u662f\u54ea\u4e2a\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c31\u8fd1\u7684\u513f\u7ae5\u533b\u9662\u662f\u54ea\u4e2a\uff1f"}],"pharmacy":[{"isHot":0,"title":"\u5c0f\u533a\u5468\u56f4\u6709\u4e09\u7532\u533b\u9662\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5468\u56f4\u6709\u4e09\u7532\u533b\u9662\u5417\uff1f"},{"isHot":0,"title":"\u836f\u5e97\u53ef\u4ee5\u5237\u533b\u4fdd\u5361\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u836f\u5e97\u53ef\u4ee5\u5237\u533b\u4fdd\u5361\u5417\uff1f"}]},"shopping":{"mall":[{"isHot":1,"title":"\u9644\u8fd1\u6709\u5927\u578b\u5546\u573a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u9644\u8fd1\u6709\u5927\u578b\u5546\u573a\u5417\uff1f"},{"isHot":0,"title":"\u5927\u5bb6\u4eba\u90fd\u53bb\u54ea\u901b\u8857\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c45\u6c11\u90fd\u53bb\u54ea\u901b\u8857\uff1f"}],"supermarket":[{"isHot":0,"title":"\u6709\u5927\u578b\u8d85\u5e02\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u9644\u8fd1\u6709\u5927\u578b\u8d85\u5e02\u5417\uff1f"},{"isHot":0,"title":"\u5927\u5bb6\u90fd\u53bb\u54ea\u4e70\u4e1c\u897f\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u5c45\u6c11\u90fd\u53bb\u54ea\u4e70\u4e1c\u897f\uff1f"}],"market":[{"isHot":0,"title":"\u6709\u5927\u578b\u8d85\u5e02\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u9644\u8fd1\u6709\u5927\u578b\u8d85\u5e02\u5417\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u6709\u83dc\u5e02\u573a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u9644\u8fd1\u6709\u83dc\u5e02\u573a\u5417\uff1f"}]},"life":{"bank":[{"isHot":1,"title":"\u9644\u8fd1\u90fd\u6709\u4ec0\u4e48\u94f6\u884c\uff1f","imText":"\u4f60\u597d\uff0c\u8fd9\u4e2a\u5c0f\u533a\u9644\u8fd1\u6709\u4ec0\u4e48\u94f6\u884c\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}],"atm":[{"isHot":0,"title":"\u9644\u8fd1\u90fd\u6709\u4ec0\u4e48\u94f6\u884c\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u6709\u4ec0\u4e48\u94f6\u884c\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}],"restaurant":[{"isHot":0,"title":"\u9644\u8fd1\u6709\u597d\u5403\u7684\u9910\u5385\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u6709\u597d\u5403\u7684\u9910\u5385\u5417\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}],"coffee":[{"isHot":0,"title":"\u9644\u8fd1\u6709\u597d\u559d\u7684\u5496\u5561\u9986\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u6709\u597d\u559d\u7684\u5496\u5561\u9986\u5417\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}]},"entertainment":{"park":[{"isHot":1,"title":"\u9644\u8fd1\u54ea\u4e2a\u516c\u56ed\u53ef\u4ee5\u905b\u72d7\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u54ea\u4e2a\u516c\u56ed\u53ef\u4ee5\u905b\u72d7\uff1f"},{"isHot":0,"title":"\u5468\u672b\u516c\u56ed\u4eba\u591a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u5468\u672b\u516c\u56ed\u4eba\u591a\u5417\uff1f"}],"gym":[{"isHot":0,"title":"\u5065\u8eab\u623f\u5468\u672b\u4eba\u591a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u5065\u8eab\u623f\u5468\u672b\u4eba\u591a\u5417\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}],"cinema":[{"isHot":0,"title":"\u7535\u5f71\u9662\u5468\u672b\u4eba\u591a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u7535\u5f71\u9662\u5468\u672b\u4eba\u591a\u5417\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}],"sport":[{"isHot":0,"title":"\u4f53\u80b2\u9986\u5468\u672b\u4eba\u591a\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u4f53\u80b2\u9986\u5468\u672b\u4eba\u591a\u5417\uff1f"},{"isHot":0,"title":"\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f","imText":"\u4f60\u597d\uff0c\u9644\u8fd1\u751f\u6d3b\u4fbf\u5229\u5417\uff1f"}]}}'>
    <h2 class="aroundTitle">周边配套</h2>
    <div class="aroundContainer">
      <div class="aroundMap" id="map">
      </div>
      <div class="tabBox">
        <ul class="aroundType">
                    <li class="LOGCLICK" data-log_evtid='10242'  data-bl="education" data-key="幼儿园,小学,中学,大学"
                data-index="kindergarten,primary-school,middle-school,University"
                data-length="10,10,10,10"
            >教育</li>
                    <li class="LOGCLICK" data-log_evtid='10242'  data-bl="traffic" data-key="地铁站,公交站" data-index="subway,bus" data-length="10,10">交通</li>

          <li class="LOGCLICK" data-log_evtid='10242'  data-bl="medical" data-key="医院,药店" data-index="hospital,pharmacy" data-length="10,10">医疗</li>
          <li class="LOGCLICK" data-log_evtid='10242'  data-bl="shopping" data-key="商场,超市,市场" data-index="mall,supermarket,market" data-length="10,10,10">购物</li>
          <li class="LOGCLICK" data-log_evtid='10242'  data-bl="life" data-key="银行,ATM,餐厅,咖啡馆" data-index="bank,atm,restaurant,coffee" data-length="10,10,10,10">生活</li>
          <li class="LOGCLICK" data-log_evtid='10242'  data-bl="entertainment" data-key="公园,电影院,健身房,体育馆" data-index="park,cinema,gym,sport" data-length="10,10,10,10">娱乐</li>
        </ul>
        <div class="itemTagBox"></div>
        <div class="aroundList withQuestion" id="mapListContainer"></div>
        <div class="aroundList-line"></div>
        <div class="aroundQuestion-container ke-agent-sj-sdk component-agent-id-100013160"></div>
        <div class="loading">
          <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/loading.gif?_v=202401081627157" class="loadingImg">
          <span class="loadingText">努力加载中...</span>
        </div>
      </div>
    </div>
  </div>
      <div class="box-l">
        <!-- 房源特色 -->
          <div class="newwrap baseinform" data-component="feature">
    <h2>
      <div class="title" style="margin-top:50px;">本房源特色</div>
    </h2>
    <div class="introContent showbasemore">
              <div class="tags clear">
          <div class="name">房源特色</div>
          <div class="content">
                                          <a class="tag taxfree " href="/ershoufang/hexi/mw1/"
                                    >
                                            满五年
                                    </a>
                                                        <a class="tag isVrFutureHome " href="/ershoufang/hexi/tt10/"
                                    >
                                            VR看装修
                                    </a>
                                                        <a class="tag isNearSubway " href="/ershoufang/hexi/su1/"
                                    >
                                            地铁
                                    </a>
                                    </div>
        </div>
                              <div class="baseattribute clear">
            <div class="name">核心卖点</div>
            <div class="content">
              满五唯一南北户型通透楼层好有电梯交通便利次新房交
            </div>
          </div>
                  <div class="baseattribute clear">
            <div class="name">小区介绍</div>
            <div class="content">
              此小区位于解放南路与浯水道交叉路口处，共有15栋楼，主要以高层为主，楼层在20-30之间，小区内栽种着各种植被，草坪上铺有石板，可供散步使用，同时配备了运动器械，可在工作之余进行简单的锻炼。
            </div>
          </div>
                  <div class="baseattribute clear">
            <div class="name">户型介绍</div>
            <div class="content">
              户型方正格局好采光充足视野无遮挡，室内布局一体化通透敞亮，独立阳台沐浴阳光功能区皆有采光
            </div>
          </div>
                  <div class="baseattribute clear">
            <div class="name">周边配套</div>
            <div class="content">
              小区门口有安保人员24小时值守，社区设施比较完善，生活交通便利，出小区门口就是友谊南路，过马路就是太湖路公园，解放南路有各路公交和地铁6号线。小区内都是小高层，楼间距大
            </div>
          </div>
                <div class="viewmore">展开更多信息</div>
        <div class="disclaimer">注：1.房源介绍中的周边配套、在建设施、规划设施、地铁信息、绿化率、得房率、容积率等信息为通过物业介绍、房产证、实勘、政府官网等渠道获取，因时间、政策会发生变化，与实际情况可能略有偏差，房源介绍仅供参考。 2.房源介绍中与距离相关的数据均来源于百度地图。 3.土地使用起止年限详见业主土地证明材料或查询相关政府部门的登记文件。</div>
          </div>
  </div>
        <!-- 房主自荐 -->
                <!-- 带看记录 -->
          <div data-component="daikan" id="daikanContainer" class="newwrap"></div>
        <!-- 户型分间 -->
          <div class="newwrap" data-component="houseLayout">
    <div class="layout-wrapper" id="layout">
      <div class="layout">
        <h2><div class="title">该户型分间</div></h2>
                  <div class="agent-ad ke-agent-sj-sdk component-agent-type-1 component-agent-id-100000449"
            data-hdic-city-id="120000"
            data-house-code="101118681080"
            data-resblock-id="1211063460197"
                        data-ucid="1000001000901337">
          </div>

          <div class="content">
            <div class="clear"></div>
            <div class="imgdiv" data-img="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_720,h_540,l_bk,f_jpg,ls_30?from=ke.com">
              <img src="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_240,h_180,l_bk,f_jpg,ls_30?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-天津新梅江锦秀里户型图">
              <span class="setbig">
                        <i></i>
                        <label>查看原图</label>
                     </span>
            </div>
            <div class="des">
              <div class="info">
                <div class="list">
                  <div id="infoList">
                                          <div class="row">
                        <div class="col">客厅</div>
                        <div class="col">34.88平米</div>
                        <div class="col">南 北</div>
                        <div class="col">落地窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">卧室A</div>
                        <div class="col">7.2平米</div>
                        <div class="col">北</div>
                        <div class="col">普通窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">卧室B</div>
                        <div class="col">9.84平米</div>
                        <div class="col">南</div>
                        <div class="col">落地窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">卧室C</div>
                        <div class="col">18.73平米</div>
                        <div class="col">南 东</div>
                        <div class="col">落地窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">厨房</div>
                        <div class="col">6.97平米</div>
                        <div class="col">北</div>
                        <div class="col">普通窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">卫生间A</div>
                        <div class="col">5.14平米</div>
                        <div class="col">北</div>
                        <div class="col">普通窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">卫生间B</div>
                        <div class="col">4.5平米</div>
                        <div class="col">北</div>
                        <div class="col">普通窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">阳台A</div>
                        <div class="col">3.47平米</div>
                        <div class="col">南 东</div>
                        <div class="col">落地窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">阳台B</div>
                        <div class="col">2.94平米</div>
                        <div class="col">北</div>
                        <div class="col">普通窗</div>
                      </div>
                                          <div class="row">
                        <div class="col">阳台C</div>
                        <div class="col">1.95平米</div>
                        <div class="col">南 东</div>
                        <div class="col">落地窗</div>
                      </div>
                                      </div>
                </div>
              </div>
            </div>
            <span class="justify_fix"></span>
            <p class="disclaimer">
              注：户型图标注的面积不同于房本面积，是实地测量后计算的地板面积，存在测量误差，购房请以房本面积为准。            </p>
          </div>
                        </div>
      <div class="layoutpicbg"></div>
      <div class="layoutpic">
        <img src="" alt="" class="pic-img fl"> <span class="closepic">×</span>
        <div class="fr list">
          <div class="title">
            <b>户型分间</b>
                                          <p>
                  <span>户型特色</span>
                                      客厅朝南、                                      全明格局、                                      南北通透、                                      观景落地窗、                                      卧室朝南、                                      卧室带卫、                                      动静分区、                                      卧室带阳台、                                      明厨、                                      明卫、                                      客厅带阳台、                                      卧室有落地窗                                  </p>
                                    </div>
          <div class="lists">
            <ul id="layoutList">
                                                <li>
                    <span class="col-1">客厅</span>
                    <span class="col-2">34.88平米</span>
                    <span class="col-3">南 北</span>
                    <span class="col-4">落地窗</span>
                  </li>
                                  <li>
                    <span class="col-1">卧室A</span>
                    <span class="col-2">7.2平米</span>
                    <span class="col-3">北</span>
                    <span class="col-4">普通窗</span>
                  </li>
                                  <li>
                    <span class="col-1">卧室B</span>
                    <span class="col-2">9.84平米</span>
                    <span class="col-3">南</span>
                    <span class="col-4">落地窗</span>
                  </li>
                                  <li>
                    <span class="col-1">卧室C</span>
                    <span class="col-2">18.73平米</span>
                    <span class="col-3">南 东</span>
                    <span class="col-4">落地窗</span>
                  </li>
                                  <li>
                    <span class="col-1">厨房</span>
                    <span class="col-2">6.97平米</span>
                    <span class="col-3">北</span>
                    <span class="col-4">普通窗</span>
                  </li>
                                  <li>
                    <span class="col-1">卫生间A</span>
                    <span class="col-2">5.14平米</span>
                    <span class="col-3">北</span>
                    <span class="col-4">普通窗</span>
                  </li>
                                  <li>
                    <span class="col-1">卫生间B</span>
                    <span class="col-2">4.5平米</span>
                    <span class="col-3">北</span>
                    <span class="col-4">普通窗</span>
                  </li>
                                  <li>
                    <span class="col-1">阳台A</span>
                    <span class="col-2">3.47平米</span>
                    <span class="col-3">南 东</span>
                    <span class="col-4">落地窗</span>
                  </li>
                                  <li>
                    <span class="col-1">阳台B</span>
                    <span class="col-2">2.94平米</span>
                    <span class="col-3">北</span>
                    <span class="col-4">普通窗</span>
                  </li>
                                  <li>
                    <span class="col-1">阳台C</span>
                    <span class="col-2">1.95平米</span>
                    <span class="col-3">南 东</span>
                    <span class="col-4">落地窗</span>
                  </li>
                                          </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
        <!-- 房源照片 -->
          <div data-component="housePhotos">
    <div class="newwrap" id="housePic">
      <div class="content-wrapper housePic">
        <h3>
          <div class="title">此房源照片</div>
        </h3>
        <div class="container">
          <div class="list">
                          <div data-index="0">
                <img src="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-客厅">
                <span class="name">客厅</span>
              </div>
                          <div data-index="1">
                <img src="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-客厅">
                <span class="name">客厅</span>
              </div>
                          <div data-index="2">
                <img src="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-卧室A">
                <span class="name">卧室A</span>
              </div>
                          <div data-index="3">
                <img src="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_710,h_400,l_bk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-户型图">
                <span class="name">户型图</span>
              </div>
                          <div data-index="4">
                <img src="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-卧室B">
                <span class="name">卧室B</span>
              </div>
                          <div data-index="5">
                <img src="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-卧室C">
                <span class="name">卧室C</span>
              </div>
                          <div data-index="6">
                <img src="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-厨房">
                <span class="name">厨房</span>
              </div>
                          <div data-index="7">
                <img src="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="满五唯一通透户型楼层好有电梯交通便利-卫生间A">
                <span class="name">卫生间A</span>
              </div>
                        <!-- <div>
              <img src="//placehold.it/450x338" alt="">
              <span class="name">客厅A 18平米 南 落地窗</span>
            </div> -->
            <div class="left_fix"></div>
            <div class="left_fix"></div>
          </div>
        </div>
        <div class="more">查看更多图片</div>
      </div>
    </div>

    <div class="bigImg">
      <div class="mask"></div>
      <div class="list">
        <img src="" alt="">
        <div class="loading"></div>
        <div class="pre"><span></span></div>
        <div class="next"><span></span></div>
      </div>
      <div class="close"></div>
      <div class="slide">
        <div class="desc"></div>
        <ul>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg" data-desc="客厅 1/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/pc1_2aF0oTxuL.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg" data-desc="客厅 2/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/pc0_yudr7A4uE_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg" data-desc="卧室A 3/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/pc0_RiKJc1Cbf_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_710,h_400,l_bk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png" data-desc="户型图 4/8" data-pic="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_1000,h_750,l_bk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/hdic-frame/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_710,h_400,l_bk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg" data-desc="卧室B 5/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg" data-desc="卧室C 6/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg" data-desc="厨房 7/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                      <li data-src="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" data-uri="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg" data-desc="卫生间A 8/8" data-pic="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com">
              <img src="https://ke-image.ljcdn.com/120000-inspection/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com" alt="">
            </li>
                    <!-- <li data-src="//image2.ljcdn.com/appro/group2/M00/B7/AA/rBAF7FX6sUqAeuhGAADSk3x5cr4639.jpg.1024x768.jpg" data-desc="客厅1"><img src="//image2.ljcdn.com/appro/group2/M00/B7/AA/rBAF7FX6sUqAeuhGAADSk3x5cr4639.jpg.89x67.jpg" alt="客厅1"></li> -->
        </ul>
        <div class="pre-show-danger"><span>风险提示：</span> <p>以上户型图为房源参考图，其中户型结构及面积并非按国家专业测绘活动所得，与真实现状及产权证明呈现的面积存在差异，仅供参考，请以产权证明或专业机构测量结果为准。</p></div>
      </div>
    </div>
  </div>
        <!-- 看房记录 -->
        <div data-component="seeRecord" class="newwrap" id="record">
  <div class="record">
    <div class="list">
      <div class="title">近30日看房记录
        <span class="next disable"><i></i></span>
        <span class="pre disable"><i></i></span>
      </div>
      <div class="content">
        <div class="record-header">
          <div class="item mytime">带看时间</div>
          <div class="item myname">带看经纪人</div>
          <div class="phone">咨询</div>
          <div class="item mytotal">带看量</div>
        </div>
        <div class="row"><span class="noData">暂无看房记录</span></div>
      </div>
    </div>
    <div class="panel">
      <div class="panel-title">近7天带看次数</div>
      <div class="count">0</div>
      <div class="totalCount">- 30日带看<span>0</span>次 -</div>
      <!-- <div class="msyy">马上预约看房</div> -->
    </div>
  </div>
</div>
        <!-- 小区介绍 -->
          <div id="resblockCardContainer" class="newwrap" data-component="xiaoquIntro">
    <div class="xiaoquCard">
      <div class="xiaoqu_header clear">
        <h3><span class="fl">新梅江锦秀里简介</span></h3><a class="fr" href=https://tj.ke.com/xiaoqu/1211063460197/ target="_blank"
                                                                  data-lj_dianji="10023">查看小区详情</a>      </div>
      <div class="xiaoqu_content clear">
        <div class="xiaoqu_main fl">
                      <div class="xiaoqu_info">
            <label class="xiaoqu_main_label">小区均价</label>
            <span class="xiaoqu_main_info price_red">
                                              33703 元/㎡
                                  </span>
          </div>
                      <div class="xiaoqu_info">
            <label class="xiaoqu_main_label">建筑年代</label>
            <span class="xiaoqu_main_info">
                                              暂无数据
                                          </span>
          </div>
          <div class="xiaoqu_info clear">
            <label class="xiaoqu_main_label">建筑类型</label>
            <span class="xiaoqu_main_info">
                                                  板楼/塔板结合
                                              </span>
          </div>
          <div class="xiaoqu_info">
            <label class="xiaoqu_main_label">楼栋总数</label>
            <span class="xiaoqu_main_info">
                                              16 栋
                                          </span>
          </div>
        </div>
        <a href="https://tj.ke.com/xiaoqu/1211063460197/" class="xiaoqu_img fr" data-lj_dianji="10023">
                      <img src="https://ke-image.ljcdn.com/hdic-resblock/1dfb382f-fb02-4af4-8f1f-01ca669632cc.jpg.225x170.jpg" alt="新梅江锦秀里">
                          <img class="quanjing-icon" src="https://img.ljcdn.com/beike/buiness2c/1605168844564.gif" alt="新梅江锦秀里全景logo">
                              </a>
      </div>
    </div>
  </div>
        <!-- 税费计算器、房贷计算器  -->
            <div class="newwrap" data-component="calculator">
        <div class="m-calculator VIEWDATA" id="calculator"
             data-city="天津"
             data-cityid="120000"
             data-shoufu='{"houseCode":"101118681080","taxStatus":0,"taxResult":[],"price":"5380000","evaluation":5111000,"loanConfig":{"cityCode":"120000","maxLoanRate":{"first":"70","second":"50"},"maxFound":120,"maxYear":30,"interestRate":{"found":[{"rateText":"\u57fa\u51c6\u5229\u7387","rateMultiple":1,"rate":3.25},{"rateText":"\u4e8c\u5957\u5229\u7387","rateMultiple":1,"rate":3.25},{"rateText":"5\u5e74\u5185\u6700\u65b0\u5229\u7387","rateMultiple":1,"rate":3.25},{"rateText":"5\u5e74\u4ee5\u4e0a\u6700\u65b0\u5229\u7387","rateMultiple":1,"rate":3.25},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e10%","rateMultiple":1.1,"rate":3.575}],"business":[{"rateText":"\u57fa\u51c6\u5229\u7387","rateMultiple":1,"rate":4.2},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e5%","rateMultiple":1.05,"rate":4.41},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e10%","rateMultiple":1.1,"rate":4.62},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e15%","rateMultiple":1.15,"rate":4.83},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e20%","rateMultiple":1.2,"rate":5.04},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e25%","rateMultiple":1.25,"rate":5.25},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e30%","rateMultiple":1.3,"rate":5.46},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e35%","rateMultiple":1.35,"rate":5.67},{"rateText":"\u57fa\u51c6\u5229\u7387\u4e0a\u6d6e40%","rateMultiple":1.4,"rate":5.88}]}},"totalLoan":3577700,"pureShoufu":1802300,"totalShoufu":1802300,"foundLoan":0,"businessLoan":3577700,"businessInterest":2720704.2726215,"foundInterest":0,"totalInterest":2720704.2726215,"monthPay":22460.005555556,"monthReduce":34.783194444444,"monthPayWithInterest":17495.567423949,"totalShoufuDesc":"180.2","pureShoufuDesc":"180.2","agent":{"agentCode":"1003476472","agentUcid":"1000001003476472","name":"\u8d3e\u542f\u8d85","appid":"3","photoPath":"https:\/\/ke-image.ljcdn.com\/usercenter\/images\/uc_ehr_avatar\/12796ce6-119f-4a52-a830-2bd37a46e24e.jpg.120x160.jpg?from=ke.com","agentUrl":"https:\/\/dianpu.ke.com\/1000001003476472","agent_level":"","tags":[],"assessCount":0,"feedbackGoodRate":0,"feedbackCommonRate":0,"feedbackBadRate":0,"seeNums":"2","userName":"\u8d3e\u542f\u8d85","agentLevel":"","agentCity":"120000","agentType":3,"seStatus":true,"esfBlock":false,"fourPhoneOne":"10106188","phoneMain":"10106188","phoneExt":"","storeName":"","totalCommentScore":0,"agentShortCompany":"\u5fb7\u4f51","jobYear":"3-4\u5e74","isQualify":true,"imInfo":{"port":"app_lianjia_jiaoyi_shoufuyusuan_fangyuanxiangqing","app_data":"{\"business_dig_v\":\"{\\\"u\\\":1000001003476472,\\\"v\\\":\\\"V1\\\",\\\"s\\\":\\\"TICKET\\\",\\\"adId\\\":100000828,\\\"flow\\\":\\\"commerce\\\",\\\"b\\\":\\\"SellAssignResblockCommerceWeiHuPanBuilderV2\\\",\\\"p\\\":\\\"\\\",\\\"g\\\":\\\"\\\",\\\"sid\\\":\\\"21025186\\\",\\\"rid\\\":\\\"7018217955016832384\\\"}\"}"}},"mzAgent":{"agentCode":"1003476472","agentUcid":"1000001003476472","name":"\u8d3e\u542f\u8d85","appid":"3","photoPath":"https:\/\/ke-image.ljcdn.com\/usercenter\/images\/uc_ehr_avatar\/12796ce6-119f-4a52-a830-2bd37a46e24e.jpg.120x160.jpg?from=ke.com","agentUrl":"https:\/\/dianpu.ke.com\/1000001003476472","agent_level":"","tags":[],"assessCount":0,"feedbackGoodRate":0,"feedbackCommonRate":0,"feedbackBadRate":0,"seeNums":"2","userName":"\u8d3e\u542f\u8d85","agentLevel":"","agentCity":"120000","agentType":3,"seStatus":true,"esfBlock":false,"fourPhoneOne":"10106188","phoneMain":"10106188","phoneExt":"","storeName":"","totalCommentScore":0,"agentShortCompany":"\u5fb7\u4f51","jobYear":"3-4\u5e74","isQualify":true,"imInfo":{"port":"app_lianjia_jiaoyi_shoufuyusuan_fangyuanxiangqing","app_data":"{\"business_dig_v\":\"{\\\"u\\\":1000001003476472,\\\"v\\\":\\\"V1\\\",\\\"s\\\":\\\"CPA\\\",\\\"adId\\\":100000827,\\\"flow\\\":\\\"commerce\\\",\\\"b\\\":\\\"CpaResblockCommerceBuilder\\\",\\\"p\\\":\\\"\\\",\\\"g\\\":\\\"\\\",\\\"sid\\\":\\\"20839958_1211063460197\\\",\\\"rid\\\":\\\"7018217957533617408\\\"}\"}"}}}'
             data-view-evtid="23458"
             data-view-event="ModuleExpo"
             data-action="city_name=天津"
        >
            <div class="tab-hd">
                <h3 class="active">参考首付</h3>
            </div>
            <div class="tab-bd">
                <div class="tab-item tab-tax active">
                    <div class="tab-item-l">
                        <div class="item-top"></div>
                        <dl>
                            <dt></dt>
                            <dd><button id="calculatorBtn">开始计算</button></dd>
                        </dl>
                    </div>
                    <div class="tab-item-r">
                        <div class="result-text"></div>
                        <div class="chart" id="calculator-chart"></div>
                    </div>
                </div>
            </div>
            <div class="tab-ft">
                <span>本次计算仅作为购房参考，不能作为最终的购房依据。了解更准确的方案，建议
                                    <a class="CLICKDATA im-talk"
                       data-role="beikeim-createtalk"
                       data-ucid="1000001003476472"
                       data-click-evtid="23462"
                       data-click-event="IMClick"
                       data-source-extends='house_code=101118681080&port=app_lianjia_jiaoyi_shoufuyusuan_fangyuanxiangqing&app_data={"business_dig_v":"{\"u\":1000001003476472,\"v\":\"V1\",\"s\":\"CPA\",\"adId\":100000827,\"flow\":\"commerce\",\"b\":\"CpaResblockCommerceBuilder\",\"p\":\"\",\"g\":\"\",\"sid\":\"20839958_1211063460197\",\"rid\":\"7018217957533617408\"}"}'
                       data-msg-payload="请问这套房子的首付和税费是多少？">
                        <span class="talk" >咨询经纪人</span>
                    </a>
                                </span>
            </div>
        </div>
    </div>
      </div>
      <div class="box-r">
        <div data-component="floatAgent" id="diamondAgent" class="agbox" data-isorder="0" data-question='[{"text":"\u9996\u4ed8\u7a0e\u8d39\u662f\u591a\u5c11\uff1f","title":"\u5728\u7ebf\u54a8\u8be2\u9996\u4ed8\u7a0e\u8d39","imText":"\u4f60\u597d\uff0c\u6211\u60f3\u54a8\u8be2\u8fd9\u5957\u623f\u6e90\u9996\u4ed8\u7a0e\u8d39\u662f\u591a\u5c11\uff1f"},{"text":"\u623f\u5b50\u6709\u4ec0\u4e48\u4f18\u7f3a\u70b9\uff1f","title":"\u5728\u7ebf\u54a8\u8be2\u623f\u5b50\u4f18\u7f3a\u70b9","imText":"\u4f60\u597d\uff0c\u6211\u60f3\u54a8\u8be2\u8fd9\u5957\u623f\u6e90\u6709\u4ec0\u4e48\u4f18\u7f3a\u70b9\uff1f"},{"text":"\u662f\u540c\u6237\u578b\u6700\u4f4e\u4ef7\u5417\uff1f","title":"\u5728\u7ebf\u54a8\u8be2\u662f\u5426\u540c\u6237\u578b\u6700\u4f4e\u4ef7","imText":"\u4f60\u597d\uff0c\u6211\u60f3\u54a8\u8be2\u8fd9\u5957\u623f\u6e90\u662f\u4e0d\u662f\u540c\u6237\u578b\u7684\u6700\u4f4e\u4ef7\uff1f"},{"text":"\u5728\u51e0\u53f7\u697c\uff0c\u4ec0\u4e48\u4f4d\u7f6e\uff1f","title":"\u5728\u7ebf\u54a8\u8be2\u623f\u5b50\u5728\u4ec0\u4e48\u4f4d\u7f6e","imText":"\u4f60\u597d\uff0c\u6211\u60f3\u54a8\u8be2\u8fd9\u5957\u623f\u6e90\u5728\u51e0\u53f7\u697c\uff0c\u4ec0\u4e48\u4f4d\u7f6e\uff1f"}]'>
</div>
      </div>
    </div>
    <!-- 推荐二手 -->
    <div id="recommendErshou" data-component="recommendErshou"></div>
    <!-- 推荐新房 -->
    <div id="recommendXinfang"></div>
    <!-- 业主 -->
      <div class="m-yezhu" data-component="yezhu">
    <div class="wrap">
      <div class="hd">我有房子要卖</div>
      <ul>
                  <li class="item-gujia">
            <div class="marsk"></div>
            <div class="tit">不知道如何定价</div>
            <div class="sub-tit">每天超过30000次估价请求量</div>
            <a href="https://tj.ke.com/yezhu/gujia/?channel_id=2002" class="btn-link" target="_blank">我要估价&nbsp;&gt;</a>

          </li>
                <li class="item-maifang">
          <div class="marsk"></div>
          <div class="tit">把房源委托给贝壳</div>
          <div class="sub-tit">10万+专业经纪人·线上千万级浏览量</div>
          <a href="https://tj.ke.com/yezhu/maifang/?channel_id=2018" class="btn-link" target="_blank">发布房源&nbsp;&gt;</a>
        </li>
        <li class="item-xiazai">
          <div class="marsk"></div>
          <div class="tit">已有房源在贝壳销售</div>
          <div class="sub-tit">去贝壳APP业主中心管理委托</div>
          <span href="javascript:;" class="btn-link btn-app">
            <span>去APP管理委托&nbsp;&gt;</span>
            <span class="layer-qrcode">
              <span class="icon-qrcode">
                <img src="https://ajax.api.ke.com/qr/getDownloadQr?location=yezhu&ljweb_channel_key=ershoufang_view" />
              </span>
              <span class="txt">去贝壳找房APP提升卖房速度</span>
              <span class="sub-txt">APP·移动卖房新体验</span>
            </span>
          </span>
        </li>
      </ul>
    </div>
  </div>
    <!-- 反xx模板 -->
        <!--
 * @Descripttion:
 * @version:
 * @Author: zhoumeiyan
 * @Date: 2021-05-20 15:35:25
 * @LastEditors: zhoumeiyan
 * @LastEditTime: 2021-05-21 16:00:52
-->
<div class="footer">
  <div class="wrapper">
    <div class="f-title">
      <div class="fl">
        <ul>
                    <li>
            <a href="https://open.ke.com/home" >开放平台 </a> </li>           <li>
            <a href="https://kol.ke.com/" >贝壳号 </a> </li>           <li>
            <a href="https://tj.ke.com/sitemap/" >网站地图 </a> </li>           <li>
            <a href="https://about.ke.com/introduce/index.html" >了解贝壳 </a> </li>           <li>
            <a href="https://investors.ke.com" >投资者关系 / Investors </a> </li>  </ul> </div> <a href="javascript:;" class="fr req_btn">
              官方客服咨询
            </a>
      </div>
      <div class="lianjia-link-box">
        <div class="fl">
          <div class="tab">
                        <span  class="hover" >商圈二手房 </span>             <span >热门二手房 </span>             <span >热门小区 </span>             <span >城市小区 </span>             <span >城市楼盘 </span>             <span >城市二手房 </span>             <span >贝壳规则中心 </span>  </div> <div
              class="link-list">
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/nanyingmenjie/">南营门街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/nanshi/">南市二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/quanyechang/">劝业场二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/xiaobailou/">小白楼二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/tiyuguanjie/">体育馆街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/xinxingjie/">新兴街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/tangjiakou/">唐家口二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/xiangyanglou/">向阳楼二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/wanxincun/">万新村二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/dawangzhuang/">大王庄二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/zhenlidao/">真理道二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/shanghanglu/">上杭路二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/taiyangcheng/">太阳城二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/chunhuajie/">春华街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/changzhoudao/">常州道二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/fuminlu/">富民路二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/zhongshanmenjie/">中山门街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/lushandao/">鲁山道二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/dazhigu/">大直沽二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/erhaoqiaojie/">二号桥街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/yuexiulu/">越秀路二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/liulinjie/">柳林街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/xinmeijiang/">新梅江二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/tiantajie/">天塔街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/taoyuanjie/">桃园街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/chentangzhuang/">陈塘庄二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/machangjie/">马场街二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/guajiasi/">挂甲寺二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/xiawafang/">下瓦房二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/dayingmen/">大营门二手房</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220048565134513/">金海云城二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c12000000020745/">吾悦华邸二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045708568/">乌江南里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220055476333802/">艺墅家酩悦二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045366202/">官易里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045675536/">银山里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045296455/">秋爽里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045285675/">迎水东里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220045083354747/">渤龙公寓二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220041414592976/">锦庭园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220053567702521/">龙峰馨园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045297507/">瑞湾花园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045227921/">凌奥花园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045691173/">丹江里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045206875/">金平东里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045213710/">彩虹花园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220032901911906/">泓荷园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220072598173838/">万科滨海大都会观涛苑二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045367797/">河通花园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220037090394884/">儒林轩二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220041917996893/">富力津门湖澄澜花园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220041406229599/">紫乐广场二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045212973/">田川里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220030379012404/">泉鑫佳苑西区二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220045336148661/">香江健康小镇玫瑰园二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1220024863233832/">绿地海域香颂二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045672121/">如皋里二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1217590228912917/">天房光合谷泊雅苑二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045329948/">天津大学新园村二手房</a>
                                        <a target="_blank" href="https://tj.ke.com/ershoufang/c1211045161407/">盛达园二手房</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220034100984938/">宝翔景苑</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1217590228912917/">天房光合谷泊雅苑</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/12000000020745/">吾悦华邸</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045427536/">永明西里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220035832928857/">水岸城春华园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220045083354747/">渤龙公寓</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045206875/">金平东里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045213710/">彩虹花园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220045336148661/">香江健康小镇玫瑰园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220041406229599/">紫乐广场</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045161407/">盛达园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045227921/">凌奥花园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045675536/">银山里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045672121/">如皋里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220041917996893/">富力津门湖澄澜花园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220048565134513/">金海云城</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045678755/">镇江里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045489269/">广田里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220072598173838/">万科滨海大都会观涛苑</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220053567702521/">龙峰馨园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045691173/">丹江里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045456002/">湘潭里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045422500/">水木天成依湖园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220041414592976/">锦庭园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220024863233832/">绿地海域香颂</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220055476333802/">艺墅家酩悦</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045568190/">晶品轩</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220032901911906/">泓荷园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045212973/">田川里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045708568/">乌江南里</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://cc.ke.com/xiaoqu/">长春小区
</a>
                                        <a target="_blank" href="https://cd.ke.com/xiaoqu/">成都小区
</a>
                                        <a target="_blank" href="https://dg.ke.com/xiaoqu/">东莞小区
</a>
                                        <a target="_blank" href="https://dl.ke.com/xiaoqu/">大连小区
</a>
                                        <a target="_blank" href="https://hf.ke.com/xiaoqu/">合肥小区
</a>
                                        <a target="_blank" href="https://hz.ke.com/xiaoqu/">杭州小区
</a>
                                        <a target="_blank" href="https://lf.ke.com/xiaoqu/">廊坊小区
</a>
                                        <a target="_blank" href="https://sh.ke.com/xiaoqu/">上海小区
</a>
                                        <a target="_blank" href="https://sjz.ke.com/xiaoqu/">石家庄小区
</a>
                                        <a target="_blank" href="https://sy.ke.com/xiaoqu/">沈阳小区
</a>
                                        <a target="_blank" href="https://sz.ke.com/xiaoqu/">深圳小区
</a>
                                        <a target="_blank" href="https://wh.ke.com/xiaoqu/">武汉小区
</a>
                                        <a target="_blank" href="https://wx.ke.com/xiaoqu/">无锡小区
</a>
                                        <a target="_blank" href="https://xa.ke.com/xiaoqu/">西安小区
</a>
                                        <a target="_blank" href="https://xz.ke.com/xiaoqu/">徐州小区
</a>
                                        <a target="_blank" href="https://zh.ke.com/xiaoqu/">珠海小区
</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://bj.fang.ke.com/loupan/">北京楼盘
</a>
                                        <a target="_blank" href="https://cc.fang.ke.com/loupan/">长春楼盘
</a>
                                        <a target="_blank" href="https://dg.fang.ke.com/loupan/">东莞楼盘
</a>
                                        <a target="_blank" href="https://dl.fang.ke.com/loupan/">大连楼盘
</a>
                                        <a target="_blank" href="https://fs.fang.ke.com/loupan/">佛山楼盘
</a>
                                        <a target="_blank" href="https://gz.fang.ke.com/loupan/">广州楼盘
</a>
                                        <a target="_blank" href="https://hf.fang.ke.com/loupan/">合肥楼盘
</a>
                                        <a target="_blank" href="https://hk.fang.ke.com/loupan/">海口楼盘
</a>
                                        <a target="_blank" href="https://hui.fang.ke.com/loupan/">惠州楼盘
</a>
                                        <a target="_blank" href="https://lf.fang.ke.com/loupan/">廊坊楼盘
</a>
                                        <a target="_blank" href="https://nj.fang.ke.com/loupan/">南京楼盘
</a>
                                        <a target="_blank" href="https://sh.fang.ke.com/loupan/">上海楼盘
</a>
                                        <a target="_blank" href="https://su.fang.ke.com/loupan/">苏州楼盘
</a>
                                        <a target="_blank" href="https://sy.fang.ke.com/loupan/">沈阳楼盘
</a>
                                        <a target="_blank" href="https://wx.fang.ke.com/loupan/">无锡楼盘
</a>
                                        <a target="_blank" href="https://xz.fang.ke.com/loupan/">徐州楼盘
</a>
                                        <a target="_blank" href="https://yt.fang.ke.com/loupan/">烟台楼盘
</a>
                                        <a target="_blank" href="https://zh.fang.ke.com/loupan/">珠海楼盘
</a>
                                        <a target="_blank" href="https://zs.fang.ke.com/loupan/">中山楼盘
</a>
                                        <a target="_blank" href="https://zz.fang.ke.com/loupan/">郑州楼盘
</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://bj.ke.com/ershoufang/">北京二手房
</a>
                                        <a target="_blank" href="https://cc.ke.com/ershoufang/">长春二手房
</a>
                                        <a target="_blank" href="https://dg.ke.com/ershoufang/">东莞二手房
</a>
                                        <a target="_blank" href="https://dl.ke.com/ershoufang/">大连二手房
</a>
                                        <a target="_blank" href="https://fs.ke.com/ershoufang/">佛山二手房
</a>
                                        <a target="_blank" href="https://gz.ke.com/ershoufang/">广州二手房
</a>
                                        <a target="_blank" href="https://hf.ke.com/ershoufang/">合肥二手房
</a>
                                        <a target="_blank" href="https://hk.ke.com/ershoufang/">海口二手房
</a>
                                        <a target="_blank" href="https://hui.ke.com/ershoufang/">惠州二手房
</a>
                                        <a target="_blank" href="https://lf.ke.com/ershoufang/">廊坊二手房
</a>
                                        <a target="_blank" href="https://nj.ke.com/ershoufang/">南京二手房
</a>
                                        <a target="_blank" href="https://sh.ke.com/ershoufang/">上海二手房
</a>
                                        <a target="_blank" href="https://su.ke.com/ershoufang/">苏州二手房
</a>
                                        <a target="_blank" href="https://sy.ke.com/ershoufang/">沈阳二手房
</a>
                                        <a target="_blank" href="https://wx.ke.com/ershoufang/">无锡二手房
</a>
                                        <a target="_blank" href="https://xz.ke.com/ershoufang/">徐州二手房
</a>
                                        <a target="_blank" href="https://yt.ke.com/ershoufang/">烟台二手房
</a>
                                        <a target="_blank" href="https://zh.ke.com/ershoufang/">珠海二手房
</a>
                                        <a target="_blank" href="https://zs.ke.com/ershoufang/">中山二手房
</a>
                                        <a target="_blank" href="https://zz.ke.com/ershoufang/">郑州二手房
</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://www.ke.com/zhuanti/protocol">贝壳找房隐私声明 正文</a>
                                        <a target="_blank" href="https://www.ke.com/zhuanti/serviceProtocol">贝壳平台服务使用协议</a>
                                        <a target="_blank" href="https://rules-center.ke.com">贝壳规则中心</a>
                                      </dd>
                </dl>
              </div>
                        </div>
        </div>
        <div class="clear"></div>
      </div>
      <ul class="partner-logo">
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=招商银行">
                    <a target="_blank" href="https://image1.ljcdn.com/materials/appindexconf/8f9822cf882e6f263b81f7a394dd0712.jpg">
            <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/partner/zsyh.png?_v=20191219184206415" title="招商银行" alt="招商银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=上海银行">
                    <a target="_blank" href="https://img.ljcdn.com/beike/PC/1624330009091.jpg">
            <img src="https://image1.ljcdn.com/materials/appindexconf/57f25e75780b61e27a74a8a5adc7586a.jpg" title="上海银行" alt="上海银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=中国光大银行">
                    <a target="_blank" href="https://image1.ljcdn.com/materials/appindexconf/2d8668bfc893536176d1462378e1cbd7.jpg">
            <img src="https://image1.ljcdn.com/materials/appindexconf/ea3bcafededbafe865f986d01c6030a3.png" title="中国光大银行" alt="中国光大银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=华夏银行">
                    <a target="_blank" href="https://img.ljcdn.com/beike/beike/1592276474011.png">
            <img src="https://image1.ljcdn.com/materials/appindexconf/369f029b0449e76b616c1920f18774ed.png" title="华夏银行" alt="华夏银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=北京农商银行">
                    <a target="_blank" href="https://img.ljcdn.com/beike/PC/1631518116390.jpg">
            <img src="https://image1.ljcdn.com/materials/appindexconf/4f590a93d92909b167d428b2f45d5274.jpg" title="北京农商银行" alt="北京农商银行">
          </a>
                  </li>
              </ul>
      <div class="bottom">
        <div class="copyright fl">
                    天津小屋信息科技有限公司 | 地址：天津经济技术开发区南港工业区综合服务区办公楼C座一层112室09单元 | 电话：10106188 | <a target="_blank"
            href="http://beian.miit.gov.cn/">津ICP备18000836号-1</a> | © Copyright 2024 ke.com版权所有
          | <a target="_blank" href="//file.ljcdn.com/bigc-file2cdn/Mensa/1585731661478.pdf">营业执照</a>
                    | <a target="_blank" href="//file.ljcdn.com/bigc-file2cdn/Mensa/1585732230759.pdf">ICP证</a>
          | <a target="_blank"
            href="https://www.ke.com/zhuanti/commonProtocol?id=1dc38816524dffa9da7949856540d168">贝壳平台知识产权保护</a>
          <br>
          老年人客服热线：010-60640529<br>
          违法和不良信息举报电话：010-86440676| 违法和不良信息举报邮箱：jubaoyouxiang@ke.com <br>
          涉未成年人举报电话：010-86440676| 涉未成年人举报邮箱：jubaoyouxiang@ke.com
          <br>
          <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/beian.png?_v=202401081627157" alt="beian" style="display: inline-block;height: 20px;width: auto;">
          <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=12010602120282">津公网安备
            12010602120282号</a> |
          <a target="_blank" href="//www.12377.cn">网上有害信息举报专区</a>
        </div>
      </div>
    </div>
  </div>
  
              <div class="validate" data-component="C_reportBox">
    <div class="validateOverlay"></div>
    <div class="valideteMain" data-entrance="">
        <div class="validateTop">
            <a href="javascript:;" class="validateCloseBtn"></a>
        </div>
        <div class="reportBox">
            <form action="" method="post" class="validForm">
                <div class="formMain">
                    <h3></h3>
                    <div class="infju_me">
                        <div class="inputBox"></div>
                        <div class="text_box">
                        <textarea class="others" maxlength="60"
                                  placeholder="补充您遇到的问题。例如：是否带看，房源真实情况等（至少15个字）"></textarea>
                            <div class="cont_box">
                                <span class="text_count" value="">0</span>/60
                            </div>
                        </div>
                        <div class="note">
                            <a href="https://rule.ke.com/#/promise/detail?busiType=1&id=76425" target="_blank">
                                贝壳坚决执行
                                <span>假一赔百</span>
                                条例，举报通过后会对举报者进行现金奖励，请注意接收相关消息
                            </a>
                        </div>
                        
                    </div>
                </div>
            </form>
            <div class="wyjbconfrm jiudin CLICKDATA"
            id="reportBtn"
            data-click-evtid="11449" 
            data-click-event="WebClick"
            data-action="source_type=详情页_举报入口_点击提交&housedel_id=101118681080&housedel_source=30201">
                举报
            </div>
            <div id="varifyCodeBtn"></div>
        </div>
        <div class="reportResult">
            <div class="result_icon"></div>
            <div class="result_title"></div>
            <div class="result_desc"></div>
        </div>
        <div id="reportCaptcha"></div>
    </div>
</div>
      </div>
<div id="only" data-city="tj" data-page="ershoufang_view"></div><script type="text/javascript" src="https://s1.ljcdn.com/pegasus/redskull/deps/jquery_lj_0_1.js?_v=202401081627157" crossorigin="anonymous"></script><script src='https://file.ljcdn.com/nebula/index_1687226806824.js' crossorigin="anonymous"></script>
  <script>if (window.require) {var path = 'https://s1.ljcdn.com/pegasus/pc/asset?_v=202401081627157'.split("?");require.config({baseUrl: path[0],paths: {'echarts': '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar': '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line': '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie': '../../dep/echarts-1.4.1/build/echarts','echarts3': '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs: path[1]});}var feData = {"cityName": "北京","getFavHouseUrl": "/api/gethousefav","setFavHouseUrl": "/api/sethousefav","getLastSearch": "/api/getlastsearch","getCommunityHistory": "/api/getcommunityhistory","verifyHouse": "/api/verifyHouse","getUser": "/api/getUser","verifyCode": "/api/getVerifyCode","complaint": "/api/complaint","getDecoration": "/api/getDecoration","trendData": "/site/getpicinfo"}</script>
  <script>
    window.__STAT_LJ_CONF = window.__STAT_LJ_CONF || {};
    window.__STAT_LJ_CONF.params = window.__STAT_LJ_CONF.params || {};
    window.__STAT_LJ_CONF.params.is_yanjiao = 0;
          </script>
  <script type="text/javascript" src="https://s1.ljcdn.com/pegasus/redskull/js/sellDetail/index.js?_v=202401081627157" crossorigin="anonymous"></script>
  <script>
    window.GLOBAL_INFOS = {
      ucid: '',
      hasDaikan: '1',
      houseType: '',
      houseCode:'101118681080',
      isUnique: '暂无数据',
      registerTime: '1680424356',
      area: '145.21平米',
      totalPrice: '538',
      price: '37050',
      houseId: '101118681080',
      resblockId: '1211063460197',
      resblockName: '新梅江锦秀里',
      isRemove: '0',
      status: '1',
      defaultImg: 'https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157',
      digv: '',
      fbExpoId: $.getQuery('fb_expo_id'),
      showType: $.getQuery('show_type'),
      defaultBrokerIcon: 'https://s1.ljcdn.com/pegasus/redskull/images/common/default-jingjiren.png?_v=202401081627157',
      resblockPosition: '117.24402,39.049928',
      cityId: '120000',
      changedate: [1, 3, 4, 5, 3],
      changenum: [123, 567, 232, 347, 122],
      diamondAgent:null,
      goldAgent:null,
      agentInfo:null,
      uniqueAgent:true,
      showCart: '0',
      test_400_hide: '',
      uuid: 'a2daacf1-47ee-4baa-bfaf-a48deb15e937',
      loadingImg: 'https://s1.ljcdn.com/pegasus/redskull/images/ershoufang/sellDetail/loading.gif?_v=202401081627157',
      qrImg: 'https://ajax.api.ke.com/qr/getDownloadQr',
      title: '满五唯一通透户型楼层好有电梯交通便利_天津新梅江锦秀里二手房3室1厅145.21平米【天津贝壳找房】',
      images: [{"type":"\u5ba2\u5385","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc1_2aF0oTxuL.jpg","isHead":1,"isVr":1,"url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc1_2aF0oTxuL.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc1_2aF0oTxuL.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc1_2aF0oTxuL.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u5ba2\u5385","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_yudr7A4uE_1.jpg","url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_yudr7A4uE_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_yudr7A4uE_1.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_yudr7A4uE_1.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u5367\u5ba4A","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_RiKJc1Cbf_1.jpg","url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_RiKJc1Cbf_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_RiKJc1Cbf_1.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/pc0_RiKJc1Cbf_1.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u6237\u578b\u56fe","fcSort":0,"isOverground":0,"uri":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png","url":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_710,h_400,l_bk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_1000,h_750,l_bk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_df9df870-cd85-4d62-b7e7-69c7e36ef37f.png!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u5367\u5ba4B","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg","url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/31776108-cf93-47b4-98fd-84f3b028f657_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u5367\u5ba4C","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/bee69374-362e-4846-833f-910c6d44e134_1000.jpg","url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/bee69374-362e-4846-833f-910c6d44e134_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u53a8\u623f","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg","url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/5651415c-ef4d-4a23-b00b-262a99d03c86_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"},{"type":"\u536b\u751f\u95f4A","uri":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg","url":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriBig":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_1000,h_750,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com","uriSmall":"https:\/\/ke-image.ljcdn.com\/120000-inspection\/ff36220b-63c8-481b-b4c8-997d1eb02126_1000.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com"}],
      housedelType: '有VR',
      houseSource: '30201',
      agentList: [{"tags":null,"school":"\u5929\u6d25\u8f7b\u5de5\u804c\u4e1a\u6280\u672f\u5b66\u9662","seniority":"1-2\u5e74","responseRate":1,"imRate":0,"phoneRate":1,"imQualified":1,"phoneQualified":1,"allVisitCount":8,"allDealCount":5,"feedbackScore":5,"commentCount":168,"majorBizcircle":"\u65b0\u6885\u6c5f","majorDistrict":"\u6cb3\u897f","allCustomerCount":131,"answerCount":0,"usefulAnswerCount":0,"vipLevel":0,"politicalCode":"9","politicalName":"","politicalImg":null,"source":"MEMBER","ucId":"1000000030031782","userCode":"30031782","reason":null,"agentMark":null,"houseRole":null,"digV":"{\"u\":1000000030031782,\"v\":\"V3\",\"s\":\"MEMBER\",\"adId\":100000144,\"flow\":\"commerce\",\"b\":\"CommerceSynthesizeMEMBERBuilder\",\"p\":\"\",\"g\":\"ab767-1096-3489\",\"sid\":\"10000000300317821211063460197200002_20780099\",\"rid\":\"7018217959563280449\"}","flowType":"commerce","proofComplete":false,"port":"shangyehua_ershou_pc_zhanwei_zuanzhan","name":"\u9a86\u8273\u4e3d","agentDomain":"OTHER","avatar":"https:\/\/img.ljcdn.com\/usercenter\/images\/uc_ehr_avatar\/1f9262ea-5de4-4d19-bf28-e4f40cff8ef5.jpg.480x640.jpg","mobileType":"AGENT","mobile":"","brand":"\u5fb7\u4f51","jobTitle":"\u9ad8\u7ea7\u5e97\u7ecf\u7406","positionCode":"785","positionName":"\u7efc\u5408\u7ecf\u7eaa\u4eba","officeAddress":"120000","officeAddressName":"\u5929\u6d25","compName":"\u5929\u6d25\u5fb7\u4f51","compFullName":"\u5929\u6d25\u5fb7\u4f51","resblockId":null,"bizcircleId":null,"stationId":null,"houseCode":null,"houseId":null,"style":null,"agentToken":"1754554490444558337","shopCode":"TJ_14_1204439","shopName":"\u805a\u661f\u67cf\u7fe0\u56ed\u65d7\u8230\u5e97-\u4e00\u5e97","rentApartmentAgentType":null,"dianpuUrl":"https:\/\/dianpu.ke.com\/1000000030031782?_referSource=100000144&houseCode=101118681080","primaryProof":[],"proofListWithSort":[{"no":"30620201012100000746","creditScore":"","img":"https:\/\/image1.ljcdn.com\/ehr-personnel\/20190108180804890B5IW0ZJU.png","creditGrade":"","creditGradeUrl":"","title":"\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u8bc1","type":2,"jumpQueryUrl":"","originUrl":"","creditEvaluate":"","extField":"","verify":1,"verifyUrl":"","desc":"\u6301\u6709\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u804c\u4e1a\u8d44\u683c\u8bc1\u3002\r\n\u7531\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u9881\u53d1\u4eba\u529b\u8d44\u6e90\u793e\u4f1a\u4fdd\u969c\u90e8\u3001\u4f4f\u623f\u57ce\u4e61\u5efa\u8bbe\u90e8\u76d1\u5236\uff0c\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u7528\u5370\u7684\u76f8\u5e94\u7ea7\u522b\u300a\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4e13\u4e1a\u4eba\u5458\u804c\u4e1a\u8d44\u683c\u8bc1\u4e66\u300b\u5728\u5168\u56fd\u8303\u56f4\u6709\u6548\u3002"},{"img":"https:\/\/img.ljcdn.com\/ehr-personnel\/2297cf3c-d718-45cc-bf03-f8e449cad4e5.jpg","creditEvaluate":"","creditGradeUrl":"","title":"\u8d39\u7387","type":-100,"desc":"","jumpQueryUrl":""}],"agentProofList":[{"no":"30620201012100000746","creditScore":"","img":"https:\/\/image1.ljcdn.com\/ehr-personnel\/20190108180804890B5IW0ZJU.png","creditGrade":"","creditGradeUrl":"","title":"\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u8bc1","type":2,"jumpQueryUrl":"","originUrl":"","creditEvaluate":"","extField":"","verify":1,"verifyUrl":"","desc":"\u6301\u6709\u5168\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u534f\u7406\u804c\u4e1a\u8d44\u683c\u8bc1\u3002\r\n\u7531\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u9881\u53d1\u4eba\u529b\u8d44\u6e90\u793e\u4f1a\u4fdd\u969c\u90e8\u3001\u4f4f\u623f\u57ce\u4e61\u5efa\u8bbe\u90e8\u76d1\u5236\uff0c\u4e2d\u56fd\u623f\u5730\u4ea7\u4f30\u4ef7\u5e08\u4e0e\u623f\u5730\u4ea7\u7ecf\u7eaa\u4eba\u5b66\u4f1a\u7528\u5370\u7684\u76f8\u5e94\u7ea7\u522b\u300a\u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u623f\u5730\u4ea7\u7ecf\u7eaa\u4e13\u4e1a\u4eba\u5458\u804c\u4e1a\u8d44\u683c\u8bc1\u4e66\u300b\u5728\u5168\u56fd\u8303\u56f4\u6709\u6548\u3002"},{"img":"https:\/\/img.ljcdn.com\/ehr-personnel\/2297cf3c-d718-45cc-bf03-f8e449cad4e5.jpg","creditEvaluate":"","creditGradeUrl":"","title":"\u8d39\u7387","type":-100,"desc":"","jumpQueryUrl":""}],"orgProofList":null,"levelLabel":"\u661f\u5149\u7ecf\u7eaa\u4eba","levelLabelUrl":"https:\/\/image1.ljcdn.com\/baikeimg\/898d7b42422767de8fd43eaf9fe395fc0f49746f.png","specialtyList":["\u8d1d\u58f3\u5206\u4f18\u79c0","\u5ba2\u6237\u63a8\u8350\u524d10%"],"phone400":"4000326815-4808","usefulCount":0,"showingCount":0,"lastShowingTime":null,"qrCodeUrl":null,"sellProperty":{"anchorProperty":[],"allDealCount":5,"allVisitCount":8},"rentProperty":{"allDealCount":53,"allVisitCount":0},"nhProperty":{"anchorProperty":{"level":"","name":""},"lastThirtyCust":6,"lastThirtyVisit":4,"allDealCount":1,"nhKeQualityLevel":0,"allVisitCount":4,"nhExcellentAgentTag":0,"nhKeQuality":0},"keQuality":415,"brandCode":"3","agentLicenseCode":null,"agentLicenseExt":null,"agentLicensePcExt":null,"qualityRank":null,"v5Rank":null,"extAgentProofMap":null,"extAgentProofTitleMap":{"creditGradeTitle":"\u4fe1\u7528\u7b49\u7ea7:","descTitle":"\u8bc1\u4ef6\u8bf4\u660e:","creditScoreTitle":"\u4fe1\u7528\u8bc4\u5206:","originUrlTitle":"\u67e5\u770b\u8be6\u60c5","noTitle":"\u8bc1\u4ef6\u7f16\u53f7:"},"paramTagList":["commerceMemberLevel1"],"isFjh":0,"orgCode":"TJ_15_1204440","orgName":"\u805a\u661f\u67cf\u7fe0\u56ed\u65d7\u8230\u5e97-\u4e00\u5e97\u4e00\u7ec4","exposureNum":null,"cityName":null,"agentName":null,"cityCode":null,"nhExpectSjScore":null,"originalNhExpectSjScore":null,"nhExpectCalcMode":null,"locationId":null,"locationType":null}],
      isNewHouseReport: '1',
    }
  </script>
  <!-- LianjiaIM   --><script>window.LIANJIANIM_INFOS = {ucid: '',staticRoot: 'https://s1.ljcdn.com/pegasus/?_v=202401081627157'}</script><!--cookie mapping--><img src='' alt="cookie_mapping_url" style="display: none;"><!--反爬虫--><script>window['__abbaidu_2011_subidgetf'] = function () {return 110000;};window['__abbaidu_2011_cb'] = function (responseData) {var res = JSON.stringify({ t: responseData, r: location.href, os: 'web', v: '0.1' });res = btoa ? btoa(res) : res;document.cookie = 'srcid=' + res + ';path=/;';};</script><!--数据上报--><script>(function(){var bp = document.createElement('script');var curProtocol = window.location.protocol.split(':')[0];if (curProtocol === 'https'){bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';}else{bp.src = 'http://push.zhanzhang.baidu.com/push.js';}var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(bp, s);})();</script><script>$(function(){$('.lj-lazy').lazyload();$('.lazyload').scrollLoading();})</script><script type="application/javascript" src="https://dlswbr.baidu.com/heicha/mw/abclite-2011-s2.js"></script></body></html>

    '''

    # 初始化一个字典来存储提取的信息
    house_info = {
        '户型结构': '',
        '套内面积': '',
        '所在楼层': '',
        '套内面积': '',
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

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(str, 'html.parser')
    introContent = soup.find('div', class_="introContent")

    # 查找包含信息的数据
    for item in introContent.find_all('li'):
        label = item.find('span', class_='label').text.strip()
        value = item.get_text(strip=True).replace("\n", '').replace(label, '')
        print(f'{label} : {value}')
        if label in house_info:
            house_info[label] = value
    # 提取结果
    return {k: v for k, v in house_info.items() if v}


def build_zone_info():
    str1 = '''
<!DOCTYPE html><html class="" lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" /><!-- 2017.11.8 市场需求加上新的统计 -->

<script>
  ljConf = {
      city_id: '120000',
      city_abbr: 'tj',
      city_name: '天津',
      channel: 'xiaoqu',
      page: 'xiaoqu_detail',
      pageConfig: {"ajaxroot":"\/\/ajax.api.ke.com\/","imAppid":"BEIKE_WEB_20170105","imAppkey":"2d7e19fe599aa5087b4d46948e552e89"},
      feroot: '//s1.ljcdn.com/pegasus/',
      ferootnew: '//s1.ljcdn.com/pegasus/',
      domainConfig: {"webroot":"\/\/bj.ke.com\/","wwwroot":"\/\/www.ke.com\/","ajaxapiroot":"https:\/\/ajax.api.ke.com\/","apiroot":"\/\/ajax.ke.com\/","festaticroot":"\/\/cms.ke.com\/static\/","videoroot":"\/\/video.ljcdn.com\/","feroot":"\/\/s1.ljcdn.com\/pegasus\/","ferootnew":"\/\/s1.ljcdn.com\/pegasus\/","newsroot":"\/\/news.ke.com\/","userroot":"\/\/user.ke.com\/","fangroot":"\/\/bj.fang.ke.com\/","agentroot":"\/\/agent.lianjia.com\/","version":"202401081627157bd","pageconfig":{"ajaxroot":"\/\/ajax.api.ke.com\/","imAppid":"BEIKE_WEB_20170105","imAppkey":"2d7e19fe599aa5087b4d46948e552e89"},"imgroot":null,"behaviors":[]},
      ucid:'',
      cdn:'0',
  };
</script>

<!-- 2017.7.18 开放全国 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?9152f8221cb6243a53c83b956842be8a";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<script src='//file.ljcdn.com/fee/index.js' crossorigin="anonymous"></script><script type="text/javascript" src="//s1.ljcdn.com/captcha-js-sdk-v2/captcha.js"></script><script type="text/javascript" src="//s1.ljcdn.com/clogin/js/pcLogin.js"></script><script>function evn() {var match = location.href.match(/\:\/\/(dev|test|preview|\d).+/);if (match && match[1]) {return match[1];} else {return 'prod';}}window.dt && dt.set({pid: 'Pegasus',uuid: document.cookie.match(/lianjia_uuid=([^;]+)/) ? document.cookie.match(/lianjia_uuid=([^;]+)/)[1] : '',ucid: '',env: evn() === 'prod' ? "production" : "",is_test: evn() !== 'prod',record: {spa: false,white_screen: { enable: false },time_on_page: true,performance: true,js_error: true,js_error_report_config: {ERROR_RUNTIME: true,ERROR_SCRIPT: true,ERROR_STYLE: true,ERROR_IMAGE: true,ERROR_AUDIO: true,ERROR_VIDEO: true,ERROR_CONSOLE: false,ERROR_TRY_CATCH: true,checkErrorNeedReport: function (desc, stack) {const userAgent = navigator.userAgent;const isIE = /Trident|MSIE/.test(userAgent);if (isIE) {return false;}if (!/\/\/(s1\.ljcdn\.com\/)/.test(desc) &&!/\/\/(s1\.ljcdn\.com\/)/.test(stack)) {return false;}if (/\/\/s1\.ljcdn\.com\/(link\-static\/resource\/plat_framework|web\-im\-sdk|agent\-sj\-sdk|vrlab|tingyun|\$\.|\$ is not defined|no stach)/.test(desc) ||/\/\/s1\.ljcdn\.com\/(link\-static\/resource\/plat_framework|web\-im\-sdk|agent\-sj\-sdk|vrlab|tingyun|\$\.|\$ is not defined|no stach)/.test(stack) ||/\/\/s1\.ljcdn\.com\/(pegasus\/redskull\/images\/(common|ershoufang)\/(beian.png|blank.gif|im-chart@2x.png|loading.gif|partner\/zsyh.png|vrgold.png|default_house_detail.png))/.test(desc) ||/\/\/s1\.ljcdn\.com\/(pegasus\/redskull\/images\/(common|ershoufang)\/(beian.png|blank.gif|im-chart@2x.png|loading.gif|partner\/zsyh.png|vrgold.png|default_house_detail.png))/.test(stack)) {return false;}return true;}}},version: '1.0.0'});function _plog(evtId, data, pageId) {var defData = {'plat_form': navigator.platform,'page_url': window.location.href};data = $.extend(defData, data);dt.notify(evtId,pageId || window.location.href,data);}</script>
<script>
    function RESIZEIMG(b,k,l,m){var c=b.parentNode;var d=parseInt(c.offsetWidth)||k;var e=parseInt(c.offsetHeight)||l;var f=d/e;var g=b.naturalWidth||b.width;var h=b.naturalHeight||b.height;var i=g/h;var j="width";if(f<i){j="height";try{b.style["left"]="-"+parseInt(Math.abs((d-(g*e/h))/2))+"px"}catch(e){}}else if(m){try{b.style["top"]="-"+parseInt(Math.abs((e-(h*d/g))/2))+"px"}catch(e){}};b.style[j]="100%";};
</script>
<script>window.FROM_CHANNEL = 'beike';</script>  <link rel="stylesheet" href="https://s1.ljcdn.com/pegasus/redskull/css/xiaoquDetail/index.css?_v=202401081627157">
  <link rel="canonical" href="https://tj.ke.com/xiaoqu/12000000001175/"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc">
<title>喜峰嘉园_天津喜峰嘉园二手房|房价|租房【天津贝壳找房】</title>
<meta name="description" content="贝壳天津小区大全,喜峰嘉园参考均价:20700元/㎡,位于河北新开河,喜峰嘉园在售二手房源21套,已有20人关注.查询喜峰嘉园优质二手房房源、租房房源、经纪人、近期成交记录等信息,就到天津贝壳找房." />
<meta name="keywords" content="喜峰嘉园,天津喜峰嘉园,喜峰嘉园二手房,喜峰嘉园房价,喜峰嘉园租房 " />
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.ke.com/tj/xiaoqu/12000000001175/" >
<meta name="mobile-agent" content="format=html5;url=https://m.ke.com/tj/xiaoqu/12000000001175/"><link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><!--[if lt IE 9]><script type="text/javascript" src="https://s1.ljcdn.com/pegasus/dep/common-require/html5.js?_v=202401081627157" crossorigin="anonymous"></script><![endif]--></head><!-- htmlRef --><body id="beike">
<div class="xiaoquDetailPage">
  <div class="banner" style="display: block">
    <div class="container">
        <ul class="channelList">
            <li>
                <a href="//www.ke.com/">首页</a>
            </li>
                            <li                     class="">
                    <a href="https://tj.ke.com/ershoufang/" >二手房</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.fang.ke.com/loupan" >新房</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.zu.ke.com/zufang" >租房</a>
                                                        </li>
                            <li                     class="selected">
                    <a href="https://tj.ke.com/xiaoqu/" >小区</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://tj.ke.com/yezhu/maifang/?channel_id=2004" target="_blank">发布房源</a>
                                                        </li>
                            <li                     class="">
                    <a href="https://research.ke.com/" target="_blank">贝壳研究院</a>
                                                        </li>
                            <li                     class="">
                    <a href="javascript:void(0)" >下载APP</a>
                                                                <div class="appQRCode">
                            <img src="//ajax.api.ke.com/qr/getDownloadQr?location=site_middle">
                        </div>
                                    </li>
                            <li                     class="">
                    <a href="https://open.ke.com/home?source=9" target="_blank">开放平台</a>
                                                        </li>
                    </ul>
        <div class="banner-right">
            <div class="login" id="userInfoContainer">
                <i></i>
                <a href="https://clogin.ke.com/login?service=https%3A%2F%2Fwww.ke.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Ftj.ke.com%252Fxiaoqu%252F12000000001175%252F" id="loginBtn" rel="nofollow">登录</a>
                /
                <a href="https://clogin.ke.com/register?service=https%3A%2F%2Fwww.ke.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Ftj.ke.com%252Fxiaoqu%252F12000000001175%252F" id="registerBtn" rel="nofollow">注册</a>
            </div>
            <div class="phone">
                <i></i>
                <span>投诉电话 1010-6188</span>
            </div>
        </div>
    </div>
</div>

    <script type="text/template" id="userInfoTpl">
        <i></i>
        <%if(isAgent){%>
        <a id="userNameContainer" href="<%=ljConf.domainConfig.agentroot%>"><%=username%></a>
        <%}else{%>
        <a id="userNameContainer" href="<%=ljConf.domainConfig.userroot%>" rel="nofollow"><%=username%></a>
        <%}%>
        <span id="tipContainer"></span>
        &nbsp;&nbsp;<a href="<%=logoutUrl%>" target="_self">退出</a>
        <span id="pushNewsListContainer"></span>
    </script>
    <script type="text/template" id="pushNewsListTpl">
        <div class="pushNewsList">
            <%for(var i in group_by_type){%>
            <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
            <a href="<%=pushMsgMap[i].url%>"><%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%></a>
            <%}%>
            <%}%>
        </div>
    </script>


  <div data-component="detailHeader">
    <div class="header">
        <div class="menu clear">
            <div class="menuLeft">
                <a href="/ershoufang/" class="logo"></a>
                <!-- <span class="channelName">二手房</span> -->
                <ul class="typeList">
                                            <li >
                            <a href="/ershoufang/">在售</a>
                        </li>
                                            <li >
                            <a href="/chengjiao/">成交</a>
                        </li>
                                            <li class="selected">
                            <a href="/xiaoqu/">小区</a>
                        </li>
                                            <li >
                            <a href="https://map.ke.com/map/120000/ESF/">地图找房</a>
                        </li>
                                            <li >
                            <a href="/fapaifang/">法拍房</a>
                        </li>
                                    </ul>
            </div>
            <div class="search">
                <div class="input" log-mod="search">
                    <form action="/ershoufang/rs" id="searchForm">
                        <span class="noArrow" data-bl="switch">
                          <span class="state">在售</span>
                          <i></i>
                        </span>
                        <span class="sstate" data-bl="switch">
                            <span data-state="1">在售</span>
                            <span data-state="2">成交</span>
                            <span data-state="3">小区</span>
                        </span>
                        <input type="text" id="searchInput" placeholder="请输入关键字搜索" autocomplete="off">
                        <button type="submit" class="searchButton" data-bl="search" data-el="search">&nbsp;<i></i>&nbsp;
                        </button>
                    </form>
                    <div class="searchMsg" id="searchMsgContainer"></div>
                </div>
            </div>
        </div>
    </div>
    <div class="detailHeader VIEWDATA">
        <div class="title-wrapper" log-mod="detail_header">
            <div class="content">
                                    <span class="worth_position"></span>
                                <div class="title">
                    <h1 class="main" title="喜峰嘉园">
                        喜峰嘉园
                                            </h1>
                    <div class="sub">
                                                                                    (河北)
                                                                                        河北区铜陵路99号
                                                                        </div>
                </div>
                                    <div class="btnContainer ">
                        <div>
                            <div class="action">
                                <button id="follow" class="followbtn" data-text="关注小区">
                                    关注小区</button>
                                <span id="favCount" class="count">20</span>人关注
                                <span class="layer-qrcode followLayer" style="display: none;">
                        <span class="icon-qrcode">
                          <img width="100" height="100"
                               src="https://ajax.api.ke.com/qr/getDownloadQr?location=follow_app&jweb_channel_key=ershoufang_view"
                               alt="下载贝壳找房APP">
                        </span>
                        <span class="txt">下载贝壳找房APP</span>
                        <span class="sub-txt">房源动态早知道</span>
                        <span class="icon-close"></span>
                      </span>
                            </div>
                        </div>
                    </div>
                            </div>
        </div>
    </div>
    <div class="intro clear" mod-id="lj-common-bread">
        <div class="container">
            <div class="fl l-txt">
                                                            <a href="/">天津房产</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="/xiaoqu/">天津小区</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="https://tj.ke.com/xiaoqu/xinkaihe/">新开河小区</a>
                                                                <span class="stp">&nbsp;&gt;&nbsp;</span>
                                                                                <a href="/xiaoqu/12000000001175/">喜峰嘉园</a>
                                                                                        </div>
        </div>
    </div>
</div>
  <!-- 小区图片&相关信息 -->
  <div data-component="info">
    <div class="xiaoquOverview">
        <div class="xiaoquImg fl">
            <div class="xiaoquBigImg">
                <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" alt="喜峰嘉园户型图实景图" id="overviewBigImg" class="new-default-icon">
                <div class="imgDesc">查看剩余0张大图</div>
                <div class="overviewImgLoading"><span></span></div>
                            </div>
            <div class="xiaoquImgThumbnail clear">
                <div class="imgControllLeft fl disable" id="overviewImgLeft"><</div>
                <div class="imgControllRight fr" id="overviewImgRight">></div>
                <div class="imgThumbnailList">
                    <ol id="overviewThumbnail">
                                                                    </ol>
                </div>
            </div>
        </div>
        <div class="xiaoquDescribe fr">
            <div class="share">
                <span class="shareIcon"></span>分享此小区
                <div class="shareInfomation">
                    <img src="/api/getresblockqr?rid=12000000001175" alt="">
                    <div class="desc1">使用微信扫一扫</div>
                    <div class="desc2">查看小区信息分享给好友</div>
                </div>
            </div>
            <div class="xiaoquPrice clear">
                <div class="fl">
                                    <span class="xiaoquUnitPrice">20700</span>元/㎡<span class="xiaoquUnitPriceDesc">1月参考均价</span>
                                </div>
                
            </div>
            <div class="xiaoquInfo">
                <div class="xiaoquInfoItemMulty">
                    <div class="xiaoquInfoItemCol">
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">建筑类型</span>
                            <span class="xiaoquInfoContent">板楼</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">房屋总数</span>
                                                        <span class="xiaoquInfoContent">909户</span>
                                                    </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">楼栋总数</span>
                                                        <span class="xiaoquInfoContent">11栋</span>
                                                    </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">绿化率</span>
                            <span class="xiaoquInfoContent">
                                                                40%
                                                            </span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">容积率</span>
                            <span class="xiaoquInfoContent">
                                                                2
                                                            </span>
                        </div>
                                            </div>
                    <div class="xiaoquInfoItemCol">
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">交易权属</span>
                            <span class="xiaoquInfoContent">商品房/经济适用房/动迁安置房/限价商品房/乡产/私产/校产</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">建成年代</span>
                                                        <span class="xiaoquInfoContent">暂无信息 </span>
                                                    </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">供暖类型</span>
                            <span class="xiaoquInfoContent">集中供暖</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">用水类型</span>
                            <span class="xiaoquInfoContent">民水</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">用电类型</span>
                            <span class="xiaoquInfoContent">民电</span>
                        </div>
                                            </div>
                </div>
                <div class="xiaoquInfoItemOneLine">
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">物业费</span>
                        <span class="xiaoquInfoContent outer">
                                                2.2元/平米/月
                                                </span>
                    </div>
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">附近门店</span>
                        <span class="xiaoquInfoContent outer">
                                                                                <span mendian="117.190015,39.189294" xiaoqu="[117.19078502924,39.18840789505]" class="actshowMap">鼎山聚云峰喜峰嘉园店</span>/新开河街道古北道与南口路交口喜峰嘉园配建1-8 9 10 11-101
                                                                            </span>
                    </div>
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">物业公司</span>
                        <span class="xiaoquInfoContent outer">天津远洋物业管理有限公司</span>
                    </div>
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">开发商</span>
                        <span class="xiaoquInfoContent outer">远洋集团</span>
                    </div>
                </div>
            </div>
            
            <div id="100011295-100000036" class="ke-agent-sj-sdk component-agent-id-100011295" 
                data-resblock-id=""
            ></div>

            <!-- 钻石经纪人 -->
                            <div class="noData" style="display:none;">暂无相关经纪人，请直接联系客服  10106188</div>
                        <div class="download">
                <div class="qr-code">
                    <img width="94" height="94" src="https://ajax.api.ke.com/qr/getDownloadQr?location=right&ljweb_channel_key=xiaoqu_detail" alt="下载贝壳找房APP">
                    <span class="text">扫描下载APP 随时查看新房源</span>
                </div>
            </div>
        </div>
    </div>

    <!-- 图片大图模式 -->
        <div id="ditufloat" style="display:none">
        <div class="floatmap clear">
            <i class="close"></i>
            <div class="top clear">
            <div class="dis fl">
                <i class="icon1"></i>
                <span class="first">喜峰嘉园</span>
                <p class="second">河北新开河</p>
            </div>
            <span class="three">
                <i class="icon2"></i>
            </span>
            <div class="shop fl">
                <i class="icon3"></i>
                <span class="five">鼎山聚云峰喜峰嘉园店</span>
                <p class="six">新开河街道古北道与南口路交口喜峰嘉园配建1-8 9 10 11-101</p>
            </div>
            </div>
            <div class="mapcon">
            <div class="map" id="mapInitalize"></div>
            </div>
        </div>
    </div>
</div>
  <!-- fix导航  -->
              

<div data-component="fixedTabs" class="fixedContent">
  <div class="fixedTabs">
    <div class="fixedTabsContent">
              <a href="#goodSell">优质二手房</a>
              <a href="#frameDeal">小区成交记录</a>
              <a href="#around">周边配套</a>
          </div>
  </div>
</div>

  <div class="m-content">
    <div class="box-l xiaoquMainContent">
      <!-- 小区全部户型 -->
            <!-- 在售列表 -->
              <div data-component='sell' class="goodSell VIEWDATA" id="goodSell" data-view-evtid="12343" data-view-event="ModuleExpo"
     data-action="source_type=PC小区详情页二手房模块曝光">
    <div class="goodSellHeader clear">
        <h3 class="fl">喜峰嘉园优质二手房</h3>
        <a href="https://tj.ke.com/ershoufang/c12000000001175/" class="fr CLICKDATA" data-click-evtid="11968" data-click-event="WebClick"
           data-action="source_type=PC小区详情页同小区在售二手房查看全部点击">查看小区全部在售二手房</a>
    </div>
    <ol class="clear">
                                    <li class="fl CLICKDATA" data-click-evtid="11967" data-click-event="WebClick"
                    data-action="source_type=PC小区详情页同小区在售二手房卡片点击&click_position=0&housedel_id=101118208351">
                    <a target="_blank" href="https://tj.ke.com/ershoufang/101118208351.html" class="goodSellItemPic" title="喜峰嘉园 2室1厅 南">
                        <img class="lj-lazy" src='https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157'
                             data-original="https://ke-image.ljcdn.com/110000-inspection/pc1_PShgMkWyn_1.jpg!m_fill,w_280,h_210,f_jpg?from=ke.com"
                             alt="喜峰嘉园 2室1厅 南-天津喜峰嘉园二手房" title="喜峰嘉园 2室1厅 南">
                                                        <span class="goodSellItemPrice">¥152万</span>
                                                </a>
                    <div class="goodSellItemTitle"><a href="https://tj.ke.com/ershoufang/101118208351.html" title="喜峰嘉园 2室1厅 南">喜峰嘉园 2室1厅 南</a>
                    </div>
                    <div class="goodSellItemDesc">78.15平/2室1厅</div>
                </li>
                                                <li class="fl CLICKDATA" data-click-evtid="11967" data-click-event="WebClick"
                    data-action="source_type=PC小区详情页同小区在售二手房卡片点击&click_position=1&housedel_id=101121263661">
                    <a target="_blank" href="https://tj.ke.com/ershoufang/101121263661.html" class="goodSellItemPic" title="喜峰嘉园两室通透户型，业主家闲置房源，诚意出售">
                        <img class="lj-lazy" src='https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157'
                             data-original="https://ke-image.ljcdn.com/110000-inspection/pc1_u4U0GrMmn_1.jpg!m_fill,w_280,h_210,f_jpg?from=ke.com"
                             alt="喜峰嘉园两室通透户型，业主家闲置房源，诚意出售-天津喜峰嘉园二手房" title="喜峰嘉园两室通透户型，业主家闲置房源，诚意出售">
                                                        <span class="goodSellItemPrice">¥149万</span>
                                                </a>
                    <div class="goodSellItemTitle"><a href="https://tj.ke.com/ershoufang/101121263661.html" title="喜峰嘉园两室通透户型，业主家闲置房源，诚意出售">喜峰嘉园两室通透户型，业主家闲置房源，诚意出售</a>
                    </div>
                    <div class="goodSellItemDesc">78.14平/2室1厅</div>
                </li>
                                                <li class="fl CLICKDATA" data-click-evtid="11967" data-click-event="WebClick"
                    data-action="source_type=PC小区详情页同小区在售二手房卡片点击&click_position=2&housedel_id=101120836570">
                    <a target="_blank" href="https://tj.ke.com/ershoufang/101120836570.html" class="goodSellItemPic" title="喜峰嘉园  精装修  H户型 满两年税费低 采光好">
                        <img class="lj-lazy" src='https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157'
                             data-original="https://ke-image.ljcdn.com/110000-inspection/pc1_R1OpZ5Oym_1.jpg!m_fill,w_280,h_210,f_jpg?from=ke.com"
                             alt="喜峰嘉园  精装修  H户型 满两年税费低 采光好-天津喜峰嘉园二手房" title="喜峰嘉园  精装修  H户型 满两年税费低 采光好">
                                                        <span class="goodSellItemPrice">¥204万</span>
                                                </a>
                    <div class="goodSellItemTitle"><a href="https://tj.ke.com/ershoufang/101120836570.html" title="喜峰嘉园  精装修  H户型 满两年税费低 采光好">喜峰嘉园  精装修  H户型 满两年税费低 采光好</a>
                    </div>
                    <div class="goodSellItemDesc">89.98平/2室1厅</div>
                </li>
                        </ol>
</div>
            <!-- 徐州隐藏成交记录列表 -->
              <div data-component="deal">
    <div class="frameDeal VIEWDATA" id="frameDeal" data-view-evtid="12345" data-view-event="ModuleExpo" data-action="source_type=PC小区详情页全部成交模块曝光">
        <h3 class="frameDealHeader">喜峰嘉园小区成交记录</h3>
        <div class="frameDealList">
            <div class="frameDealListHeader">
            <div class="frameDealInfo">房屋户型</div>
            <div class="frameDealArea">面积</div>
            <div class="frameDealDate">签约日期</div>
            <div class="frameDealPrice">成交价</div>
            <div class="frameDealUnitPrice">成交单价</div>
                        </div>
            <ol class="frameDealListItem">
                                                <li>
                                                <div class="frameDealInfo">
                            <a target="_blank" href="https://tj.ke.com/chengjiao/101118446471.html" class="frameDealImg">
                                <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-frame/standard_23d2b8b0-bb7a-46dd-866c-9fcedbcce1a3.png.280x210.jpg?from=ke.com" alt="1室1厅-天津喜峰嘉园二手房">
                            </a>
                            <div class="frameDealDesc">
                                <a target="_blank" href="https://tj.ke.com/chengjiao/101118446471.html" class="frameDealTitle">1室1厅</a>
                                <div class="frameDealFloor">低楼层/18层&nbsp;南</div>
                                <div class="frameDealResblock">暂无信息</div>
                            </div>
                        </div>
                        <div class="frameDealArea">61.06平米</div>
                        <div class="frameDealDate">2023-10-06</div>
                        <div class="frameDealPrice">
                                                                                            107万
                                                                                    </div>
                        <div class="frameDealUnitPrice">
                            <!-- 成交价为暂无或者隐藏展示时，成交单价字段引导用户在线咨询经纪人 -->
                                                            17524元/平                                                    </div>
                                            </li>
                                                                <li>
                                                <div class="frameDealInfo">
                            <a target="_blank" href="https://tj.ke.com/chengjiao/101118215340.html" class="frameDealImg">
                                <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-frame/standard_3b053778-d5ca-4113-ab68-b9f956fa3025.png.280x210.jpg?from=ke.com" alt="3室2厅-天津喜峰嘉园二手房">
                            </a>
                            <div class="frameDealDesc">
                                <a target="_blank" href="https://tj.ke.com/chengjiao/101118215340.html" class="frameDealTitle">3室2厅</a>
                                <div class="frameDealFloor">高楼层/8层&nbsp;南 北</div>
                                <div class="frameDealResblock">暂无信息</div>
                            </div>
                        </div>
                        <div class="frameDealArea">90.66平米</div>
                        <div class="frameDealDate">2023-09-10</div>
                        <div class="frameDealPrice">
                                                                                            191万
                                                                                    </div>
                        <div class="frameDealUnitPrice">
                            <!-- 成交价为暂无或者隐藏展示时，成交单价字段引导用户在线咨询经纪人 -->
                                                            21068元/平                                                    </div>
                                            </li>
                                                                <li>
                                                <div class="frameDealInfo">
                            <a target="_blank" href="https://tj.ke.com/chengjiao/101119061245.html" class="frameDealImg">
                                <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-frame/standard_8c390f67-8818-4244-a5fa-3a067f199adf.png.280x210.jpg?from=ke.com" alt="1室1厅-天津喜峰嘉园二手房">
                            </a>
                            <div class="frameDealDesc">
                                <a target="_blank" href="https://tj.ke.com/chengjiao/101119061245.html" class="frameDealTitle">1室1厅</a>
                                <div class="frameDealFloor">高楼层/18层&nbsp;南 北</div>
                                <div class="frameDealResblock">暂无信息</div>
                            </div>
                        </div>
                        <div class="frameDealArea">59平米</div>
                        <div class="frameDealDate">2023-06-21</div>
                        <div class="frameDealPrice">
                                                                                            82.3万
                                                                                    </div>
                        <div class="frameDealUnitPrice">
                            <!-- 成交价为暂无或者隐藏展示时，成交单价字段引导用户在线咨询经纪人 -->
                                                            13950元/平                                                    </div>
                                            </li>
                                        </ol>
        </div>
            </div>
    <!-- 成交点击弹出的二维码 -->

    <div class="download_layer" data-component="dealToDownload">
    <div class="download_layer_ewmframe">
        <span class="close black">&times</span>
        <img src="https://ajax.api.ke.com/qr/getDownloadQr?location=list&ljweb_channel_key=xiaoquchengjiao"/>
        <p class="gray">
            查看最新成交价格
        </p>
        <p class="gray">
            下载贝壳找房APP
        </p>
    </div>
</div>
</div>
            <!-- 徐州隐藏联系经纪人 -->
        <div data-component="agentList" class="brokerList VIEWDATA" id="brokerList" log-mod="xiaoqu_detail_diamond-many" data-view-evtid="12346" data-view-event="ModuleExpo" data-action="source_type=PC小区详情页联系经纪人模块曝光">
    <div class="broheader">
        <h3 class="title">联系经纪人</h3>
        <span class="subTitle">您可以通过电话联系经纪人</span>
        <!--  -->
    </div>

    <div id="100011296-100000036" class="ke-agent-sj-sdk component-agent-id-100011296" 
        data-resblock-id=""
    ></div>

    <ul style="display: none">
        </ul>
</div>
      <!-- 徐州隐藏正在出租 -->
              <div data-component="chuzu" class="rentList">
    <div class="rentListHeader clear">
        <h3 class="rentListTitle fl">喜峰嘉园正在出租</h3>
        <a href="http://tj.zu.ke.com/zufang/c12000000001175/" class="fr">查看小区全部出租房</a>
    </div>
    <div class="rentListContent clear">
                    <div class="rentItem fl">
                <a target="_blank" href="http://tj.zu.ke.com/zufang/TJ1859454272282820608.html" class="rentItemImg" title="整租·喜峰嘉园 3室1厅 南/北"> 
                <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/110000-inspection/10675c39-7665-44b5-8361-41a5fcd19c7b.jpg.280x210.jpg" alt="整租·喜峰嘉园 3室1厅 南/北-天津喜峰嘉园租房" title="整租·喜峰嘉园 3室1厅 南/北">
                                </a>
                <div class="rentItemTitle"><a target="_blank" href="http://tj.zu.ke.com/zufang/TJ1859454272282820608.html" title="整租·喜峰嘉园 3室1厅 南/北">整租·喜峰嘉园 3室1厅 南/北</a></div>
                <div class="rentItemInfo clear">
                <div class="rentItemRoom fl">91.00平/3室1厅1卫</div>
                <div class="rentItemPrice fr"><span>3200</span>元/月</div>
                </div>
            </div>
                    <div class="rentItem fl">
                <a target="_blank" href="http://tj.zu.ke.com/zufang/TJ1858043945368420352.html" class="rentItemImg" title="整租·喜峰嘉园 2室1厅 南/北"> 
                <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/110000-inspection/pc1_df6C1dybE.jpg.280x210.jpg" alt="整租·喜峰嘉园 2室1厅 南/北-天津喜峰嘉园租房" title="整租·喜峰嘉园 2室1厅 南/北">
                                </a>
                <div class="rentItemTitle"><a target="_blank" href="http://tj.zu.ke.com/zufang/TJ1858043945368420352.html" title="整租·喜峰嘉园 2室1厅 南/北">整租·喜峰嘉园 2室1厅 南/北</a></div>
                <div class="rentItemInfo clear">
                <div class="rentItemRoom fl">89.00平/2室1厅1卫</div>
                <div class="rentItemPrice fr"><span>3000</span>元/月</div>
                </div>
            </div>
                    <div class="rentItem fl">
                <a target="_blank" href="http://tj.zu.ke.com/zufang/TJ1831990925245546496.html" class="rentItemImg" title="整租·喜峰嘉园 2室1厅 南/北"> 
                <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/110000-inspection/pc1_9mIwpEEmE.jpg.280x210.jpg" alt="整租·喜峰嘉园 2室1厅 南/北-天津喜峰嘉园租房" title="整租·喜峰嘉园 2室1厅 南/北">
                                </a>
                <div class="rentItemTitle"><a target="_blank" href="http://tj.zu.ke.com/zufang/TJ1831990925245546496.html" title="整租·喜峰嘉园 2室1厅 南/北">整租·喜峰嘉园 2室1厅 南/北</a></div>
                <div class="rentItemInfo clear">
                <div class="rentItemRoom fl">79.00平/2室1厅1卫</div>
                <div class="rentItemPrice fr"><span>1900</span>元/月</div>
                </div>
            </div>
            </div>
</div>          </div>
    <!-- 金牌经纪人fix -->
    <div data-component="goldAgent" class="box-r fixedAgent" log-mod="xiaoqu_detail_diamond-first" >
    <div class="fixedAgentMain" >
        <div class="fixedRelationInfo clear">
            <div class="fl">小区顾问</div>
            <div class="fr"><a>喜峰嘉园</a></div>
            </div>
    
        <div class="component-agent-id-100011295-bk"
        ></div>

        <button class="btn-large followFrameBtn followbtn" data-role="followBtn">关注小区</button>
        <div class="followedLine"></div>
        <div class="followedDesc">
        <span class="followedDescContent">已有<span data-role="followNumber">20</span>人关注此小区</span>
        </div>
    </div>
</div>
    <div class="xiaoquAround">
      <!-- 周边配套 -->
      <div data-component="mapCard" class="around" id="around">
  <h2 class="aroundTitle">喜峰嘉园周边配套</h2>
  <div class="aroundContainer">
    <div class="aroundMap" id="map">
    </div>
    <div class="tabBox">
      <ul class="aroundType">
        <li class="LOGCLICK" data-log_evtid='10242'  data-bl="traffic" data-key="地铁站,公交站" data-index="subway,bus" data-length="10,10">交通</li>
                  <li class="LOGCLICK" data-log_evtid='10242'  data-bl="education" data-key="幼儿园,小学,中学,大学"
              data-index="kindergarten,primary-school,middle-school,University"
              data-length="5,5,5,5"
          >教育</li>
                <li class="LOGCLICK" data-log_evtid='10242'  data-bl="medical" data-key="医院,药店" data-index="hospital,pharmacy" data-length="10,10">医疗</li>
        <li class="LOGCLICK" data-log_evtid='10242'  data-bl="shopping" data-key="商场,超市,市场" data-index="mall,supermarket,market" data-length="7,7,6">购物</li>
        <li class="LOGCLICK" data-log_evtid='10242'  data-bl="life" data-key="银行,ATM,餐厅,咖啡馆" data-index="bank,atm,restaurant,coffee" data-length="5,5,5,5">生活</li>
        <li class="LOGCLICK" data-log_evtid='10242'  data-bl="entertainment" data-key="公园,电影院,健身房,体育馆" data-index="park,cinema,gym,sport" data-length="5,5,5,5">娱乐</li>
      </ul>
      <div class="itemTagBox"></div>
      <div class="aroundList" id="mapListContainer"></div>
      <div class="loading">
        <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/loading.gif?_v=202401081627157" class="loadingImg">
        <span class="loadingText">努力加载中...</span>
      </div>
    </div>
  </div>
</div>

<script type='text/template' id="mapListTpl">
<div class="name"><%=keyword%></div>
<ul>
  <%for(var i = 0;i < list.length;i++){%>
  <li data-index="<%=i%>">
    <i>&#<%=i+65%>;</i>
    <div class="item">
      <div class="itemTitle"><%=list[i].title%></div>
      <div class="itemInfo"><%=list[i].address%></div>
    </div>
  </li>
  <%}%>
</ul>
</script>
      <!-- 附近小区 -->
              <div data-component="nearby" class="nearby" id="nearby">
    <div class="nearbyHeader clear">
        <h3 class="nearByTitle fl">喜峰嘉园附近小区</h3>
        <a href="https://tj.ke.com/xiaoqu/xinkaihe/" class="fr" style="display: none;">查看同商圈小区</a>
    </div>
    <div class="nearbyList clear">
                <div class="nearbyItem fl">
            <a target="_blank" href="https://tj.ke.com/xiaoqu/2811052354990/">
            <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-resblock/2faa74d7-494c-43f4-8e4b-f9cc4af0c738.JPG.170x125.jpg" alt="万隆桃香园" title="万隆桃香园">
            <div class="bg"></div>
            <div class="desc">
                <div class="nearbyItemTitle">万隆桃香园</div>
                <div class="nearbyItemType">
                <span>
                                        11830元/㎡
                                    </span>
                </div>
            </div>
            </a>
        </div>
                <div class="nearbyItem fl">
            <a target="_blank" href="https://tj.ke.com/xiaoqu/1211046633997/">
            <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-resblock/34adaa95-e1e9-474a-80a5-286730fdd7bb.jpg.170x125.jpg" alt="风采里" title="风采里">
            <div class="bg"></div>
            <div class="desc">
                <div class="nearbyItemTitle">风采里</div>
                <div class="nearbyItemType">
                <span>
                                        15360元/㎡
                                    </span>
                </div>
            </div>
            </a>
        </div>
                <div class="nearbyItem fl">
            <a target="_blank" href="https://tj.ke.com/xiaoqu/1220075280507675/">
            <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original=".170x125.jpg" alt="天和丽园" title="天和丽园">
            <div class="bg"></div>
            <div class="desc">
                <div class="nearbyItemTitle">天和丽园</div>
                <div class="nearbyItemType">
                <span>
                                        11816元/㎡
                                    </span>
                </div>
            </div>
            </a>
        </div>
                <div class="nearbyItem fl">
            <a target="_blank" href="https://tj.ke.com/xiaoqu/1211047089204/">
            <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-resblock/c3b8a3ee-7a00-4bcc-a33e-6bcf177b32f8.jpg.170x125.jpg" alt="桃花园南里" title="桃花园南里">
            <div class="bg"></div>
            <div class="desc">
                <div class="nearbyItemTitle">桃花园南里</div>
                <div class="nearbyItemType">
                <span>
                                        16490元/㎡
                                    </span>
                </div>
            </div>
            </a>
        </div>
                <div class="nearbyItem fl">
            <a target="_blank" href="https://tj.ke.com/xiaoqu/1211046135166/">
            <img class="lj-lazy" src="https://s1.ljcdn.com/pegasus/redskull/images/common/blank.gif?_v=202401081627157" data-original="https://ke-image.ljcdn.com/hdic-resblock/ea174489-6a68-486c-b5cf-3205acfb0f16.JPG.170x125.jpg" alt="仁恒河滨花园" title="仁恒河滨花园">
            <div class="bg"></div>
            <div class="desc">
                <div class="nearbyItemTitle">仁恒河滨花园</div>
                <div class="nearbyItemType">
                <span>
                                        40599元/㎡
                                    </span>
                </div>
            </div>
            </a>
        </div>
            </div>
</div>          </div>
  </div>

  <!-- 业主模块 -->
    <!-- 小区下架处理 -->
    <div class="disclaimer">
    <h1>1. 小区介绍中的周边配套、在建设施、规划设施、地铁信息、建筑类型、物业费用等信息为通过物业介绍、房产证、实勘、政府官网等渠道获取，因时间、政策会发生变化，与实际情况可能略有偏差，仅供参考。</h1>
    <h1>2.小区介绍中与距离相关的数据均来源于百度地图。</h1>
  </div>

  <!--
 * @Descripttion:
 * @version:
 * @Author: zhoumeiyan
 * @Date: 2021-05-20 15:35:25
 * @LastEditors: zhoumeiyan
 * @LastEditTime: 2021-05-21 16:00:52
-->
<div class="footer">
  <div class="wrapper">
    <div class="f-title">
      <div class="fl">
        <ul>
                    <li>
            <a href="https://open.ke.com/home" >开放平台 </a> </li>           <li>
            <a href="https://kol.ke.com/" >贝壳号 </a> </li>           <li>
            <a href="https://tj.ke.com/sitemap/" >网站地图 </a> </li>           <li>
            <a href="https://about.ke.com/introduce/index.html" >了解贝壳 </a> </li>           <li>
            <a href="https://investors.ke.com" >投资者关系 / Investors </a> </li>  </ul> </div> <a href="javascript:;" class="fr req_btn">
              官方客服咨询
            </a>
      </div>
      <div class="lianjia-link-box">
        <div class="fl">
          <div class="tab">
                        <span  class="hover" >热门小区 </span>             <span >商圈小区 </span>             <span >城市二手房 </span>             <span >城市小区 </span>             <span >城市楼盘 </span>             <span >贝壳规则中心 </span>  </div> <div
              class="link-list">
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045583007/">懿德园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220030387408351/">天宝新苑小区一期</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220030285395687/">军秀园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1220025006980400/">实地·海棠雅著</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045555771/">怡安温泉公寓</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045563732/">程林东里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211046466574/">宜天花园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211046850259/">裕德里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211100197260/">中环福境</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045640370/">北斗花园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211063764608/">宝庆里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211099888438/">社会山Bigparty</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045865764/">东锦里</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1210660951371530/">金地艺城瑞府</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/12000000000344/">龙瀚南园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045662005/">紫玉园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045415639/">水木天成阁林园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211100678638/">福锦园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/1211045778977/">大地十二城枫桥园</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/2811052386803/">金地格林世界梧桐苑B区</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/nanyingmenjie/">南营门街小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/nanshi/">南市小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/quanyechang/">劝业场小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/xiaobailou/">小白楼小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/tiyuguanjie/">体育馆街小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/xinxingjie/">新兴街小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/tangjiakou/">唐家口小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/xiangyanglou/">向阳楼小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/wanxincun/">万新村小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/dawangzhuang/">大王庄小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/zhenlidao/">真理道小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/shanghanglu/">上杭路小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/taiyangcheng/">太阳城小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/chunhuajie/">春华街小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/changzhoudao/">常州道小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/fuminlu/">富民路小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/zhongshanmenjie/">中山门街小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/lushandao/">鲁山道小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/dazhigu/">大直沽小区</a>
                                        <a target="_blank" href="https://tj.ke.com/xiaoqu/erhaoqiaojie/">二号桥街小区</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://cc.ke.com/ershoufang/">长春二手房
</a>
                                        <a target="_blank" href="https://cq.ke.com/ershoufang/">重庆二手房
</a>
                                        <a target="_blank" href="https://cs.ke.com/ershoufang/">长沙二手房
</a>
                                        <a target="_blank" href="https://dl.ke.com/ershoufang/">大连二手房
</a>
                                        <a target="_blank" href="https://fs.ke.com/ershoufang/">佛山二手房
</a>
                                        <a target="_blank" href="https://gz.ke.com/ershoufang/">广州二手房
</a>
                                        <a target="_blank" href="https://hf.ke.com/ershoufang/">合肥二手房
</a>
                                        <a target="_blank" href="https://hz.ke.com/ershoufang/">杭州二手房
</a>
                                        <a target="_blank" href="https://jn.ke.com/ershoufang/">济南二手房
</a>
                                        <a target="_blank" href="https://nj.ke.com/ershoufang/">南京二手房
</a>
                                        <a target="_blank" href="https://sjz.ke.com/ershoufang/">石家庄二手房
</a>
                                        <a target="_blank" href="https://su.ke.com/ershoufang/">苏州二手房
</a>
                                        <a target="_blank" href="https://wh.ke.com/ershoufang/">武汉二手房
</a>
                                        <a target="_blank" href="https://wx.ke.com/ershoufang/">无锡二手房
</a>
                                        <a target="_blank" href="https://xa.ke.com/ershoufang/">西安二手房
</a>
                                        <a target="_blank" href="https://xm.ke.com/ershoufang/">厦门二手房
</a>
                                        <a target="_blank" href="https://xz.ke.com/ershoufang/">徐州二手房
</a>
                                        <a target="_blank" href="https://yt.ke.com/ershoufang/">烟台二手房
</a>
                                        <a target="_blank" href="https://zh.ke.com/ershoufang/">珠海二手房
</a>
                                        <a target="_blank" href="https://zz.ke.com/ershoufang/">郑州二手房
</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://bj.ke.com/xiaoqu/">北京小区
</a>
                                        <a target="_blank" href="https://cc.ke.com/xiaoqu/">长春小区
</a>
                                        <a target="_blank" href="https://cd.ke.com/xiaoqu/">成都小区
</a>
                                        <a target="_blank" href="https://cq.ke.com/xiaoqu/">重庆小区
</a>
                                        <a target="_blank" href="https://cs.ke.com/xiaoqu/">长沙小区
</a>
                                        <a target="_blank" href="https://dg.ke.com/xiaoqu/">东莞小区
</a>
                                        <a target="_blank" href="https://dl.ke.com/xiaoqu/">大连小区
</a>
                                        <a target="_blank" href="https://fs.ke.com/xiaoqu/">佛山小区
</a>
                                        <a target="_blank" href="https://gz.ke.com/xiaoqu/">广州小区
</a>
                                        <a target="_blank" href="https://hk.ke.com/xiaoqu/">海口小区
</a>
                                        <a target="_blank" href="https://hui.ke.com/xiaoqu/">惠州小区
</a>
                                        <a target="_blank" href="https://jn.ke.com/xiaoqu/">济南小区
</a>
                                        <a target="_blank" href="https://lf.ke.com/xiaoqu/">廊坊小区
</a>
                                        <a target="_blank" href="https://qd.ke.com/xiaoqu/">青岛小区
</a>
                                        <a target="_blank" href="https://su.ke.com/xiaoqu/">苏州小区
</a>
                                        <a target="_blank" href="https://sy.ke.com/xiaoqu/">沈阳小区
</a>
                                        <a target="_blank" href="https://wh.ke.com/xiaoqu/">武汉小区
</a>
                                        <a target="_blank" href="https://wx.ke.com/xiaoqu/">无锡小区
</a>
                                        <a target="_blank" href="https://xm.ke.com/xiaoqu/">厦门小区
</a>
                                        <a target="_blank" href="https://xz.ke.com/xiaoqu/">徐州小区
</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://bj.fang.ke.com/loupan/">北京楼盘
</a>
                                        <a target="_blank" href="https://cc.fang.ke.com/loupan/">长春楼盘
</a>
                                        <a target="_blank" href="https://cq.fang.ke.com/loupan/">重庆楼盘
</a>
                                        <a target="_blank" href="https://hf.fang.ke.com/loupan/">合肥楼盘
</a>
                                        <a target="_blank" href="https://hz.fang.ke.com/loupan/">杭州楼盘
</a>
                                        <a target="_blank" href="https://jn.fang.ke.com/loupan/">济南楼盘
</a>
                                        <a target="_blank" href="https://km.fang.ke.com/loupan/">昆明楼盘
</a>
                                        <a target="_blank" href="https://nc.fang.ke.com/loupan/">南昌楼盘
</a>
                                        <a target="_blank" href="https://nj.fang.ke.com/loupan/">南京楼盘
</a>
                                        <a target="_blank" href="https://qd.fang.ke.com/loupan/">青岛楼盘
</a>
                                        <a target="_blank" href="https://sh.fang.ke.com/loupan/">上海楼盘
</a>
                                        <a target="_blank" href="https://sjz.fang.ke.com/loupan/">石家庄楼盘
</a>
                                        <a target="_blank" href="https://sy.fang.ke.com/loupan/">沈阳楼盘
</a>
                                        <a target="_blank" href="https://tj.fang.ke.com/loupan/">天津楼盘
</a>
                                        <a target="_blank" href="https://ty.fang.ke.com/loupan/">太原楼盘
</a>
                                        <a target="_blank" href="https://wh.fang.ke.com/loupan/">武汉楼盘
</a>
                                        <a target="_blank" href="https://wx.fang.ke.com/loupan/">无锡楼盘
</a>
                                        <a target="_blank" href="https://xm.fang.ke.com/loupan/">厦门楼盘
</a>
                                        <a target="_blank" href="https://yt.fang.ke.com/loupan/">烟台楼盘
</a>
                                        <a target="_blank" href="https://zz.fang.ke.com/loupan/">郑州楼盘
</a>
                                      </dd>
                </dl>
              </div>
                            <div>
                <dl>
                  <dd>
                                        <a target="_blank" href="https://www.ke.com/zhuanti/protocol">贝壳找房隐私声明 正文</a>
                                        <a target="_blank" href="https://www.ke.com/zhuanti/serviceProtocol">贝壳平台服务使用协议</a>
                                        <a target="_blank" href="https://rules-center.ke.com">贝壳规则中心</a>
                                      </dd>
                </dl>
              </div>
                        </div>
        </div>
        <div class="clear"></div>
      </div>
      <ul class="partner-logo">
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=招商银行">
                    <a target="_blank" href="https://image1.ljcdn.com/materials/appindexconf/8f9822cf882e6f263b81f7a394dd0712.jpg">
            <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/partner/zsyh.png?_v=20191219184206415" title="招商银行" alt="招商银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=上海银行">
                    <a target="_blank" href="https://img.ljcdn.com/beike/PC/1624330009091.jpg">
            <img src="https://image1.ljcdn.com/materials/appindexconf/57f25e75780b61e27a74a8a5adc7586a.jpg" title="上海银行" alt="上海银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=中国光大银行">
                    <a target="_blank" href="https://image1.ljcdn.com/materials/appindexconf/2d8668bfc893536176d1462378e1cbd7.jpg">
            <img src="https://image1.ljcdn.com/materials/appindexconf/ea3bcafededbafe865f986d01c6030a3.png" title="中国光大银行" alt="中国光大银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=华夏银行">
                    <a target="_blank" href="https://img.ljcdn.com/beike/beike/1592276474011.png">
            <img src="https://image1.ljcdn.com/materials/appindexconf/369f029b0449e76b616c1920f18774ed.png" title="华夏银行" alt="华夏银行">
          </a>
                  </li>
                <li class="CLICKDATA VIEWDATA" data-view-evtid="27043" data-view-event="ItemExpo" data-click-evtid="27044"
          data-click-event="WebClick" data-action="click_value=北京农商银行">
                    <a target="_blank" href="https://img.ljcdn.com/beike/PC/1631518116390.jpg">
            <img src="https://image1.ljcdn.com/materials/appindexconf/4f590a93d92909b167d428b2f45d5274.jpg" title="北京农商银行" alt="北京农商银行">
          </a>
                  </li>
              </ul>
      <div class="bottom">
        <div class="copyright fl">
                    天津小屋信息科技有限公司 | 地址：天津经济技术开发区南港工业区综合服务区办公楼C座一层112室09单元 | 电话：10106188 | <a target="_blank"
            href="http://beian.miit.gov.cn/">津ICP备18000836号-1</a> | © Copyright 2024 ke.com版权所有
          | <a target="_blank" href="//file.ljcdn.com/bigc-file2cdn/Mensa/1585731661478.pdf">营业执照</a>
                    | <a target="_blank" href="//file.ljcdn.com/bigc-file2cdn/Mensa/1585732230759.pdf">ICP证</a>
          | <a target="_blank"
            href="https://www.ke.com/zhuanti/commonProtocol?id=1dc38816524dffa9da7949856540d168">贝壳平台知识产权保护</a>
          <br>
          老年人客服热线：010-60640529<br>
          违法和不良信息举报电话：010-86440676| 违法和不良信息举报邮箱：jubaoyouxiang@ke.com <br>
          涉未成年人举报电话：010-86440676| 涉未成年人举报邮箱：jubaoyouxiang@ke.com
          <br>
          <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/beian.png?_v=202401081627157" alt="beian" style="display: inline-block;height: 20px;width: auto;">
          <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=12010602120282">津公网安备
            12010602120282号</a> |
          <a target="_blank" href="//www.12377.cn">网上有害信息举报专区</a>
        </div>
      </div>
    </div>
  </div>
  
</div>
<div id="only" data-city="tj" data-page="xiaoqu_detail"></div><script type="text/javascript" src="https://s1.ljcdn.com/pegasus/redskull/deps/jquery_lj_0_1.js?_v=202401081627157" crossorigin="anonymous"></script><script src='https://file.ljcdn.com/nebula/index_1687226806824.js' crossorigin="anonymous"></script>
<script>if (window.require) {var path = 'https://s1.ljcdn.com/pegasus/pc/asset?_v=202401081627157'.split("?");require.config({baseUrl: path[0],paths: {'echarts': '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar': '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line': '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie': '../../dep/echarts-1.4.1/build/echarts','echarts3': '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs: path[1]});}var feData = {"cityName": "北京","getFavHouseUrl": "/api/gethousefav","setFavHouseUrl": "/api/sethousefav","getLastSearch": "/api/getlastsearch","getCommunityHistory": "/api/getcommunityhistory","verifyHouse": "/api/verifyHouse","getUser": "/api/getUser","verifyCode": "/api/getVerifyCode","complaint": "/api/complaint","getDecoration": "/api/getDecoration","trendData": "/site/getpicinfo"}</script>
<script type="text/javascript" src="https://s1.ljcdn.com/pegasus/redskull/js/xiaoquDetail/index.js?_v=202401081627157" crossorigin="anonymous"></script>
<script type="text/javascript">
  window.GLOBAL_INFOS = {
    id:12000000001175,
    resblockPosition:'117.19078502924,39.18840789505',
    resblockName:'喜峰嘉园',
    resblockId: '12000000001175',
    cityId: '120000',
    others: {"name":"\u559c\u5cf0\u5609\u56ed","resblockId":12000000001175,"favCount":20,"minTenement":2.2,"maxTenement":2.2,"buildingCount":11,"houseAmount":909,"curbageRate":2,"greenRate":40,"address":"\u6cb3\u5317\u533a\u94dc\u9675\u8def99\u53f7","buildingType":"\u677f\u697c","buildYear":"\u6682\u65e0\u4fe1\u606f","property":"\u5929\u6d25\u8fdc\u6d0b\u7269\u4e1a\u7ba1\u7406\u6709\u9650\u516c\u53f8","developer":"\u8fdc\u6d0b\u96c6\u56e2","agentShop":"\u9f0e\u5c71\u805a\u4e91\u5cf0\u559c\u5cf0\u5609\u56ed\u5e97","shopAddress":"\u65b0\u5f00\u6cb3\u8857\u9053\u53e4\u5317\u9053\u4e0e\u5357\u53e3\u8def\u4ea4\u53e3\u559c\u5cf0\u5609\u56ed\u914d\u5efa1-8 9 10 11-101","shopDistance":"119m","shopPosition":"117.190015,39.189294","district":"\u6cb3\u5317","districtUrl":"https:\/\/tj.ke.com\/xiaoqu\/hebei\/","bizcircle":"\u65b0\u5f00\u6cb3","bizcircleUrl":"https:\/\/tj.ke.com\/xiaoqu\/xinkaihe\/","coordinates":"117.19078502924,39.18840789505","unitPrice":20700,"bdaTime":"1\u6708","houseSellNum":21,"dealProperties":"\u5546\u54c1\u623f\/\u7ecf\u6d4e\u9002\u7528\u623f\/\u52a8\u8fc1\u5b89\u7f6e\u623f\/\u9650\u4ef7\u5546\u54c1\u623f\/\u4e61\u4ea7\/\u79c1\u4ea7\/\u6821\u4ea7","priceDesc":"\u53c2\u8003\u5747\u4ef7","electricType":"\u6c11\u7535","heatingType":"\u96c6\u4e2d\u4f9b\u6696","waterType":"\u6c11\u6c34","isSellPrice":2,"priceUnitAvgGov":0},
    father_others: {"subNav":[{"title":"\u5728\u552e","url":"\/ershoufang\/","current":false,"isNew":false},{"title":"\u6210\u4ea4","url":"\/chengjiao\/","current":false,"isNew":true},{"title":"\u5c0f\u533a","url":"\/xiaoqu\/","current":1,"isNew":false},{"title":"\u5730\u56fe\u627e\u623f","url":"https:\/\/map.ke.com\/map\/120000\/ESF\/","current":false,"isNew":false},{"title":"\u6cd5\u62cd\u623f","url":"\/fapaifang\/","current":false,"isNew":false}],"abstract":{"name":"\u559c\u5cf0\u5609\u56ed","resblockId":12000000001175,"favCount":20,"minTenement":2.2,"maxTenement":2.2,"buildingCount":11,"houseAmount":909,"curbageRate":2,"greenRate":40,"address":"\u6cb3\u5317\u533a\u94dc\u9675\u8def99\u53f7","buildingType":"\u677f\u697c","buildYear":"\u6682\u65e0\u4fe1\u606f","property":"\u5929\u6d25\u8fdc\u6d0b\u7269\u4e1a\u7ba1\u7406\u6709\u9650\u516c\u53f8","developer":"\u8fdc\u6d0b\u96c6\u56e2","agentShop":"\u9f0e\u5c71\u805a\u4e91\u5cf0\u559c\u5cf0\u5609\u56ed\u5e97","shopAddress":"\u65b0\u5f00\u6cb3\u8857\u9053\u53e4\u5317\u9053\u4e0e\u5357\u53e3\u8def\u4ea4\u53e3\u559c\u5cf0\u5609\u56ed\u914d\u5efa1-8 9 10 11-101","shopDistance":"119m","shopPosition":"117.190015,39.189294","district":"\u6cb3\u5317","districtUrl":"https:\/\/tj.ke.com\/xiaoqu\/hebei\/","bizcircle":"\u65b0\u5f00\u6cb3","bizcircleUrl":"https:\/\/tj.ke.com\/xiaoqu\/xinkaihe\/","coordinates":"117.19078502924,39.18840789505","unitPrice":20700,"bdaTime":"1\u6708","houseSellNum":21,"dealProperties":"\u5546\u54c1\u623f\/\u7ecf\u6d4e\u9002\u7528\u623f\/\u52a8\u8fc1\u5b89\u7f6e\u623f\/\u9650\u4ef7\u5546\u54c1\u623f\/\u4e61\u4ea7\/\u79c1\u4ea7\/\u6821\u4ea7","priceDesc":"\u53c2\u8003\u5747\u4ef7","electricType":"\u6c11\u7535","heatingType":"\u96c6\u4e2d\u4f9b\u6696","waterType":"\u6c11\u6c34","isSellPrice":2,"priceUnitAvgGov":0},"is_bk":false,"bigPic":[],"picNum":0,"panorama":null,"sold":[{"houseId":"101118446471","viewUrl":"https:\/\/tj.ke.com\/chengjiao\/101118446471.html","source":"","jushi":"1\u5ba41\u5385","area":61.06,"resblockName":"\u559c\u5cf0\u5609\u56ed","floorStat":"\u4f4e\u697c\u5c42","totalFloor":"18","signTime":"2023-10-06","isSold":1,"orientation":"\u5357","isDisplay":1,"signSource":"","buildYear":"\u6682\u65e0\u4fe1\u606f","title":"\u559c\u5cf0\u5609\u56ed","price":107,"unitPrice":17524,"imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_23d2b8b0-bb7a-46dd-866c-9fcedbcce1a3.png.280x210.jpg?from=ke.com"},{"houseId":"101118215340","viewUrl":"https:\/\/tj.ke.com\/chengjiao\/101118215340.html","source":"","jushi":"3\u5ba42\u5385","area":90.66,"resblockName":"\u559c\u5cf0\u5609\u56ed","floorStat":"\u9ad8\u697c\u5c42","totalFloor":"8","signTime":"2023-09-10","isSold":1,"orientation":"\u5357 \u5317","isDisplay":1,"signSource":"","buildYear":"\u6682\u65e0\u4fe1\u606f","title":"\u559c\u5cf0\u5609\u56ed","price":191,"unitPrice":21068,"imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_3b053778-d5ca-4113-ab68-b9f956fa3025.png.280x210.jpg?from=ke.com"},{"houseId":"101119061245","viewUrl":"https:\/\/tj.ke.com\/chengjiao\/101119061245.html","source":"","jushi":"1\u5ba41\u5385","area":59,"resblockName":"\u559c\u5cf0\u5609\u56ed","floorStat":"\u9ad8\u697c\u5c42","totalFloor":"18","signTime":"2023-06-21","isSold":1,"orientation":"\u5357 \u5317","isDisplay":1,"signSource":"","buildYear":"\u6682\u65e0\u4fe1\u606f","title":"\u559c\u5cf0\u5609\u56ed","price":82.3,"unitPrice":13950,"imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-frame\/standard_8c390f67-8818-4244-a5fa-3a067f199adf.png.280x210.jpg?from=ke.com"}],"soldUrl":"https:\/\/tj.ke.com\/chengjiao\/c12000000001175\/","rent":[{"viewUrl":"http:\/\/tj.zu.ke.com\/zufang\/TJ1859454272282820608.html","price":"3200","source":"zufang","square":"91.00","imgSrc":"https:\/\/ke-image.ljcdn.com\/110000-inspection\/10675c39-7665-44b5-8361-41a5fcd19c7b.jpg.280x210.jpg","roomNum":"3\u5ba41\u53851\u536b","title":"\u6574\u79df\u00b7\u559c\u5cf0\u5609\u56ed 3\u5ba41\u5385 \u5357\/\u5317"},{"viewUrl":"http:\/\/tj.zu.ke.com\/zufang\/TJ1858043945368420352.html","price":"3000","source":"zufang","square":"89.00","imgSrc":"https:\/\/ke-image.ljcdn.com\/110000-inspection\/pc1_df6C1dybE.jpg.280x210.jpg","roomNum":"2\u5ba41\u53851\u536b","title":"\u6574\u79df\u00b7\u559c\u5cf0\u5609\u56ed 2\u5ba41\u5385 \u5357\/\u5317"},{"viewUrl":"http:\/\/tj.zu.ke.com\/zufang\/TJ1831990925245546496.html","price":"1900","source":"zufang","square":"79.00","imgSrc":"https:\/\/ke-image.ljcdn.com\/110000-inspection\/pc1_9mIwpEEmE.jpg.280x210.jpg","roomNum":"2\u5ba41\u53851\u536b","title":"\u6574\u79df\u00b7\u559c\u5cf0\u5609\u56ed 2\u5ba41\u5385 \u5357\/\u5317"}],"rentUrl":"http:\/\/tj.zu.ke.com\/zufang\/c12000000001175\/","ershoufang":[{"id":"101118208351","title":"\u559c\u5cf0\u5609\u56ed 2\u5ba41\u5385 \u5357","price":"152","unitPrice":"19450","area":78.15,"viewUrl":"https:\/\/tj.ke.com\/ershoufang\/101118208351.html","onListDate":"2023-03-02","resblockName":"\u559c\u5cf0\u5609\u56ed","resblockUrl":"","picture":"https:\/\/ke-image.ljcdn.com\/110000-inspection\/pc1_PShgMkWyn_1.jpg!m_fill,w_280,h_210,f_jpg?from=ke.com","jushi":"2\u5ba41\u5385","buildSize":78.15,"hallNum":"2\u5ba41\u5385","houseCode":"101118208351"},{"id":"101121263661","title":"\u559c\u5cf0\u5609\u56ed\u4e24\u5ba4\u901a\u900f\u6237\u578b\uff0c\u4e1a\u4e3b\u5bb6\u95f2\u7f6e\u623f\u6e90\uff0c\u8bda\u610f\u51fa\u552e","price":"149","unitPrice":"19069","area":78.14,"viewUrl":"https:\/\/tj.ke.com\/ershoufang\/101121263661.html","onListDate":"2023-09-27","resblockName":"\u559c\u5cf0\u5609\u56ed","resblockUrl":"","picture":"https:\/\/ke-image.ljcdn.com\/110000-inspection\/pc1_u4U0GrMmn_1.jpg!m_fill,w_280,h_210,f_jpg?from=ke.com","jushi":"2\u5ba41\u5385","buildSize":78.14,"hallNum":"2\u5ba41\u5385","houseCode":"101121263661"},{"id":"101120836570","title":"\u559c\u5cf0\u5609\u56ed  \u7cbe\u88c5\u4fee  H\u6237\u578b \u6ee1\u4e24\u5e74\u7a0e\u8d39\u4f4e \u91c7\u5149\u597d","price":"204","unitPrice":"22672","area":89.98,"viewUrl":"https:\/\/tj.ke.com\/ershoufang\/101120836570.html","onListDate":"2023-08-31","resblockName":"\u559c\u5cf0\u5609\u56ed","resblockUrl":"","picture":"https:\/\/ke-image.ljcdn.com\/110000-inspection\/pc1_R1OpZ5Oym_1.jpg!m_fill,w_280,h_210,f_jpg?from=ke.com","jushi":"2\u5ba41\u5385","buildSize":89.98,"hallNum":"2\u5ba41\u5385","houseCode":"101120836570"}],"ershoufangUrl":"https:\/\/tj.ke.com\/ershoufang\/c12000000001175\/","nearby":[{"url":"https:\/\/tj.ke.com\/xiaoqu\/2811052354990\/","imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-resblock\/2faa74d7-494c-43f4-8e4b-f9cc4af0c738.JPG","name":"\u4e07\u9686\u6843\u9999\u56ed","houseType":"\u666e\u901a\u4f4f\u5b85\/\u5546\u4e1a\/\u5e95\u5546","sellNum":145,"unitPrice":"11830\u5143\/\u33a1"},{"url":"https:\/\/tj.ke.com\/xiaoqu\/1211046633997\/","imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-resblock\/34adaa95-e1e9-474a-80a5-286730fdd7bb.jpg","name":"\u98ce\u91c7\u91cc","houseType":"\u666e\u901a\u4f4f\u5b85\/\u5546\u4e1a\/\u5e95\u5546","sellNum":182,"unitPrice":"15360\u5143\/\u33a1"},{"url":"https:\/\/tj.ke.com\/xiaoqu\/1220075280507675\/","imgSrc":null,"name":"\u5929\u548c\u4e3d\u56ed","houseType":"\u666e\u901a\u4f4f\u5b85\/\u5546\u4e1a\/\u5e95\u5546","sellNum":140,"unitPrice":"11816\u5143\/\u33a1"},{"url":"https:\/\/tj.ke.com\/xiaoqu\/1211047089204\/","imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-resblock\/c3b8a3ee-7a00-4bcc-a33e-6bcf177b32f8.jpg","name":"\u6843\u82b1\u56ed\u5357\u91cc","houseType":"\u666e\u901a\u4f4f\u5b85","sellNum":127,"unitPrice":"16490\u5143\/\u33a1"},{"url":"https:\/\/tj.ke.com\/xiaoqu\/1211046135166\/","imgSrc":"https:\/\/ke-image.ljcdn.com\/hdic-resblock\/ea174489-6a68-486c-b5cf-3205acfb0f16.JPG","name":"\u4ec1\u6052\u6cb3\u6ee8\u82b1\u56ed","houseType":"\u666e\u901a\u4f4f\u5b85","sellNum":126,"unitPrice":"40599\u5143\/\u33a1"}],"tdkData":{"title":"\u559c\u5cf0\u5609\u56ed_\u5929\u6d25\u559c\u5cf0\u5609\u56ed\u4e8c\u624b\u623f|\u623f\u4ef7|\u79df\u623f\u3010\u5929\u6d25\u8d1d\u58f3\u627e\u623f\u3011","keywords":"\u559c\u5cf0\u5609\u56ed,\u5929\u6d25\u559c\u5cf0\u5609\u56ed,\u559c\u5cf0\u5609\u56ed\u4e8c\u624b\u623f,\u559c\u5cf0\u5609\u56ed\u623f\u4ef7,\u559c\u5cf0\u5609\u56ed\u79df\u623f ","description":"\u8d1d\u58f3\u5929\u6d25\u5c0f\u533a\u5927\u5168,\u559c\u5cf0\u5609\u56ed\u53c2\u8003\u5747\u4ef7:20700\u5143\/\u33a1,\u4f4d\u4e8e\u6cb3\u5317\u65b0\u5f00\u6cb3,\u559c\u5cf0\u5609\u56ed\u5728\u552e\u4e8c\u624b\u623f\u6e9021\u5957,\u5df2\u670920\u4eba\u5173\u6ce8.\u67e5\u8be2\u559c\u5cf0\u5609\u56ed\u4f18\u8d28\u4e8c\u624b\u623f\u623f\u6e90\u3001\u79df\u623f\u623f\u6e90\u3001\u7ecf\u7eaa\u4eba\u3001\u8fd1\u671f\u6210\u4ea4\u8bb0\u5f55\u7b49\u4fe1\u606f,\u5c31\u5230\u5929\u6d25\u8d1d\u58f3\u627e\u623f."},"canonical":"https:\/\/tj.ke.com\/xiaoqu\/12000000001175\/","breadcrumbs":{"0":{"title":"\u5929\u6d25\u623f\u4ea7","url":"\/"},"1":{"title":"\u5929\u6d25\u5c0f\u533a","url":"\/xiaoqu\/"},"3":{"title":"\u65b0\u5f00\u6cb3\u5c0f\u533a","url":"https:\/\/tj.ke.com\/xiaoqu\/xinkaihe\/"},"4":{"title":"\u559c\u5cf0\u5609\u56ed","url":"\/xiaoqu\/12000000001175\/"}},"meta":{"curCityId":120000,"curCityName":"\u5929\u6d25"},"fbExpoId":"","fbQueryId":""},
    // sidebar:null
  }
</script>
<!-- LianjiaIM   --><script>window.LIANJIANIM_INFOS = {ucid: '',staticRoot: 'https://s1.ljcdn.com/pegasus/?_v=202401081627157'}</script><!--cookie mapping--><img src='' alt="cookie_mapping_url" style="display: none;"><!--反爬虫--><script>window['__abbaidu_2011_subidgetf'] = function () {return 110000;};window['__abbaidu_2011_cb'] = function (responseData) {var res = JSON.stringify({ t: responseData, r: location.href, os: 'web', v: '0.1' });res = btoa ? btoa(res) : res;document.cookie = 'srcid=' + res + ';path=/;';};</script><!--数据上报--><script>(function(){var bp = document.createElement('script');var curProtocol = window.location.protocol.split(':')[0];if (curProtocol === 'https'){bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';}else{bp.src = 'http://push.zhanzhang.baidu.com/push.js';}var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(bp, s);})();</script><script>$(function(){$('.lj-lazy').lazyload();$('.lazyload').scrollLoading();})</script><script type="application/javascript" src="https://dlswbr.baidu.com/heicha/mw/abclite-2011-s2.js"></script></body></html>

    '''

    str2 = '''
            <div class="xiaoquInfo">
                <div class="xiaoquInfoItemMulty">
                    <div class="xiaoquInfoItemCol">
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">建筑类型</span>
                            <span class="xiaoquInfoContent">板楼</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">房屋总数</span>
                                                        <span class="xiaoquInfoContent">909户</span>
                                                    </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">楼栋总数</span>
                                                        <span class="xiaoquInfoContent">11栋</span>
                                                    </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">绿化率</span>
                            <span class="xiaoquInfoContent">
                                                                40%
                                                            </span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">容积率</span>
                            <span class="xiaoquInfoContent">
                                                                2
                                                            </span>
                        </div>
                                            </div>
                    <div class="xiaoquInfoItemCol">
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">交易权属</span>
                            <span class="xiaoquInfoContent">商品房/经济适用房/动迁安置房/限价商品房/乡产/私产/校产</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">建成年代</span>
                                                        <span class="xiaoquInfoContent">暂无信息 </span>
                                                    </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">供暖类型</span>
                            <span class="xiaoquInfoContent">集中供暖</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">用水类型</span>
                            <span class="xiaoquInfoContent">民水</span>
                        </div>
                        <div class="xiaoquInfoItem">
                            <span class="xiaoquInfoLabel">用电类型</span>
                            <span class="xiaoquInfoContent">民电</span>
                        </div>
                                            </div>
                </div>
                <div class="xiaoquInfoItemOneLine">
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">物业费</span>
                        <span class="xiaoquInfoContent outer">
                                                2.2元/平米/月
                                                </span>
                    </div>
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">附近门店</span>
                        <span class="xiaoquInfoContent outer">
                              <span mendian="117.190015,39.189294" xiaoqu="[117.19078502924,39.18840789505]" class="actshowMap">鼎山聚云峰喜峰嘉园店</span>/新开河街道古北道与南口路交口喜峰嘉园配建1-8 9 10 11-101
                                                                            </span>
                    </div>
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">物业公司</span>
                        <span class="xiaoquInfoContent outer">天津远洋物业管理有限公司</span>
                    </div>
                    <div class="xiaoquInfoItem outerItem">
                        <span class="xiaoquInfoLabel">开发商</span>
                        <span class="xiaoquInfoContent outer">远洋集团</span>
                    </div>
                </div>
            </div>
    '''

    zone_info = {
        '建筑类型': '',
        '房屋总数': '',
        '楼栋总数': '',
        '区绿化率': '',
        '区容积率': '',
        '交易权属': '',
        '建成年代': '',
        '供暖类型': '',
        '用水类型': '',
        '用电类型': '',
        '房物业费': '',
        '附近门店': '',
        '物业公司': '',
        '其开发商': ''
    }

    soup = BeautifulSoup(str2, 'html.parser')
    xiaoqu_info_items = soup.find_all('div', class_='xiaoquInfoItem')

    spans_label = []
    spans_value = []
    for item in xiaoqu_info_items:
        spans = item.find_all('span', class_='xiaoquInfoLabel')
        spans_label.extend(spans)

        spans = item.find_all('span', class_='xiaoquInfoContent')
        spans_value.extend(spans)

    print(f'spans_label {len(spans_label)}')
    print(f'spans_value {len(spans_value)}')

    for id, span in enumerate(spans_label):
        label = span.text.strip().replace("\n", '')
        value = spans_value[id].get_text(strip=True).replace("\n", '')

        if spans_value[id]:
            for child in spans_value[id].contents:
                if child.name == 'span' and child.get("mendian"):
                    value1 = {
                        'name': child.get_text(strip=True),
                        'mapInfo': child.get("mendian").strip(),
                        'location': value
                    }
                    value = value1
                    break

        print(f'{label} : {value}')

        if label in zone_info:
            zone_info[label] = value
    # 提取结果
    return {k: v for k, v in zone_info.items() if v}


build_zone_info()
