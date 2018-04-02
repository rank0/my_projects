# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
_author_=Captain
IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
'''
from bs4 import BeautifulSoup
import requests,re,random

def get_ip_list():
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')   #获取每一行的所有数据，以列表返回
    https_ip_list = []
    http_ip_list = []
    for i in range(1, len(ips)):  # 从第一行开始，默认从0开始
        ip_info = ips[i]
        tds = ip_info.find_all('td')  #获取每一列的数据，以列表返回
        if re.match(r'HTTPS', tds[5].text):
            temp = str("https://" + tds[1].text + ":" + tds[2].text)
            https_ip_list.append(temp)  # https类型+IP+端口
        else:
            temp = str('http://' + tds[1].text + ':' + tds[2].text)
            http_ip_list.append(temp)  # http类型+IP+端口
    return https_ip_list,http_ip_list

def get_random_ip(https_ip_list,http_ip_list):
    https_ip = random.choice(https_ip_list)
    http_ip = random.choice(http_ip_list)
    proxies = {
        "https": https_ip,
        "http": http_ip,
    }
    return proxies

if __name__ == '__main__':
    https_ip_list, http_ip_list=get_ip_list()
    for i in range(1,7):
        print get_random_ip(https_ip_list,http_ip_list)