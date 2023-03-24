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





dfs = []
urls = []
pres = []
preNumbers = []
for i in range(0,47):
    url = f'https://shotnavi.jp/gcguide/searchpref.php?pref={i+1}'
    r= requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find_all("span", itemprop='title')
    pre = title[-1].text
    founds = soup.find_all('a')
    time.sleep(3)    
    obj = {pre:''}
    for f in founds:
        if 'gcinfo_' in str(f.get('href')):
            t = f.get('href')
            text = f'https://shotnavi.jp/gcguide/{t}'
            urls.append(text)
            pres.append(pre)
            preNumbers.append(i+1)




arr1 = np.array([urls,pres,preNumbers])
df = pd.DataFrame(data=arr1).transpose()

df.to_csv('./prefectureCourseUrls.csv')

