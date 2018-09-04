#coding=utf-8
'''
Created on 2018-9-3

@author: Administrator
'''


import requests
import urllib2
import re
import json
import time,datetime
import random
import os
import csv
import pandas as pd
import openpyxl
import ssl
import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import sys
reload(sys)
sys.setdefaultencoding('utf8')

html = '''

<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script src="/Scripts/utf-8.js" type="text/javascript"></script>
    <title>渝B60Q65奥迪牌A4L小型轿车一辆_重庆市涪陵区人民法院</title>
    <meta name="Keywords" content="诉讼,诉讼资产,房产,土地,资产,林权,矿权,工程,竞价,法院,拍卖" />
    <meta name="Description" content="人民法院诉讼资产网" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <link rel="Stylesheet" type="text/css" href="/Styles/commonStyle.css" />
    <link rel="Stylesheet" type="text/css" href="/Styles/index.css" />
    <link href="/Styles/xmxx.css" rel="stylesheet" type="text/css" />
    <script type="text/javascript" src="/Scripts/jquery-1.4.4.min.js"></script>
    <script src="/Scripts/zzsc.js"></script>
    <script src="/Scripts/jquery.sticky.js"></script>
    <script type="text/javascript" src="/ckplayer/ckplayer.js" charset="utf-8"></script>
    <link href="/Styles/zzsc.css" rel="stylesheet" type="text/css" />
    <script src="/Scripts/JavaScript.js"></script>
    <style type="text/css">
        .cur {
            background-image: url(/Images/选中.png);
            color: white !important;
            font-weight: bold;
            text-decoration: none !important;
        }

        .cur2 {
            color: #3e3d3d !important;
            text-decoration: none !important;
        }

        .ti {
            font-size: 24px;
            color: #d91615;
            font-weight: bold;
            font-family: 'Microsoft YaHei';
            padding: 3px;
        }

        .ti1 {
            color: #2f2f2f;
            font-family: 'SimSun';
            font-size: 14px;
        }

        .pic1 {
            width: 480px;
            height: 320px;
        }

        .div1 {
            margin-left: 65px;
            padding: 15px;
        }

        .div2 p {
            text-align: right;
        }

        .div2 {
            padding-top: 40px;
        }

        #wind {
            font-size: 16px;
            font-family: '微软雅黑';
        }

            #wind table {
                border: 0;
                margin: 0;
                border-collapse: collapse;
            }

                #wind table td {
                    padding: 10px;
                }

        .Record div {
            width: 200px;
            text-align: center;
            height: 25px;
            line-height: 25px;
            float: left;
        }

        .Record {
            width: 800px;
            margin: 0px auto;
            padding: 25px 0;
            border-bottom: 1px dashed #ccc;
            text-align: center;
        }

        .Record1 {
            background: #a2000d;
            color: white;
            padding: 2px;
            font-size: 12px;
            font-family: 'Microsoft YaHei';
        }

        .Record2 {
            background: white;
            padding: 2px;
            font-size: 12px;
            font-family: 'Microsoft YaHei';
            border: 1px solid #ccc;
        }

        #bdjs11 div table {
            display: inline-block;
        }

        a:hover {
            text-decoration: none;
        }

        .s1 {
            background: #a2000d;
            width: 5px;
            height: 18px;
            display: inline-block;
            margin-right: 10px;
        }

        .search1 {
            margin-top: 18px;
            height: 30px;
            font-family: 'Microsoft YaHei';
            color: #313131;
            font-size: 14px;
            line-height: 18px;
            font-weight: bold;
            list-style: none;
        }

        .yxq {
            display: block;
            line-height: 25px;
            background: #ccc;
        }

        .tcl {
            font-family: 'Microsoft YaHei';
            color: #313131;
            font-size: 14px;
            font-weight: bold;
        }

        #history1 {
            padding-left: 25px;
        }

        .topbox {
            height: 500px;
            background-color: #313131;
        }

        .section-content {
            border-bottom: 5px solid #0000FF;
            min-height: 500px;
            background: #eee;
            width: 1200px;
            margin: auto;
            line-height: 500px;
            text-align: center;
        }

        .nav-height {
            position: relative;
            height: 50px;
        }

        .nav-wrap {
            width: 960px;
            height: 50px;
            background: #fff;
        }

            .nav-wrap.navFix {
                position: fixed;
                top: 0;
                left: 100;
                border-bottom: 1px solid #e3e3e3\9;
                z-index: 99999;
            }

            .nav-wrap ul {
                padding: 0;
                margin: 0 auto;
                width: 960px;
                display: block;
            }

            .nav-wrap.navFix ul {
                border-bottom: 0;
            }

            .nav-wrap li {
                display: inline-block;
                text-align: left;
                height: 50px;
                line-height: 50px;
                float: left;
            }

                .nav-wrap li a {
                    display: block;
                    padding: 0 20px;
                    font-size: 20px;
                    color: #333;
                    text-decoration: none;
                    font-family: 'Microsoft YaHei';
                    background-color: rgb(238, 238, 238);
                }

                    .nav-wrap li a:hover {
                        color: #a2000d;
                    }

                    .nav-wrap li a.active {
                        border-bottom: 2px solid #a2000d;
                        color: #a2000d;
                        background: white;
                    }

        .nav-mobile {
            display: none;
            font-weight: bold;
            width: 100%;
        }

        .click-me {
            width: 150px;
            height: 30px;
            background: #4680d1;
            color: white;
            text-align: center;
            line-height: 30px;
        }

            .click-me a {
                display: block;
                color: white;
            }

        .helper-tag {
            background: #fafafa;
            color: #cd0000;
            font-weight: 700;
            border: 1px solid #dfdfdf;
            border-radius: 2px;
            margin-right: 10px;
            padding: 2px 9px;
        }

        .help1 {
            font-weight: bold;
        }

        .help2 ul li {
            padding: 0;
            margin: 0;
        }

            .help2 ul li a {
                font-size: 12px;
            }
        .fz {
            width: 100%;
            height: 30px;
            border-bottom: 1px solid #e8e8e8;
            border-top: 1px solid #e8e8e8;
            line-height: 30px;
            text-indent: 10px;
            height: 30px;
            font-size: 14px;
            font-family: 'Microsoft YaHei';
            font-weight: bold;
            background: #f1f1f1;
        }
        .fz1 {
            text-align: center;
            display: block;
            margin-top: 5px;
            font-weight: bold;
        }
        .fz2 {
            width: 120px;
            margin-left:40px;
            margin-top: 5px;
        }
    </style>
</head>
<body style="background:#eeeeee;">
    <div id="head">
    <div style="width:100%; height:35px;background:#eeeeee;">
        <div style="width:1200px; margin:0px auto; height:35px;">
            <iframe src="http://www1.rmfysszc.gov.cn/Login1/" frameborder="0" scrolling="no" hspace="0" vspace="0" width="1200" height="35" align="middle" allowtransparency="true"> </iframe>
        </div>
    </div>
    <div style="width:100%; height: 100px; background-image: url(http://www.rmfysszc.gov.cn/images/bannersf.png); background-position: center center"></div>
    <div style="width:100%; height:50px; border-bottom:2px solid #a2000d; background:white;">
        <div style="width:1200px; margin:0px auto; height:100%;">
            <a href="http://www.rmfysszc.gov.cn" target="_blank"><img class="nav" style=" margin-top:14px; margin-right:170px;" src="http://www.rmfysszc.gov.cn/2017version/images/导航栏/导航栏-首页图标.png" /></a>
            <a href="http://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1" target="_blank"><img class="nav" style=" margin-top: 14px; margin-right: 170px;" src="http://www.rmfysszc.gov.cn/2017version/images/导航栏/导航栏-拍卖项目图标点击.png" /></a>
            <a href="https://auction.rmfysszc.gov.cn/" target="_blank"><img class="nav" style=" margin-top: 14px; margin-right: 170px;" src="http://www.rmfysszc.gov.cn/2017version/images/导航栏/导航栏-竞价大厅图标.png" /></a>
            <a href="http://www1.rmfysszc.gov.cn/agency/?fid=&dh=8" target="_blank"><img class="nav" style=" margin-top: 14px; margin-right: 170px;" src="http://www.rmfysszc.gov.cn/2017version/images/导航栏/导航栏-司辅工作图标.png" /></a>
            <a href="http://www.rmfysszc.gov.cn/helpcenter.html" target="_blank"><img class="nav" style=" margin-top:14px;" src="http://www.rmfysszc.gov.cn/2017version/images/导航栏/导航栏-帮助中心图标.png" /></a>
        </div>
    </div>
</div>

        <div style="width:1200px; margin:0px auto;background:white;">

            <div style="width:1180px; margin:0px auto;">
                <div style=" width:1180px; height:30px; line-height:30px; font-size:12px; font-family:'Microsoft YaHei'; color:#535353; font-weight:bold; margin:0px auto;">
                    <img style="margin-top:8px;" src="http://www.rmfysszc.gov.cn/2017version/images/map.png" />&nbsp;您当前所在位置:&nbsp;&nbsp;<a target="_blank" style="color: #535353; " href="http://www.rmfysszc.gov.cn">首页</a>&nbsp;&nbsp;&gt;&nbsp;&nbsp;<a href="http://www1.rmfysszc.gov.cn/projects.shtml">拍卖项目</a>&nbsp;&nbsp;&gt;&nbsp;&nbsp;<a href="javascript:void(0)" style="color: #a2000d">标的详情</a>
                </div>
                <div id="Title"><h1 style="font-family:'宋体'; color:#292c2e">渝B60Q65奥迪牌A4L小型轿车一辆</h1></div>
                <div id="Main1" style="height:320px;">
                    <div id="MainLeft" style="float:left; width:480px; height:100%;">
                        <div id="zzsc">
                            <a href="javascript:void(0)"><img class="pic1" src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115309._sm_.jpg" /></a><a href="javascript:void(0)"><img class="pic1" src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115412._sm_.jpg" /></a><a href="javascript:void(0)"><img class="pic1" src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115403._sm_.jpg" /></a><a href="javascript:void(0)"><img class="pic1" src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115356._sm_.jpg" /></a>
                        </div>
                    </div>
                    <div id="MainRight" style="width:480px;float:left; height:100%;margin-left:10px;">
                        <div id="price" style=" width:100%; height:80px; background:#f1f1f1;">
                            <div style="text-indent:30px; margin-top:10px; color:#2f2f2f; width:100%; float:left; font-size:14px; font-family:'SimSun'">
                                起拍价<span style="font-size:22px;color:#d91615; padding:10px; font-family:SimHei">￥13.5万元</span>
                            </div>
                            <div style="text-indent:30px; margin-top:10px;color:#2f2f2f; width:100%; float:left;font-size:14px; font-family:'SimSun'">
                                <span>大&nbsp;&nbsp;写</span><span style="color:#d91615; padding:10px; font-family:SimHei; text-indent:10px;font-size:20px;">壹拾叁万伍仟元</span>
                            </div>

                        </div>
                        <div id="time1" style="width:100%; height:60px; text-indent:30px; font-size:14px; line-height:60px;color:#2f2f2f;font-family:'SimSun'">
                            <span id="wen" style="">距开始</span><span id="time" style="margin-left:10px; "></span>&nbsp;<img style="" src="/Images/时钟.png" />
                        </div>
                        <div id="bm1" style="width:100%; height:40px; text-indent:30px;">
                            <a href="javascript:void(0)" onclick="collection(1147887,93675)" style="font-size:24px;color:red;line-height:41px;"><img src="/Images/收藏.png" style=" cursor:pointer;" /></a>
                            &nbsp;&nbsp;

                            <span class="bm"><img src="/Images/报名2.png" /></span>
                        </div>
                        <div id="bg1" style="width:100%; height:110px; margin-top:30px; text-indent:30px;">
                            <div style="width:210px; height:100%; float:left;">
                                <table>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">评估值: </span><span style="color:#d91615;font-size:16px;">13.5万元</span><span style="color:#515050;"></span></td>
                                    </tr>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">保证金: </span><span style="color:#d91615;font-size:16px;">2.7万元</span><span style="color:#515050;"></span></td>
                                    </tr>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">公告日期: 2018.09.03</span></td>
                                    </tr>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">拍卖阶段: 第1次拍卖</span></td>
                                    </tr>
                                </table>
                            </div>
                            <div style="width:250px; height:100%; float:right;">
                                <table>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">处置法院: 重庆市涪陵区人民法院</span></td>
                                    </tr>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">联系人: 崔传宜</span></td>
                                    </tr>
                                    <tr style=" height:25px;">
                                        <td><span style="color:#515050;">咨询电话: 023-72385902</span></td>
                                    </tr>
                                    <tr style=" height:25px;">
                                        <td></td>
                                    </tr>

                                </table>
                            </div>
                        </div>
                    </div>
                    <div id="MainRight1" style="width:198px;float:left;margin-left:10px;border:1px solid #e8e8e8;max-height:318px;">
                        <div style="width:100%;height:30px;border-bottom:1px solid #e8e8e8;line-height:30px;text-indent:10px; height:30px;font-size:14px;font-family:'Microsoft YaHei'; font-weight:bold;background:#f1f1f1">
                            竞买帮助
                        </div>
                        <div style="width:100%;font-size:12px;font-family:'Microsoft YaHei';border-top:none; line-height:20px;">
                            <div class="help2" style="width:100%;">
                                <ul>
                                    <li class="help1"><a href="/helpcenter.html#entered_4" target="_blank">如何参与报名</a></li>
                                    <li class="help1"><a href="/helpcenter.html#entered_9" target="_blank">有哪些支付方式</a></li>
                                    <li class="help1"><a href="/helpcenter.html#handle_1" target="_blank">如何开始竞价</a></li>
                                    <li class="help1"><a href="http://test.rmfysszc.gov.cn/" target="_blank">体验模拟竞价</a></li>
                                </ul>
                            </div>
                              
                                </div>
                        <div>
                        </div>
                    </div>
                </div>
                <div id="sc" style="width:960px; height:40px;">
                    <div id="Div2" style="float:left; width:480px; height:100%; text-align:right;line-height:40px; font-size:12px; color:#747474; font-family:'Microsoft YaHei';">
                        <span style="font-weight:bold; color:#504f4f;" class="bmnumber"></span>人报名&nbsp;&nbsp;&nbsp;<span style="font-weight:bold;color:#504f4f;" class="sc"></span>人收藏
                        &nbsp;&nbsp;<span style="font-weight:bold;color:#504f4f;" class="hits"></span>次围观
                    </div>
                </div>
            </div>
                



            <div class="xmxx_main">
                <div id="Main" style="width:960px; margin:0px auto">
                    <div class="nav-height" id="navHeight">
                        <nav class="nav-wrap" id="nav-wrap">
                            <div class="nav-mobile">Click</div>
                            <ul class="clearfix">
                                <li><a class="active" href="#tbts">特别提示</a></li>
                                <li><a class="" href="#pmgg">拍卖公告</a></li>
                                <li><a class="" href="#jmxz">竞买须知</a></li>
                                <li><a class="" href="#bdjs">标的介绍</a></li>
                                <li><a class="" href="#yxgmq">优先购买权</a></li>
                                <li><a class="" href="#jjjl">竞价记录</a></li>
                            </ul>
                        </nav>
                    </div>
                    <div id="Content" style="margin-top:20px;">
                        <div id="tbts" style="width:100%;  margin-bottom:20px;">
                            <img src="/Images/特别提示.png" style="margin-bottom:10px;" />
                            <div style="text-indent:20px;">
                                <p>1、竞买人应当具备完全民事行为能力，法律、行政法规、司法解释对买受人资格或者条件有特殊规定的（比如商品房限购等），竞买人应当具备规定的资格或者条件。</p>
                                <p>2、委托他人代为竞买的，竞买人应当理解委托的法律含义，办妥委托手续，并在竞价程序开始前经人民法院确认。</p>
                                <p>3、竞买人应当仔细阅读拍卖公告、竞买须知及相关附件资料，了解标的情况、竞价规则、交款方式、法律责任。</p>
                                <p>4、拍卖标的以现状为准，对于实物标的，竞买人可以申请看样。</p>
                                <p>5、竞买人决定参与竞价的，视为对拍卖标的完全了解，并接受拍卖标的一切已知和未知瑕疵。</p>
                                <p>6、竞买人取得竞价资格后，出价不得低于起拍价；拍卖以最高出价成交，优先购买权人可以在不加价的情况下行使优先权；无人报名或出价的，竞价会流标。</p>
                                <p>7、买受人悔拍后保证金不予退还；悔拍后重新拍卖的，原买受人不得参加竞买。</p>
                                <p>8、拍卖保证金或变卖价款缴纳期间不计利息。</p>
                                <p>9、拍卖成交的，将以买受人的真实身份自动生成确认书并公示。</p>
                            </div>
                            <div id="history1"
                                style="display:none"
                                    >
                                    <div style="width:100%; height:18px;">
                                        <div class="s1" style="float:left;"></div>
                                        <div class="tcl" style="float:left; line-height:18px;">历史版本</div>
                                    </div>
                                    <div class="tcl" style="margin-top:10px;">
                                        <center style="line-height:25px;">暂无修改记录</center>
                                    </div>
                            </div>
                        </div>
                        <div id="pmgg" style="width:100%; margin-bottom:20px;">
                            <img src="/Images/拍卖公告.png" style="margin-bottom:10px;" />
                            <div style="text-indent:20px;">
                                <p style="text-align:center;font-size: 14px;font-family: microsoft yahei;font-weight: bolder;"><a href="/statichtml/rm_xmdetail/1147887.shtml" target="_blank" title="渝B60Q65奥迪牌A4L小型轿车一辆">渝B60Q65奥迪牌A4L小型轿车一辆</a></p>
                                    <P style="TEXT-ALIGN: center; LINE-HEIGHT: 13pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly" class=MsoNormal align=center><B style="mso-bidi-font-weight: normal"><SPAN style="COLOR: black; FONT-SIZE: 16pt; mso-hansi-font-family: 宋体" lang=EN-US><?xml:namespace prefix = o ns = "urn:schemas-microsoft-com:office:office" /><o:p><FONT face=宋体>&nbsp;</FONT></o:p></SPAN></B></P>
<P style="TEXT-ALIGN: center; LINE-HEIGHT: 20pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly" class=MsoNormal align=center><B style="mso-bidi-font-weight: normal"><SPAN style="COLOR: black; FONT-SIZE: 16pt; mso-hansi-font-family: 宋体"><FONT face=宋体>渝<SPAN lang=EN-US>B60Q65</SPAN>奥迪牌<SPAN lang=EN-US>A4L</SPAN>小型轿车一辆司法变卖公告<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></B></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>受重庆市涪陵区人民法院委托，定于<U style="text-underline: thick"><SPAN lang=EN-US>9</SPAN>月<SPAN lang=EN-US>7</SPAN>日<SPAN lang=EN-US>10</SPAN>：<SPAN lang=EN-US>00</SPAN>起至<SPAN lang=EN-US>9</SPAN>月<SPAN lang=EN-US>12</SPAN>日<SPAN lang=EN-US>10</SPAN>：<SPAN lang=EN-US>00</SPAN>止<B style="mso-bidi-font-weight: normal">（延时除外）</B></U>对以下标的物按现<SPAN style="LETTER-SPACING: 0.2pt">状依法在重庆联交所涪陵分所以<U style="text-underline: thick">互联网竞价方式</U>进行公开整体变卖，公告如下：<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22.8pt; MARGIN: 0cm 0cm 0pt; LAYOUT-GRID-MODE: char; mso-line-height-rule: exactly; mso-pagination: none; mso-char-indent-count: 2.0; mso-layout-grid-align: none" class=MsoNormal><SPAN style="LETTER-SPACING: 0.2pt; COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>一、本次变卖标的物（以下简称标的物）：<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22.8pt; MARGIN: 0cm 0cm 0pt; LAYOUT-GRID-MODE: char; mso-line-height-rule: exactly; mso-pagination: none; mso-char-indent-count: 2.0; mso-layout-grid-align: none" class=MsoNormal><SPAN style="LETTER-SPACING: 0.2pt; COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>渝<SPAN lang=EN-US>B60Q65</SPAN>奥迪牌<SPAN lang=EN-US>A4L</SPAN>小型轿车一辆，据机动车询价报告显示：标的物品牌型号为奥迪牌<SPAN lang=EN-US>FV7203BECBG,</SPAN>车辆识别代号为<SPAN lang=EN-US>LFV3A28KXE3063746</SPAN>，发动机号为<SPAN lang=EN-US>018170</SPAN>，初次登记日期为<SPAN lang=EN-US>2014</SPAN>年<SPAN lang=EN-US>12</SPAN>月<SPAN lang=EN-US>5</SPAN>日，行驶里程不详，棕色。变卖保留价<SPAN lang=EN-US>13.5</SPAN>万元，竞买保证金：<SPAN lang=EN-US>2.7</SPAN>万元，竞价阶梯为仟。<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">二、标的物展示时间、地点：自公告之日起，在标的物停放地（</SPAN><SPAN style="FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">涪陵区展宏二手车市场<SPAN style="COLOR: black">）现场展示。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>三、竞买登记手续办理：竞买人可通过线上（通过互联网方式）或线下（到重庆联交所现场）两种方式报名。竞买人通过线下报名的，竞买人应在<SPAN lang=EN-US>9</SPAN>月<SPAN lang=EN-US>11</SPAN>日（到账为准）前将保证金缴至重庆市高级人民法院指定联付通账户，并于<SPAN lang=EN-US>9</SPAN>月<SPAN lang=EN-US>11</SPAN>日（法定工作时间）前办理竞买登记手续（签订竞买协议等）方可取得竞买资格，逾期不予办理；竞买人通过线上报名的，竞价结束前<U style="text-underline: thick">（延时除外）</U>，竞买人均可报名参与竞买。<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>四、特别说明：<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 16.5pt; MARGIN: 0cm 0cm 0pt 6pt; mso-line-height-rule: exactly; mso-char-indent-count: 1.5; mso-para-margin-left: .5gd" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>1</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、</SPAN><SPAN style="FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">标的物有抵押。</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt">据评估报告显示：标的物共计<SPAN lang=EN-US>1</SPAN>次违法记录，累计罚款金额<SPAN lang=EN-US>100</SPAN>元，违法记分<SPAN lang=EN-US>0</SPAN>分，具体违章情况以交巡警部门查询为准。标的物违法行为未处理存在不能过户的风险。</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US><o:p></o:p></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>2</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、</SPAN><SPAN style="FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">变卖成交后，执行法院根据成交价款和变卖费用的到账记录出具法律文书，由买受人自行领取或者委托二手车市场代领，买受人接到二手车市场通知后应于<SPAN lang=EN-US>1</SPAN>日内凭有效身份证明前往二手车市场领取。二手车市场对法律文书和买受人有效身份证明核对无误后交付机动车，机动车应从变卖专用车位移走。若买受人经通知后怠于到二手车市场办理交付手续或者机动车交付后，买受人怠于将机动车移走，导致机动车仍然占用变卖专用车位，二手车市场将依据其合法收费标准向买受人收取停车费<SPAN style="COLOR: black">。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>3</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、标的物过户由执行法院协助办理，所涉及的税、费由买、卖双方按国家相关规定各自承担其应缴纳部分。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>4</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、标的物移交所涉及的欠费（包括但不限于路桥费、停车费、违章罚款及违章扣分、滞纳金）等费用均由买受人承担。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><U style="text-underline: thick"><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>5</SPAN></U><U style="text-underline: thick"><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、竞价程序结束前两分钟内无人出价的，最后出价即为成交价；有出价的，竞价时间自该出价时点顺延两分钟。竞买人的出价时间以进入我集团竞价系统的时间为准。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></U></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><U style="text-underline: thick"><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>竞价界面的显示提醒：公告上的结束时间即为竞价界面显示的自由竞价时间加两分钟延时时间，若在延时时间内无人出价，竞价会结束；若有人出价，竞价时间继续顺延两分钟。<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></U></P>
<P style="LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>6</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、请竞买人在报名前详细阅读询价报告、竞买协议等材料所披露的内容，认真查看标的物，充分了解标的物现状和瑕疵及相关法律法规、政策规定。竞买人完成报名手续，即视为已完全了解并认可标的物的现状和一切已知及未知的瑕疵，并以其独立判断决定自愿以现状竞买本项目。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>7</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、竞买人须以自己名义并以现金以外的转账方式缴入重庆市高级人民法院指定联付通账户，他人为竞买人代支付保证金的将视为无效，所缴款项退回原账户。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>8</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、竞买人通过互联网方式报名时，不得多人联合竞买，需办理多人联合竞买的竞买人请到重庆联交所现场办理竞买登记手续。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>9</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、变卖成交后，买受人应当在变卖成交后<SPAN lang=EN-US>5</SPAN>日内将价款全额划到法院指定联付通账户。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22.1pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><FONT face=宋体><B style="mso-bidi-font-weight: normal"><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US>10</SPAN></B><B style="mso-bidi-font-weight: normal"><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">、因报名、支付保证金、保证金到账、竞买登记手续（签订竞买协议等）等事项的办理需要一定时间，竞买人应尽量提前办理预留足够时间。如因办理过于接近竞价会截止时间而导致竞买人无法参加竞价会的，责任由竞买人自负。<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></B></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>联系电话及联系人：<SPAN lang=EN-US>023-72385902<SPAN style="mso-spacerun: yes">&nbsp;&nbsp;&nbsp; </SPAN></SPAN>崔老师<SPAN lang=EN-US><SPAN style="mso-spacerun: yes">&nbsp;&nbsp;&nbsp; </SPAN><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="LINE-HEIGHT: 20pt; TEXT-INDENT: 44.55pt; MARGIN: 0cm -27.6pt 0pt -24.25pt; BACKGROUND: white; mso-line-height-rule: exactly; mso-char-indent-count: 4.05; mso-para-margin-left: -2.02gd; mso-para-margin-top: 0cm; mso-para-margin-right: -2.3gd; mso-para-margin-bottom: .0001pt" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>联交所涪陵分所地址：<SPAN style="BACKGROUND: white; mso-bidi-font-weight: bold">重庆市涪陵区太极大道<SPAN lang=EN-US>44</SPAN>号</SPAN><SPAN style="mso-bidi-font-weight: bold" lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>委托法院监督电话：<SPAN style="mso-bidi-font-weight: bold" lang=EN-US>023-72812808</SPAN><SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>市高法院监督电话：<SPAN lang=EN-US>023-67673247<SPAN style="mso-spacerun: yes">&nbsp; </SPAN>67673497<o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-ALIGN: right; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal align=right><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体"><FONT face=宋体>重庆联合产权交易所集团涪陵分所<SPAN lang=EN-US><o:p></o:p></SPAN></FONT></SPAN></P>
<P style="TEXT-ALIGN: center; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 22pt 0pt 0cm; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal align=center><FONT face=宋体><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US><SPAN style="mso-spacerun: yes">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; </SPAN>2018</SPAN><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体">年<SPAN lang=EN-US>9</SPAN>月<SPAN lang=EN-US>3</SPAN>日<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></FONT></P>
<P style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 20pt; TEXT-INDENT: 22pt; MARGIN: 0cm 0cm 0pt; mso-line-height-rule: exactly; mso-char-indent-count: 2.0" class=MsoNormal><SPAN style="COLOR: black; FONT-SIZE: 11pt; mso-hansi-font-family: 宋体" lang=EN-US><o:p><FONT face=宋体>&nbsp;</FONT></o:p></SPAN></P>
                                        
                                            

                            </div>
                        </div>
                        <div id="jmxz" style="width:100%;margin-bottom:20px;">
                            <img src="/Images/竞买须知.png" style="margin-bottom:10px;" />
                            <div style="text-indent:20px;">
                                <center>暂无竞买须知</center>
                            </div>
                        </div>
                        <div id="bdjs" style="width:100%; margin-bottom:20px;">
                            <img src="/Images/标的介绍.png" style="margin-bottom:10px;" />
                            <div id="bdjs11" style="text-indent:20px;text-align:center;">
                                <div style="width:100%; margin-bottom:40px;display:none">
                                    <div style="text-align:left;text-indent:0px;">
                                        <div style="width:100%; height:18px; padding-left:25px; margin-bottom:10px;">
                                            <div class="s1" style="float:left;"></div>
                                            <div class="tcl" style="float:left; line-height:18px;">优先购买权</div>
                                        </div>
                                    </div>
                                    <div>
                                        <span class="yxq"></span>
                                    </div>
                                </div>
                                <table cellpadding="0" cellspacing="1" border="0" class="xmxx_objtab" >    <tr>        <th>名称</th>        <td colspan="7">渝B60Q65奥迪牌A4L小型轿车一辆</td>     </tr>    <tr>        <th>询价报告</th>        <td colspan="7"><span style="display:block;width:850px;white-space:pre-wrap;word-wrap:break-word;"><a href="http://files.cquae.com/Upload/201809/03/IMG_20180903_102726._sm_.jpg" target="_blank">IMG_20180903_102726._sm_.jpg</a>;<a href="http://files.cquae.com/Upload/201809/03/IMG_20180903_102909._sm_.jpg" target="_blank">IMG_20180903_102909._sm_.jpg</a>;<a href="http://files.cquae.com/Upload/201809/03/IMG_20180903_102926._sm_.jpg" target="_blank">IMG_20180903_102926._sm_.jpg</a>;<a href="http://files.cquae.com/Upload/201809/03/IMG_20180903_102937._sm_.jpg" target="_blank">IMG_20180903_102937._sm_.jpg</a>;<a href="http://files.cquae.com/Upload/201809/03/IMG_20180903_102945._sm_.jpg" target="_blank">IMG_20180903_102945._sm_.jpg</a>;<a href="http://files.cquae.com/Upload/201809/03/IMG_20180903_102953._sm_.jpg" target="_blank">IMG_20180903_102953._sm_.jpg</a>;</span></td>     </tr>    <tr>        <th>起拍价</th>        <td>13.5（万元）</td>        <th>评估值</th>        <td>13.5（万元）</td>        <th>保证金</th>        <td>2.7（万元）</td>        <th>类型</th>        <td>机动车</td>    </tr></table><img src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115309._sm_.jpg"  style="width:750px;padding:20px;"/><br/><img src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115412._sm_.jpg"  style="width:750px;padding:20px;"/><br/><img src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115403._sm_.jpg"  style="width:750px;padding:20px;"/><br/><img src="http://files.cquae.com/Upload/201809/03/QQ图片20180831115356._sm_.jpg"  style="width:750px;padding:20px;"/><br/><div style="margin-top:20px;"></div><div style="width:100%;height:40px;"></div>
                                    
                            </div>
                        </div>
                        <div id="yxgmq" style="width:100%; margin-bottom:20px;">
                            <img src="/Images/优先购买权.png" style="margin-bottom:10px;">
                            <div style="text-indent:20px;width:800px;margin:0px auto;">
                                <span class="yxq"></span>
                            </div>
                        </div>
                        <div id="jjjl" style="width:100%;margin-bottom:10px;margin-bottom:20px;">
                            <img src="/Images/jjjl.jpg" />
                            <div id="jjjl1">
                                <div class="Record">
                                    <div style="background: #ccc;">状态</div>
                                    <div style="background: #ccc;">竞价账号</div>
                                    <div style="background: #ccc;">出价</div>
                                    <div style="background: #ccc;">时间</div>
                                </div>
                                <div class="Record">
                                    没有更多出价记录...
                                </div>
                            </div>
                            <div id="result1" style="margin-top:20px;">
                                <div>
                                    <div style="width:100%; height:18px; padding-left:50px;">
                                        <div class="s1" style="float:left;"></div>
                                        <div class="tcl" style="float:left; line-height:18px;">竞价结果</div>
                                    </div>
                                </div>
                                <div id="cjs1"></div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div style="width:1200px; margin:0px auto; height:340px;background:white;margin-bottom:20px;margin-bottom:20px;">
            <iframe src="http://www1.rmfysszc.gov.cn/object/recommend/93675.shtml" frameborder="0" scrolling="no" hspace="0" vspace="0" width="1200" height="330" align="middle" allowtransparency="true"> </iframe>
        </div>
        <input type="hidden" id="time5" value="" />
        <input type="hidden" id="time6" value="" />
         <div style="width:100%; height:10px; background:#a2000d; float:left;"></div>
    <div style="width:100%; float:left; background:white; padding-bottom:30px;">
        <div style="width:1200px; margin:0px auto;  font-size:14px; color:#535353; line-height:25px;">
            <div style="width:1200px; height:240px; border-bottom:1px solid black; margin:0px auto;">
                <div style="width:900px; height:100%; float:left;">
                    <div style="width:100%; height: 170px; margin-top: 35px;">
                        <div style="width:110px; height:100%;float:left; margin-right:130px;">
                            <span style="font-size:16px; font-weight:bold; display:block;margin-bottom:20px; color:#313131">基础知识</span>
                            <a href="/helpcenter.html#index_1" class="help">什么是司法拍卖？</a>
                            <a href="/helpcenter.html#index_4" class="help">法院入驻</a>
                            <a href="/helpcenter.html#index_5" class="help">重要规定</a>
                            <a href="/helpcenter.html#index_6" class="help">文书模板</a>

                        </div>
                        <div style="width:110px; height:100%;float:left; margin-right:130px;">
                            <span style="font-size:16px; font-weight:bold; display:block;margin-bottom:20px; color:#313131">报名帮助</span>
                            <a href="/helpcenter.html#entered_4" class="help">普通竞买人报名</a>
                            <a href="/helpcenter.html#entered_5" class="help">申请执行人报名</a>
                            <a href="/helpcenter.html#entered_6" class="help">优先购买权人报名</a>
                            <a href="/helpcenter.html#entered_7" class="help">委托报名</a>
                            <a href="/helpcenter.html#work_3" class="help">机构摇号报名</a>
                        </div>
                        <div style="width:150px; height:100%;float:left; margin-right:50px;">
                            <span style="font-size:16px; font-weight:bold; display:block;margin-bottom:20px; color:#313131">支付帮助</span>
                            <a href="/helpcenter.html#entered_9" class="help">支付保证金</a>
                            <a href="/helpcenter.html#compete_1" class="help">支付余款</a>
                            <a href="/helpcenter.html#entered_10" class="help">支付额度要求</a>
                        </div>
                        <div style="width:110px; height:100%;float:left; margin-right:30px;">
                            <span style="font-size:16px; font-weight:bold; display:block;margin-bottom:20px; color:#313131">竞价帮助</span>
                            <a href="/helpcenter.html#handle_1" class="help">竞价规则</a>
                            <a href="/helpcenter.html#handle_2" class="help">竞价周期</a>
                            <a href="/helpcenter.html#entered_11" class="help">获取竞价账号</a>
                            <a href="/helpcenter.html#handle_9" class="help">进入竞价会</a>
                        </div>
                        <div style="width:1px; height:100%;float:right;">
                            <img src="http://www.rmfysszc.gov.cn/2017version/images/竖虚线.png">
                        </div>

                    </div>
                </div>
                <div style="width:300px; height:100%; float:left;">
                    <div style="width:240px; height: 170px; float: left; margin-top: 35px;  float:right;">
                        <div style="width:240px; height:100%;float:left;">
                            <span style="font-size:16px; font-weight:bold; display:block;margin-bottom:20px; color:#313131">关于我们</span>
                            <span class="help">客服专线：4009-010-838</span>
                            <span class="help">联系地址：北京市东城区东交民巷27号</span>
                            <span class="help">邮政编码：100745</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="divfoot_r2_c1" style="text-align:center;">
                <div style="font-family: 'Microsoft YaHei'; color: #535353; font-size:14px; margin-top:20px;">中华人民共和国最高人民法院司法行政装备管理局主管</div>
            </div>


        </div>
    </div>
<div style="display:none"><script src="http://s96.cnzz.com/stat.php?id=3765988&web_id=3765988" language="JavaScript"></script></div>
</body>
</html>
<script type="text/javascript">
    $(function () {
        $('.xmxx_top1 a div').bind('click', function () {
            $this = $(this);
            $this.removeClass().addClass('xmxx_top1li1');
            $('.xmxx_top1 a div').each(function () {
                $this1 = $(this);
                if ($this.get(0) != $this1.get(0)) {
                    $this1.removeClass().addClass('xmxx_top1li');
                }
            });
        });
    });
</script>
<script type="text/javascript" src="/Scripts/jquery.scrollLoading.js"></script>
<script type="text/javascript">
    function dtime1(type) {
        var urlOne = "http://www1.rmfysszc.gov.cn/Login1/GetTime.shtml";
        var pid = '1';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { id: pid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {
            },
            success: function (data) {
                $("#time6").val(data.Count);
                getMyTime1(type);
            }
        });
    }
    var startDate=null;
    function getMyTime1(type) {
        if(startDate==null){
            startDate = $("#time6").val();
        }
        startDate = new Date(startDate);
        startDate.setSeconds(startDate.getSeconds() + 1);
        var endDate = new Date('2018/9/3 10:57:40');
        var countDown = (endDate.getTime() - startDate.getTime()) / 1000;
        var day = parseInt(countDown / (24 * 60 * 60));
        var h = parseInt(countDown / (60 * 60) % 24);
        var m = parseInt(countDown / 60 % 60);
        var s = parseInt(countDown % 60);
        if (day.toString() == "NaN") {
            document.getElementById('time').innerHTML = '<span class="ti">------</span>';

        } else {
            if (countDown <= 0) {
                document.getElementById('time').innerHTML = '<span class="ti">------</span>';

            } else {
                document.getElementById('wen').innerHTML ='距结束';
                document.getElementById('time').innerHTML = '<span class="ti">' + day + '</span><span class="ti1">天</span><span class="ti">' + p(h) + '</span><span class="ti1">时</span><span class="ti">' + p(m) + '</span><span class="ti1">分</span><span class="ti">' + p(s) + '</span><span class="ti1">秒</span>';
            }
        }
        var int1 = setTimeout('getMyTime1(1)',1000);
        if (countDown <= 0) {
            clearTimeout(int1);
        }
    }
    function GetTime1(type) {
        var startDate = $("#time6").val();
        if (startDate == "") {
            dtime1(type);
        }
        if (type == 0) {
            getMyTime1(type);
        }
    }
    function dtime() {
        var urlOne = "http://www1.rmfysszc.gov.cn/Login1/GetTime.shtml";
        var pid = '1';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { id: pid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {
            },
            success: function (data) {
                $("#time5").val(data.Count);
                getMyTime();
            }
        });
    }
    dtime();
    var pstate="0";
    function IsFinish(id1,id2) {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/Finish.shtml";
        var oid = '93675';
        var pid = '1147887';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { oid:oid,pid:pid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {
            },
            success: function (data) {
                if(data.state=="0"){
                    startDate="2018/9/4 10:57:40";
                    //竞价结束
                    var fun2 = data.fun1;
                    if(fun2=="1"){
                        //流标
                        $("#time1").html("状态:流标");
                    }else{
                        //成交
                        $("#time1").html("状态:成交; <span class=\"ti\">成交价:"+data.price+"万元</span>");
                    }
                    clearInterval(id1);
                    clearInterval(id2);
                }else if(data.state=="1"){
                    startDate="2018/9/4 10:57:40";
                    //正在进行
                    $("#time1").html("状态:进行中;当前价:<span class=\"ti\">"+data.price+"万元</span>");
                }else if(data.state=="3"){
                    startDate="2018/9/4 10:57:40";
                    clearInterval(id1);
                    clearInterval(id2);
                }else if(data.state=="5"){
                    GetTime1(1);
                }
            }
        });
    }

    function p(n) {
        return n < 10 ? '0' + n : n;
    }
    var startDate=null;
    function getMyTime() {
        if(startDate==null){
            startDate = $("#time5").val();
        }
        startDate = new Date(startDate);
        startDate.setSeconds(startDate.getSeconds() + 1);
        //$("#time5").val(startDate);
        var endDate = new Date('2018/9/7 10:00:00');
        var countDown = (endDate.getTime() - startDate.getTime()) / 1000;
        var day = parseInt(countDown / (24 * 60 * 60));
        var h = parseInt(countDown / (60 * 60) % 24);
        var m = parseInt(countDown / 60 % 60);
        var s = parseInt(countDown % 60);
        if (day.toString() == "NaN") {
            document.getElementById('time').innerHTML = '<span class="ti">------</span>';
        } else {
            if(countDown <= 0){
                document.getElementById('time').innerHTML = '<span class="ti">------</span>';
            }else{
                document.getElementById('time').innerHTML = '<span class="ti">' + day + '</span><span class="ti1">天</span><span class="ti">' + p(h) + '</span><span class="ti1">时</span><span class="ti">' + p(m) + '</span><span class="ti1">分</span><span class="ti">' + p(s) + '</span><span class="ti1">秒</span>';
            }
        }
        var int1 = setTimeout('getMyTime()',1000);
        if (countDown <= 0) {
            var int2 = setInterval("IsFinish("+int2+","+int3+")",10000);
            var int3 = setInterval("GetRecord()",10000);
            IsFinish(int2,int3);
            clearTimeout(int1);
        }
    }
</script>
<script type="text/javascript">
    $(".scrollLoading").scrollLoading();
    function checkregist() {
        var pid = '1147887';
        var oid = '39748';
        $.getJSON("http://www1.rmfysszc.gov.cn/Customer/isRegistHandler1.shtml?pid=" + pid + "&oid="+oid+"&newdate=" + Math.random() + "&jsoncallback=?", function (data) {
            //alert(data.msg);
            if ((data != null) && (data != '')) {
                if (data.msg == '1') {
                    $(".bm").html("<a href=\"http://www1.rmfysszc.gov.cn/customer/idtcheck.shtml?pid=1147887\"><img src=\"/Images/报名.png\"></a>");
                }
                else {
                    $(".bm").html("<a href=\"javascript:void(0)\"><img src=\"/Images/报名2.png\"></a>");
                }
            }
            else {
                $(".bm").html("<a href=\"javascript:void(0)\"><img src=\"/Images/报名2.png\"></a>");
            }
        });


        //setTimeout('checkregist()', 10000);
    }

    checkregist();
    function collection(id,oid) {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/sc.shtml";
        $.ajax({
            type: "get",
            url: urlOne,
            data: { id: id,oid:oid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {

            },
            success: function (data) {
                if (data.name == "3") {
                    alert('您已收藏该项目');
                } else if (data.name == "2") {
                    alert('请登录后收藏');
                } else if (data.name == "0") {
                    alert('收藏失败');
                } else if (data.name == "1") {
                    alert('收藏成功');
                } else {
                    alert('收藏失败');
                }
            }
        });
    }
    function collection1() {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/GetCollection.shtml";
        var pid = '93675';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { id: pid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {
            },
            success: function (data) {
                $(".sc").html(data.Count);
                $(".hits").html(data.Hits);
            }
        });
    }
    function yxq() {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/yxq.shtml";
        var pid = '1147887';
        var oid = '39748';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { pid: pid,oid:oid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {

            },
            success: function (data) {
                $(".yxq").html(data.Count);
            }
        });
    }
    function bmnumber() {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/GetbmNumber.shtml";
        var pid = '1147887';
        var oid = '39748';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { pid: pid,oid:oid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {

            },
            success: function (data) {
                $(".bmnumber").html(data.Count);
                if(data.Count=="--"){
                    $(".bmnumber").attr("title","按法院要求，不显示报名人数");
                }
            }
        });
    }
    function GetRecord() {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/Record.shtml";
        var pid = '1147887';
        var oid = '93675';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { pid: pid,oid:oid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {

            },
            success: function (data) {
                $("#jjjl1").html(data.Count);
            }
        });
    }
    function getcj() {
        var urlOne = "http://www1.rmfysszc.gov.cn/GetHtml.aspx";
        var pid = 'https://auction.rmfysszc.gov.cn/BidResults.aspx?source=663d5e27-425f-4469-92d2-21bf1c14823b&sourceNumber=20180101010606&time=2018-09-03&oid=39748';
        $.ajax({
            type: "get",
            url: urlOne,
            data: { url: pid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {

            },
            success: function (data) {
                if(data.mark=="1"){
                    $("#result1").css("display","none");
                }
                $("#cjs1").html(data.Count);
                Getlb();
            }
        });
    }
    function Getlb() {
        var urlOne = "http://www1.rmfysszc.gov.cn/Object/Getlb.shtml";
        var oid = '93675';
        $.ajax({
            type: "get",
            url: urlOne,
            data: {oid: oid },
            dataType: "jsonp",
            jsonp: "jsoncallback",
            beforeSend: function (data, http) {
            },
            success: function (data) {
                $("#result1").css("display","");
                $("#cjs1").html(data.Count);
            }
        });
    }
    GetRecord();
    getcj();
    bmnumber();
    yxq();
    collection1();
    Getlb();
</script>
<script type="text/javascript">
    $("#Nav div a").click(function () {
        $(this).removeClass("cur2").addClass("cur");
        $(this).parent().siblings().children().removeClass("cur").addClass("cur2");
    })
</script>

<script>
    $(window).load(function () {
        $("#Nav").sticky({ topSpacing: 0 });
    });
    var src4;
    $(".nav").hover(function () {
        var index = $(".nav").index(this);
        if (index == 1) {

        } else {
            var str = $(this).attr("src");
            src4 = str;
            var src1 = str.substr(0, str.length - 4);
            var src = src1 + "点击.png";
            $(this).attr("src", src);
        }
    }, function () {
        var index1 = $(".nav").index(this);
        if (index1 == 1) {

        } else {
            $(this).attr("src", src4);
        }
    })
</script>
<script type="text/javascript">
    window._bd_share_config = {
        common : {
            bdText : '人民法院诉讼资产网_司法拍卖_'+document.title,
            bdDesc : '人民法院诉讼资产网_司法拍卖_'+document.title,
            bdUrl : 'http://www.rmfysszc.gov.cn/statichtml/rm_obj/93675.shtml',
            bdPic : 'http://files.cquae.com/Upload/201809/03/QQ图片20180831115309._sm_.jpg',
            bdMini : 2,
            bdMiniList : ["weixin","tsina","tqf","sqq","qzone","tqq","tieba","bdysc","renren","fx","ty","youdao","mshare","mail","copy","print"],
        },
        slide : [{
            bdImg : 0,
            bdPos : "right",
            bdTop : 220
        }],
    }
    with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?cdnversion='+~(-new Date()/36e5)];
</script>
<script>
    //内容信息导航吸顶
    $(document).ready(function () {
        var navHeight = $("#navHeight").offset().top;
        var navFix = $("#nav-wrap");
        $(window).scroll(function () {
            if ($(this).scrollTop() > navHeight) {
                navFix.addClass("navFix");
            }
            else {
                navFix.removeClass("navFix");
            }
        })
    })
    //内容信息导航锚点
    $('.nav-wrap').navScroll({
        mobileDropdown: true,
        mobileBreakpoint: 768,
        scrollSpy: true
    });

    $('.click-me').navScroll({
        navHeight: 0
    });

    $('.nav-wrap').on('click', '.nav-mobile', function (e) {
        e.preventDefault();
        $('.nav-wrap ul').slideToggle('fast');
    });


    $('#nav-wrap li').click(function(){
        $(this).children().addClass('active').parent().siblings().children().removeClass('active');
    })
</script>
'''
url = 'http://www.rmfysszc.gov.cn/statichtml/rm_obj/93686.shtml'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'www.rmfysszc.gov.cn=20111166; __jsluid=3d33c5d609cc877f1db4b258e86aecd6; UM_distinctid=1659d414285264-0e64f05d588c5b-43480420-1fa400-1659d414287a0; CNZZDATA3765988=cnzz_eid%3D828606482-1535936640-%26ntime%3D1535954664',
'Host': 'www.rmfysszc.gov.cn',
'Refere': 'http://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
res = requests.get(url,headers = headers)
res.encoding='utf-8'
print res.text
html = res.text

title = re.findall(re.compile(r"<title>(.*?)</title>", re.S), html.decode('Utf-8','ignore'))[0]
startPrice = re.findall(re.compile(r'<span style="font-size:22px;color:#d91615; padding:10px; font-family:SimHei">(.*?)</span>', re.S), html.decode('utf-8'))[0]
accessPrice = re.findall(re.compile(r'<td><span style="color:#515050;">.*?</span><span style="color:#d91615;font-size:16px;">(.*?)</span>', re.S), html.decode('utf-8'))[0]
cashPrice = re.findall(re.compile(r'<td><span style="color:#515050;">.*?</span><span style="color:#d91615;font-size:16px;">(.*?)</span>', re.S), html.decode('utf-8'))[1]
data = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[2]
paimaiStatus = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[3]
court = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[4]
user = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[5]
phone = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[6]
 
print '标题:'+title
print '起拍价:'+startPrice
print '评估价:'+accessPrice
print '保证金:'+cashPrice
print data
print paimaiStatus
print court
print user
print phone













