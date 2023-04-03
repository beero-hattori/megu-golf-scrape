import ssl

from time import time
from numpy import safe_eval
from soupsieve import select
import time 
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
import urllib.parse




prefectures = [
  '北海道',
  '青森県',
  '岩手県',
  '宮城県',
  '秋田県',
  '山形県',
  '福島県',
  '茨城県',
  '栃木県',
  '群馬県',
  '埼玉県',
  '千葉県',
  '東京都',
  '神奈川県',
  '新潟県',
  '富山県',
  '石川県',
  '福井県',
  '山梨県',
  '長野県',
  '岐阜県',
  '静岡県',
  '愛知県',
  '三重県',
  '滋賀県',
  '京都府',
  '大阪府',
  '兵庫県',
  '奈良県',
  '和歌山県',
  '鳥取県',
  '島根県',
  '岡山県',
  '広島県',
  '山口県',
  '徳島県',
  '香川県',
  '愛媛県',
  '高知県',
  '福岡県',
  '佐賀県',
  '長崎県',
  '熊本県',
  '大分県',
  '宮崎県',
  '鹿児島県',
  '沖縄県',
]

golfCourseLinks = []

for v in prefectures:
    time.sleep(3)
    courseUrl =  f'https://golfly.jp/courses/{v}'

    r= requests.get(courseUrl)
    soup = BeautifulSoup(r.content, "html.parser")
    aS = soup.find_all("a",  class_="block py-4 border-b border-gray-400")
    for i in aS:
        href = i.get("href")
        href = href.replace(v,urllib.parse.quote(v))
        href = "https://golfly.jp"+href
        
        golfCourseLinks.append(href)

maleTables = []
femaleTables = []



for url in golfCourseLinks:
    # time.sleep(1)
    r= requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    

    try:
        name = soup.find("div",class_="mt-4 mb-2 flex justify-between text-primary text-lg").text
        time.sleep(3)
        tables = pd.read_html(url,attrs={"class": "w-full svelte-194kye2"})
        maleData = tables[0]
        maleData.to_csv(f'./scrape-golf-course/slope-rating/{name}-male.csv', index = False)
        femaleData = tables[1]
        femaleData.to_csv(f'./scrape-golf-course/slope-rating/{name}-female.csv', index = False)      
    except Exception as e:
        print("e",e)
    
# print(len(maleTables))






