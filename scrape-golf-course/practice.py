import ssl

from time import time
import pandas as pd
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


totalCourseUrlDF = pd.read_csv('/Users/hattoriakirasatoru/Desktop/programming/scrape-golf-main/JAPAN/totalCourseUr.csv')
courseDetailDF = pd.read_csv('./scrape-golf-main/JAPAN/courseDetail.csv')



courseLayoutIds = []

for i,url in enumerate(totalCourseUrlDF["golfCourseId"].values):
    courseLayoutIds.append(i)



                    

df = pd.DataFrame({
        "course":courseDetailDF["course"].values,
        "courseType":courseDetailDF["courseType"].values,
        "no":courseDetailDF["no"].values,
        "par":courseDetailDF["par"].values,
        "tie":courseDetailDF["tie"].values,
        "tieType":courseDetailDF["tieType"].values,
            "courseLayoutId":courseLayoutIds,
        "golfCourseIds":totalCourseUrlDF["golfCourseId"].values,
    "prefecture":totalCourseUrlDF["prefecture"].values
    })


df.to_csv('./courseDetail2.csv')

