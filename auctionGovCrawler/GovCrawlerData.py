#coding=utf-8
'''
Created on 2018-9-3

@author: Administrator
'''
import requests
import json
import re
import urllib2
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
from mysql import Mysql
reload(sys)
sys.setdefaultencoding('utf8')

class AuctionCrawler:
    def getIp(self):
        ip_port = []
        ipList = mysql.getIP()
        for (ip,) in ipList:
            ip_port.append(ip)
        return ip_port
    def getHeader(self):
        headers = {
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'keep-alive',
                   'Content-Length': '117',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Cookie': 'ASP.NET_SessionId=ewn1ve2vaywitepzcbmesrbm; rmfysszc.gov.cn=20111241; __jsluid=c2b1ec9bc6b1239096a7db4b065dbb97; UM_distinctid=1659d414285264-0e64f05d588c5b-43480420-1fa400-1659d414287a0; CNZZDATA3765988=cnzz_eid%3D1443080457-1535936640-http%253A%252F%252Fwww.rmfysszc.gov.cn%252F%26ntime%3D1535942040',
                   'Host': 'www1.rmfysszc.gov.cn',
                   'Origin': 'http://www1.rmfysszc.gov.cn',
                   'Referer': 'http://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest'}
        return headers
    def getItemData(self,id):
        ip_port = self.getIp()
        #proxie = {"http": self.proxies[random.randint(0, 999)]}
        proxies = {"http":ip_port[random.randint(0, 999)]}
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
        url = 'http://www.rmfysszc.gov.cn/statichtml/rm_obj/' + str(id)
        print url
        print id[0:5]
        maxTryNum = 10
        html = ''
        for tries in range(maxTryNum):
            try:
                #ctx = ssl._create_unverified_context()
                res = requests.get(url,headers = headers,timeout = 30)
                res.encoding='utf-8'
                #使用代理访问的情况
                html = res.text
                #使用真实ip访问
                #html = opener.open(req).read()
                break
            except:
                if tries < (maxTryNum - 1):
                    continue
                else:
                    print "Has tried %d times to access url %s, all failed!", maxTryNum, url
                    break
        jsonData = {}
        #print html
        title = re.findall(re.compile(r"<title>(.*?)</title>", re.S), html.decode('utf-8'))[0]
        startPrice = re.findall(re.compile(r'<span style="font-size:22px;color:#d91615; padding:10px; font-family:SimHei">(.*?)</span>', re.S), html.decode('utf-8'))[0]
        accessPrice = re.findall(re.compile(r'<td><span style="color:#515050;">.*?</span><span style="color:#d91615;font-size:16px;">(.*?)</span>', re.S), html.decode('utf-8'))[0]
        cashPrice = re.findall(re.compile(r'<td><span style="color:#515050;">.*?</span><span style="color:#d91615;font-size:16px;">(.*?)</span>', re.S), html.decode('utf-8'))[1]
        date = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[2]
        paimaiStatus = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[3]
        court = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[4]
        user = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[5]
        phone = re.findall(re.compile(r'<td><span style="color:#515050;">(.*?)</span></td>', re.S), html.decode('utf-8'))[6]
        
        jsonData['auctionId'] = id[0:5]
        jsonData['url'] = url
        jsonData['title'] = title
        jsonData['startPrice'] = startPrice
        jsonData['accessPrice'] = accessPrice
        jsonData['cashPrice'] = cashPrice
        jsonData['date'] = date
        jsonData['paimaiStatus'] = paimaiStatus
        jsonData['court'] = court
        jsonData['user'] = user
        jsonData['phone'] = phone
        if jsonData['title'].__contains__('"'):
            jsonData['title'] = jsonData['title'].replace('"',"")
        
        mysql.insertData(jsonData)
        print '抓取成功'
        
    def getAllData(self):
        ip_port = self.getIp()
        #proxie = {"http": self.proxies[random.randint(0, 999)]}
        proxies = {"http":ip_port[random.randint(0, 999)]}
        headers = self.getHeader()
        for i in range(228, 301):
            data = {"type":0,"page":i,"name":"","area":"","state":"0","time":"0","time1":"","time2":"","money":"",
                    "money1":"",
                    "number":0,
                    "fid1":"",
                    "fid2":"",
                    "fid3":"",
                    "order":0,
                    "include":""
                    }
            respons = requests.post('http://www1.rmfysszc.gov.cn/ProjectHandle.shtml',headers = headers,data = data)
            print respons.status_code
            if respons.status_code == 200:
                js = json.loads(respons.text)
                html = js['html']
                idList = re.findall(re.compile(r"<div class='p_img'><a href='Handle/(.*?)'", re.S), html)
                for id in idList:
                    self.getItemData(id)
            
auctionCrawler = AuctionCrawler()
mysql = Mysql()
auctionCrawler.getAllData()





