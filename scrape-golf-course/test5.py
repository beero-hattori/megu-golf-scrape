import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import os
import pandas as pd
import unicodedata

# finalからuuidとゴルフ場名を取得
df1 = pd.read_csv(f"./final.csv")

# uuidとゴルフ場名のそれぞれのリストを用意

    
uuids = df1["uuid"].to_list()
courses = df1["courseName"].to_list()
preAddress = df1["address"].to_list()

# #日本2のファイル一覧を取得。
dirs=os.listdir(path="./日本2")


prefecturesObj={}

for dir in dirs:
    prefecturesObj[dir] = []


for i,a in enumerate(preAddress):
    for p in prefecturesObj:
        if p in a:
            prefecturesObj[p].append({"address":a,"uuid":uuids[i],"courseName":courses[i],"pref":p})

print("prefecturesObj",prefecturesObj)



for p in prefecturesObj:
    try:
        for item in prefecturesObj[p]:
            prefPath = f"./日本2 copy/{p}"
            files=os.listdir(path=prefPath)
            for i,file in enumerate(files):
            
                prePath = prefPath+"/"+file
                modifyiedPath = unicodedata.normalize('NFC', prePath)
                for j,course in enumerate(courses):
                    if course in modifyiedPath:
                        os.rename(modifyiedPath, re.sub(course, str(uuids[j]), modifyiedPath)) 
        
    except:
        continue

# for dir in dirs:
#     try:
#         prefPath = f"./日本2 copy/{dir}"
        
#         print(dir,prefecturesObj[dir])

#         files=os.listdir(path=prefPath)
#         for i,file in enumerate(files):
            
#             prePath = prefPath+"/"+file
#             modifyiedPath = unicodedata.normalize('NFC', prePath)
#             for j,course in enumerate(courses):
#                 if course in modifyiedPath:
#                     os.rename(modifyiedPath, re.sub(course, str(uuids[j]), modifyiedPath)) 


                    

            
    # except:
    #     continue



# print("t",t)  