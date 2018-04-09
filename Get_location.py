# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
_author_=Captain
'''
#查询IP所属国家位置

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)   # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8') #将默认的ASCII码改为UTF-8编码

def get_locat(host):
    locate = ""
    url = 'http://ip.chinaz.com/?IP={}'.format(host)
    webdata = requests.get(url)
    soup = BeautifulSoup(webdata.text, 'lxml')
    if soup.find_all('p', attrs={'class': 'WhwtdWrap bor-b1s col-gray03'}):
        tmp_locate = soup.find_all('p', attrs={'class': 'WhwtdWrap bor-b1s col-gray03'})
        tmp_locate = tmp_locate[0].find_all('span')
        locate = tmp_locate[-1].get_text()
        return locate
    else:
        return locate

if __name__ == '__main__':
    host='112.74.111.30'
    location = get_locat(host)
    print location