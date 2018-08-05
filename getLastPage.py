# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:46:12 2018

@author: HJX
"""

#coding:utf-8  
import re
import urllib.request
import os
os.chdir("D:/学习/Python/MyCodes/20180801爬取图片/tu/")

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('UTF-8')  
    return html

url = "http://www.umei.cc/bizhitupian/meinvbizhi/"
html = getHtml(url)
#reg = r'href="(^\d+$\.htm)">末页'  
reg = r'href="([.*\S]*\.htm)"' 
imgre = re.compile(reg)
imglist = re.findall(imgre, html)

for url2 in imglist:
    html2 = getHtml(url2)
    
