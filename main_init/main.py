#-*- coding: utf-8 -*-
#开发团队: ELSTP Studio
#开发人员: Wolf 
#联系方式: QQ:1465217851 emal:1465217851qq.com
#开发时间: 2019/12/25 14:42
#文件名称: main.py
#开发工具: PyCharm

import os
import sys
import requests
import re
from urllib import request as reqs
from bs4 import BeautifulSoup
from ffmpy3 import FFmpeg

ffpat = 'D:\\WORK\\PR\\TikTokP\\ffmpeg\\bin'
inpat = 'D:\\WORK\\PR\\TikTokP\\GET'
outpat = 'D:\\WORK\\PR\\TikTokP\\static\\temp'

def video_mp3(path, name):
    name = outpat + '\\' + name + '.mp3'
    out = '%s\\ffmpeg.exe -i %s -y -f mp3 %s' % (ffpat, path, name)
    print(out)
    print(os.system(out))
    return name
def down(name, url):
    pat = ''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    req = reqs.Request(url, headers=headers)
    result = reqs.urlopen(req)
    res = result.read()
    if os.path.exists('%s\\%s.mp4' % (inpat, name)):
        os.remove('%s\\%s.mp4' % (inpat, name))
    with open('%s\\%s.mp4' % (inpat, name), 'ab') as file:  # 保存到本地的文件名
        file.write(res)
        file.flush()
        pat = '%s\\%s.mp4' % (inpat, name)
        return video_mp3(path=pat, name=name), name
def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    req = requests.get(url=url, headers=headers)
    text = req.text
    url = re.findall(r'playAddr: "(.*?)"', text)
    url = url[0]
    name = ''
    text = BeautifulSoup(text, 'html.parser')
    name = text.find_all('span', class_='inner')[0]
    name = str(name)
    pat = re.compile('<span class="inner">' + '(.*?)' + '</span>', re.S)
    name = pat.findall(name)[0]
    if name == '':
        name = 'temp'
    elif url == '':
        return False
    return down(name=name, url=url)