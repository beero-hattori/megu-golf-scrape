from time import time
from numpy import safe_eval
from soupsieve import select
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import uuid


# prefectureCourseUrlsDf = pd.read_csv('./scrape-golf-course/prefectureCourseUrls.csv')
# addressLatLonDf = pd.read_csv('./scrape-golf-course/addressLatLon.csv')


courseDetail2 = pd.read_csv('./scrape-golf-course/courseDetail2.csv')


tieTypes = courseDetail2["tieType"]
course = courseDetail2["course"]
courseType = courseDetail2["courseType"]
ties = courseDetail2["tie"]
inOuts = courseDetail2["courseType"]
courseLayoutId = courseDetail2["courseLayoutId"]
golfCourseIds = courseDetail2["golfCourseIds"]
pars = courseDetail2["par"]
courseIds = []
couserTypeIds = []


golfCourseIds = courseDetail2["golfCourseIds"]

golfCourseNames = []


for i,v in enumerate(golfCourseIds):
    uid = str(uuid.uuid4())
    if i == 0:

        courseIds.append(uid)
    else:
        if golfCourseIds[i] != golfCourseIds[i-1]:
            courseIds.append(uid)
        else:
            courseIds.append(courseIds[i-1])
            
for i,v in enumerate(courseType):
    uid = str(uuid.uuid4())
    if i == 0:

        couserTypeIds.append(uid)
    else:
        if courseType[i] != courseType[i-1]:
            couserTypeIds.append(uid)
        else:
            couserTypeIds.append(couserTypeIds[i-1])
            



for i,tieArray in enumerate(tieTypes):
    t = tieArray.replace("[","").replace("]","").split(",")
    tiesNumberArray = ties[i].split("],")
    courseName = course[i]
    golfCourseId = golfCourseIds[i]
    inOut = inOuts[i].replace("詳細","")
    parArray = pars[i].replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
    courseId = courseIds[i]
    couserTypeId = couserTypeIds[i]
    

    for j,tie in enumerate(tiesNumberArray):
        
        for k,v in enumerate(t):
            yard = tie.split(",")[k].replace("[","").replace("]","").replace("'","")
            par = parArray[j]
            try:
                holeNumber = j+1
                tieName = v.replace("'","")
                
                value = f'{golfCourseId}-par:{par}-{courseName}-{inOut}:{couserTypeId}-{tieName}-holeNumber:{holeNumber}-yard:{yard}'.replace(" ","")
                print(value)
            except:
                continue
        
