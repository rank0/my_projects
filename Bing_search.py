# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
_author_=Captain
'''
#使用bing查询同IP的网站域名

import re
import requests
from bs4 import BeautifulSoup

def bing(ip):
    webdata = requests.get('http://www.bing.com/search?q=ip:' + ip + '&count=50')
    soup = BeautifulSoup(webdata.text,'lxml')
    match=[]
    temp_list = []
    if soup.find_all('a', attrs={'target': '_blank'}):
        match = soup.find_all('a', attrs={'target': '_blank'})  #获取所有a标签中属性是_blank的，查询到的域名
        re_match = re.compile(r'.+://.+?/')  #非贪婪匹配，只提取协议+域名，网站具体路径不匹配
        for num in range(len(match)-1):
            match[num] = re.findall(re_match,match[num].get('href'))[0]

        for num in range(len(match) - 1):   #去除重复域名
            if match[num] not in temp_list:
                temp_list.append(match[num])
    else:
        pass
    return temp_list

if __name__ == '__main__':
    ipaddress='112.74.111.31'
    domain_list = bing(ipaddress)
    print domain_list
