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


df = pd.read_csv('./t.csv')

urls = df["0"].values
courseUrls = []

for i,url in enumerate(urls):
    courseNumber = url.split('_')[1].split('.')[0]
    courseUrl =  f'https://shotnavi.jp/gcguide/gcinfo_{courseNumber}.htm'
    r= requests.get(courseUrl)
    time.sleep(3)
    soup = BeautifulSoup(r.content, "html.parser")
    founds = soup.find_all('a')
    for f in founds:
        if courseNumber in str(f):
            if 'レイアウト' in f.text:
                if str(f.get('href')) not in  courseUrls:
                    print("https://shotnavi.jp/gcguide/"+str(f.get('href')))
                    courseUrls.append("https://shotnavi.jp/gcguide/"+str(f.get('href')))  

courseUrlsDf = pd.DataFrame({
        "urls":courseUrls,
    })
courseUrlsDf.to_csv('./totalCourseUrl.csv')
