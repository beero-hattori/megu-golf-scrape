import time
from numpy import safe_eval
from soupsieve import select
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import uuid
import datetime

dt = datetime.datetime.now()
ts = datetime.datetime.timestamp(dt)


addressLatLonDF = pd.read_csv('./scrape-golf-course/addressLatLon.csv').reset_index()
prefectureCourseUrlsDF = pd.read_csv("./scrape-golf-course/prefectureCourseUrls.csv")
slopeRatingDF = pd.read_csv("./scrape-golf-course/slope-rating2.csv")

prefectureCourseUrlsDF = prefectureCourseUrlsDF.rename(columns={'0': 'urls', '1': 'prefectureNames',"2":"prefectureCodes"})

urls = prefectureCourseUrlsDF["urls"].values
golfCourseIds = []

for url in urls:
    id = url.split("_")[1].split(".")[0]
    golfCourseIds.append(id)


df = pd.merge(addressLatLonDF, prefectureCourseUrlsDF).drop(columns='Unnamed: 0').drop(columns='index')

df["golfCourseIds"] = golfCourseIds

newCourseName = []
newAddresses = []
newLons = []
newLats = []
newPrefectureCodes = []
newGolfCourseIds = []
newUrls = []
createdAtArray = []
updatedAtArray = []
countryCodeArray = []


for golfCourseId in golfCourseIds:
    try:
        
        spindex = slopeRatingDF.query(f'golfCourseId == {str(golfCourseId)}')["courseName"].values[0]
        courseName = slopeRatingDF.query(f'golfCourseId == {str(golfCourseId)}')["courseName"].values[0]
        
        newDF = df.query(f'golfCourseIds == "{golfCourseId}"')
        # print(courseName,newDF)
        # time.sleep(3)
        
        
        
        # address = newDF["addresses"].values[0]
        # url = newDF["urls"].values[0]
        lon = newDF["lons"].values[0]
        lat = newDF["lats"].values[0]
        p = newDF["prefectureCodes"].values[0]
        newGolfCourseIds.append(golfCourseId)
        newCourseName.append(courseName)
        # newAddresses.append(address)
        newLons.append(lon)
        newLats.append(lat)
        newPrefectureCodes.append(p)  
        newUrls.append(url)      
        countryCodeArray.append("jp")
    except Exception as e:
        # print("err",e)
        continue

finalDF = pd.DataFrame({
    "golf_course_id":newGolfCourseIds,
    "name":newCourseName,
    "prefecture_id":newPrefectureCodes,
    "created_at":int(ts),
    "updated_at":int(ts),
    "country_code":countryCodeArray,
    "lon":newLons,
    "lat":newLats,
        # "addresses":newAddresses,
    # "urls":newUrls

})

finalDF.to_csv("./scrape-golf-course/new-golf-course.csv",index=False)