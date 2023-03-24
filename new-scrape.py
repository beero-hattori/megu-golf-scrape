# from msilib.schema import tables
from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
df1 = pd.read_csv(f"./final.csv")
uuids = df1["uuid"].to_list()
courses = df1["courseName"].to_list()
preAddress = df1["address"].to_list()
prefectures=os.listdir(path="./日本2")


errorUuids = []
for i,uuid in enumerate(uuids):
    
    for p in prefectures:
        if p in preAddress[i]:
            outdir = f"./日本final/{p}"
            if not os.path.exists(outdir):
                os.mkdir(outdir)
            print("uuid",uuid)
            print("course",courses[i])
            address = preAddress[i]
            url = f"https://reserve.golfdigest.co.jp/golf-course/course-layout/{uuid}"
            headers = {'User-agent': 'Mozilla/5.0'}
            response = requests.get(url=url, headers=headers)
            sleep(2)
            response.encoding = response.apparent_encoding

            try:
                dfs = pd.read_html(response.text)

                courseNames = []
                courseDetail = []
                j=0

                for d in dfs:
                    columnFirst = d.columns.tolist()[0]
                    isDone =False
                    if isDone ==False:
                        if "HOLE：" not in columnFirst:
                            courseNames.append(columnFirst)
                            d.to_csv(f"./日本final/{p}/{uuid}-{columnFirst}-outline.csv",)                    
                        else:
                            
                            courseDetail.append(d)
                            d.to_csv(f"./日本final/{p}/{uuid}-{courseNames[j]}-detail.csv",)
                            j+=1
            except:
                errorUuids.append(uuid)

                    
       
    

    