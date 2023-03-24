import ssl

from time import time
from matplotlib.pyplot import axis
from numpy import safe_eval
from soupsieve import select
import time 
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import numpy as np
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


df = pd.read_csv('./totalCourseUrl.csv')

urls = df['urls'].values
golfCourseId =df['golfCourseIds'].values
prefecture = df["prefecture"].values




def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return: 
    """
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]


courseArray = []
tieArray = []
courseTypeArray = []
tieTypeArray = []
initNoArray = []
initParArray = []
courseLayoutId = []

for i,url in enumerate(urls):
    courseLayoutId.append(i)
    r= requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    text = soup.find_all('h1')
    courseName = text[1].text
    courseArray.append(courseName)
    courseType = soup.find("h3", class_="decoration-line").text
    courseTypeArray.append(courseType)
    dataTable = soup.find("div", class_="data-table")
    dataTable.find('div',class_='like-th').find_all('span')
    likeTh = dataTable.find('div',class_='like-th').find_all('span')
    likeThArray = []
    for th in likeTh:
        if th.text == 'No':
            continue
        elif th.text == 'PAR':
            continue
        else:
            likeThArray.append(th.text)
    tableItems = dataTable.find_all("div", class_="box")
    noArray = []
    parArray = []
    valueArray = []
    
    for i,item in enumerate(tableItems):
        if i ==0:
            continue
        else:
            strItems = str(item).split('</')
            spans = item.find_all('span')
            for j,span in enumerate(spans):
                if j ==0:
                    # print('No',span.text)
                    noArray.append(span.text)
                elif j ==1:
                    # print('PAR',span.text)
                    parArray.append(span.text)
                else:
                    valueArray.append(span.text)
    tieTypeArray.append(likeThArray)
    removeFinalNoArray = noArray[:-1]
    removeFinalParArray = parArray[:-1]
    initNoArray.append(removeFinalNoArray)
    initParArray.append(removeFinalParArray)
    removeFinalValueArray = valueArray[:-1*len(likeThArray)]
    try:
        eachTie = [list(split_list(removeFinalValueArray, len(likeThArray)))]
        tieArray.extend(eachTie)
    except:
        eachTie = [["no","no","no","no","no","no","no","no","no"]]
        tieArray.extend(eachTie)
    time.sleep(3)

df2 = pd.DataFrame({
    "courseLayoutId":courseLayoutId,
    'course':courseArray,
    'courseType':courseTypeArray,
    'no':initNoArray,
    'par':initParArray,
    "tie":tieArray,
    'tieType':tieTypeArray,
    "golfCourseIds":golfCourseId,
    "prefecture":prefecture

})



df2.to_csv('./courseDetail2.csv')


