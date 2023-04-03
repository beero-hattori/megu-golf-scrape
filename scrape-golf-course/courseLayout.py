import time
from numpy import safe_eval
from soupsieve import select
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import uuid


prefectureCourseUrlsDf = pd.read_csv('./scrape-golf-course/prefectureCourseUrls.csv')
addressLatLonDf = pd.read_csv('./scrape-golf-course/addressLatLon.csv')


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

srGolfCourseIdArray = []
srCourseNameArray = []
srCourseType1NameArray = []
srCourseType2NameArray = []
srTeeArray = []
srArray = []
srGenderArray = []


def slope_rating(courseName,gender,golfCourseId):
    try:
        df = pd.read_csv(f'./scrape-golf-course/slope-rating/{courseName}-{gender}.csv')
        courses = df["Course"].values
        Tees = df["Tee"].values
        srs = df["SR"].values
        for i,course in enumerate(courses):
            preCourse = course.split("-")
            # print(f'golfCourseId:{golfCourseId}-courseName:{courseName}-courseType1:{preCourse[0]}-courseType2:{preCourse[1]}-Tee:{Tees[i]}-SR:{srs[i]}-gender:{gender}')
            srGolfCourseIdArray.append(golfCourseId)
            srCourseNameArray.append(courseName)
            srCourseType1NameArray.append(preCourse[0])
            srCourseType2NameArray.append(preCourse[1])
            srTeeArray.append(Tees[i])
            srArray.append(srs[i])
            srGenderArray.append(gender)


            # time.sleep(3)
    except Exception as e:
        return 


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
            

golfCourseIdArray = []
parArray2 = []
courseNameArray = []
inOutArray = []
courseTypeIdArray = []
tieArray2 = []
holeNumberArray = []
yardArray = []


for i,tieArray in enumerate(tieTypes):
    t = tieArray.replace("[","").replace("]","").split(",")
    tiesNumberArray = ties[i].split("],")
    courseName = course[i]
    golfCourseId = golfCourseIds[i]
    inOut = inOuts[i].replace("詳細","")
    parArray = pars[i].replace("[","").replace("]","").replace("'","").replace(" ","").split(",")
    couserTypeId = couserTypeIds[i]
    slope_rating(courseName,"male",golfCourseId)
    slope_rating(courseName,"female",golfCourseId)
    for j,tie in enumerate(tiesNumberArray):
        for k,v in enumerate(t):
            yard = tie.split(",")[k].replace("[","").replace("]","").replace("'","")
            par = parArray[j]
            try:
                holeNumber = j+1
                tieName = v.replace("'","")                
                value = f'{golfCourseId}-par:{par}-{courseName}-{inOut}:{couserTypeId}-{tieName}-holeNumber:{holeNumber}-yard:{yard}'.replace(" ","")
                golfCourseIdArray.append(golfCourseId)
                parArray2.append(par)
                courseNameArray.append(courseName)
                inOutArray.append(inOut)
                courseTypeIdArray.append(couserTypeId)
                tieArray2.append(tieName)
                holeNumberArray.append(holeNumber)
                yardArray.append(yard)


            except:
                continue


# print(f"golfCourseId:{len(srGolfCourseIdArray)}-courseName:{len(srCourseNameArray)}-courseType1Name:{len(srCourseType1NameArray)}-courseType2Name:{len(srCourseType2NameArray)}-tee:{len(srTeeArray)}-sr:{len(srArray)}-gender:{len(srGenderArray)}")


tieDf = pd.DataFrame({
"golfCourseId":golfCourseIdArray,
"courseName":courseNameArray,
"par":parArray2,
"inOut":inOutArray,
"courseTypeId":courseTypeIdArray,
"tie":tieArray2,
"holeNumber":holeNumberArray,
"yard":yardArray
})

slopeRatingDf = pd.DataFrame({
"golfCourseId":srGolfCourseIdArray,
"courseName":srCourseNameArray,
"courseType1Name":srCourseType1NameArray,
"courseType2Name":srCourseType2NameArray,
"tee":srTeeArray,
"sr":srArray,
"gender":srGenderArray
})

slopeRatingDf2 = pd.DataFrame({
"golfCourseId":srGolfCourseIdArray,
"courseName":srCourseNameArray,
"courseType1Name":srCourseType1NameArray,
"courseType2Name":srCourseType2NameArray,
"tee":srTeeArray,
"sr":srArray,
"gender":srGenderArray
})



tieDf = pd.DataFrame({
"golf_course_id":golfCourseIdArray,
"courseName":courseNameArray,
"par":parArray2,
"course_type_name":inOutArray,
"course_type_id":courseTypeIdArray,
"tie":tieArray2,
"course_layout_index":holeNumberArray,
"yard":yardArray
})  

srGolfCourseIdArray3 = []
srCourseNameArray3 = []
srCourseType1NameArray3 = []
srCourseType2NameArray3 = []
srCourseType1IdArray3 = []
srCourseType2IdArray3 = []
srTeeArray3 = []
srArray3 = []
srGenderArray3 = []

for i,srCourseName in enumerate(srCourseNameArray):
    
    
    try:
        tDF1 = tieDf.query(f'courseName == "{srCourseName}" & inOut == "{srCourseType1NameArray[i]}"').index
        index1 = tDF1[0]
        
        tDF2 = tieDf.query(f'courseName == "{srCourseName}" & inOut == "{srCourseType2NameArray[i]}"').index
        index2 = tDF2[0]
        
        srGolfCourseIdArray3.append(srGolfCourseIdArray[i])
        srCourseNameArray3.append(srCourseNameArray[i])
        srCourseType1NameArray3.append(srCourseType1NameArray[i])
        srCourseType2NameArray3.append(srCourseType2NameArray[i])
        srCourseType1IdArray3.append(courseTypeIdArray[index1])
        srCourseType2IdArray3.append(courseTypeIdArray[index2])
        srTeeArray3.append(srTeeArray[i])
        srArray3.append(srArray[i])
        srGenderArray3.append(srGenderArray[i])
        print(srCourseNameArray[i],srGolfCourseIdArray[i])

    except Exception as e:
        print("err",e)
        continue

slopeRatingDf2 = pd.DataFrame({
"golf_course_id":srGolfCourseIdArray3,
"courseName":srCourseNameArray3,
"in_course_name":srCourseType1NameArray3,
"in_course_id":srCourseType1IdArray3,
"out_course_name":srCourseType2NameArray3,
"out_course_id":srCourseType2IdArray3,
"tee":srTeeArray3,
"slope_rating":srArray3,
"gender":srGenderArray3
})

slopeRatingDf.to_csv('./scrape-golf-course/slope-rating.csv',index=False)
tieDf.to_csv('./scrape-golf-course/tie.csv',index=False)
slopeRatingDf2.to_csv('./scrape-golf-course/slope-rating2.csv',index=False)

