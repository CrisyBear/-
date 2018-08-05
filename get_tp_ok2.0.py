#coding:utf-8  
import re
import urllib.request
import os
os.chdir("D:/学习/Python/MyCodes/20180801爬取图片/tu/")

# ------ 获取网页源代码的方法 ---
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# ------ 获取帖子内所有图片地址的方法 ------
def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    reg = r'src="([.*\S]*\.jpg)"'   #在这个网页取到的都是缩略图，这个网站的规律是缩略图的名称有“rn”，原图没有
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist


MyUrls = []
MyUrls1 = ["http://www.umei.cc/bizhitupian/meinvbizhi/%s.htm" % i for i in list(range(1,2))]
MyUrls += MyUrls1
#MyUrls2 = ["http://www.umei.cc/bizhitupian/weimeibizhi/%s.htm" % i for i in list(range(2,7))]
#MyUrls += MyUrls2
#说明：把下面##替换为你想爬的网址，备注：该网址需要是分多页显示图片的，可以把range中的“7”替换为你想爬多少页，当然，前提是网站里真的有这么多页
#MyUrls3 = ["##%s.htm" % i for i in list(range(2,7))]
#MyUrls += MyUrls3

 
imgName = 0
for url in MyUrls:
    html = getHtml(url)
    html = html.decode('UTF-8')    
    imgList = getImg(html)
    for imgPath in imgList:
        # ------ 这里最好使用异常处理及多线程编程方式 ------
        #print('原来是：',imgPath)
        if 'rn' in imgPath: 
            imgPath_Original = imgPath.replace('rn','')
            #print('变成了：',imgPath_Original)  
        else:
            imgPath_Original = imgPath
            
        try:
#            f = open('D:\\tu\\'+ str(imgName)+".jpg", 'wb')
            f = open(str(imgName)+".jpg", 'wb')
            f.write((urllib.request.urlopen(imgPath_Original)).read())
            print(imgPath_Original)
            f.close()
        except Exception as e:
            print(imgPath_Original+" error")
        imgName += 1

print("All Done!!!")
