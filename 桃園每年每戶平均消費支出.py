import matplotlib.pyplot as plt
import xlrd
import xlwt
import csv
import sys
import numpy as np


from xml.etree import ElementTree
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x


def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")


try:
    url="https://www.dgbas.gov.tw/public/data/open/localstat/011-%E5%90%84%E7%B8%A3%E5%B8%82%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E6%88%B6%E6%B6%88%E8%B2%BB%E6%94%AF%E5%87%BA.xml"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            #contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents=reponse.read().decode("UTF-8")
        else:
            contents=reponse.read()

        """
        fr = open('workfile.txt', 'w')
        fr.write(contents)
        fr.close()
        """


        root = ElementTree.fromstring(contents)
        plt.figure("桃園每年消費支出")
        list1 = []
        list2 = []
        t1 = root.findall("Data/桃園市")
        t2 = root.findall("Data/Year")
        x = 0
        while x < len(t1):
            print("桃園市平均每戶每年消費支出",t2[x].text,"年:", t1[x].text)
            list1.append(int(t2[x].text))  # 問題點字串改數字
            list2.append(int(t1[x].text))  # 問題點
            x = x + 1

        plt.plot(list1, list2, 'r-')
        plt.title('Taoyuan')
        plt.show()


except:
    print("error")

