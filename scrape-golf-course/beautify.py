from time import time
from numpy import safe_eval
from soupsieve import select
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np


# prefectureCourseUrlsDf = pd.read_csv('./scrape-golf-course/prefectureCourseUrls.csv')
# addressLatLonDf = pd.read_csv('./scrape-golf-course/addressLatLon.csv')


courseDetail2 = pd.read_csv('./scrape-golf-course/courseDetail2.csv')

courses = courseDetail2["course"]
golfCourseIds = courseDetail2["golfCourseIds"]

golfCourseNames = []

# print("golfCourseIds",golfCourseIds)

for i,v in enumerate(courses):
    if i == 0:
        continue
    else:
        if courses[i] != courses[i-1]:
            golfCourseNames.append(v)

# print(golfCourseNames)


analytics = pd.read_csv('./analytics/total-male.csv')

c = analytics["Unnamed: 0"]

cArray = []

for i,v in enumerate(c):
    if i == 0:
        continue
    else:
        if c[i] != c[i-1]:
            cArray.append(v)    
print(len(cArray))
        









