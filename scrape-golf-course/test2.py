import numpy as np
import pandas as pd
import os


prefectures = os.listdir(path='./日本2')
prefecturesObj ={}
prefecturesObj2 ={}

for p in prefectures:
    prefecturesObj[p] = [] 
    prefecturesObj2[p] = []
    prefecturePath = f"./日本2/{p}"

    try:    
        courses = os.listdir(path=prefecturePath)
        for c in courses:
            splitDetail = c.split("詳細")[0]
            if ' ' in splitDetail:
                courseName = splitDetail.split(" ")[0]
                if courseName not in prefecturesObj[p]:
                    prefecturesObj[p].append(courseName)
            else:
                prefecturesObj2[p].append(splitDetail)

    except:
        print("Error")
    df1 = pd.DataFrame({p:prefecturesObj[p]})
    df1.to_csv(f"./日本nonempth/{p}.csv")
    df2 = pd.DataFrame({p:prefecturesObj2[p]})
    df2.to_csv(f"./日本empth/{p}.csv")


    # prefecturesObj[p] = []

# 県の中のゴルフ場の情報を見る
