from time import time
from numpy import safe_eval
from soupsieve import select
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import uuid

addressLatLonDF = pd.read_csv('./scrape-golf-course/addressLatLon.csv').reset_index()
prefectureCourseUrlsDF = pd.read_csv("./scrape-golf-course/prefectureCourseUrls.csv")
prefectureCourseUrlsDF = prefectureCourseUrlsDF.rename(columns={'0': 'urls', '1': 'prefectureNames',"2":"prefectureCodes"})

urls = prefectureCourseUrlsDF["urls"].values
golfCourseIds = []

for url in urls:
    id = url.split("_")[1].split(".")[0]
    golfCourseIds.append(id)


df = pd.merge(addressLatLonDF, prefectureCourseUrlsDF).drop(columns='Unnamed: 0').drop(columns='index')

df["golfCourseIds"] = golfCourseIds



