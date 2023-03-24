import uuid
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import os
import pandas as pd



path1 = "./日本empty/total.csv"
df = pd.read_csv(path1)
df2 = df.drop(["Unnamed: 0"], axis=1,index=None)
uuids = df2["uuid"].to_list()
newUuids = []

for x in uuids:    
    newUuids.append(x.split("&")[0])

df3 = df2.drop(["uuid"], axis=1,index=None)
df3["uuid"] = newUuids
total1 = df3.drop_duplicates(subset=['uuid'], keep='first')
print("total1",total1)
path2 = "./日本pend"

prefs = os.listdir(path=path2)

dfs = []
for pref in prefs:
    p = path2+"/"+pref+"/total.csv"    
    dfs.append(pd.read_csv(p))

df3 = pd.concat(dfs)
df4 = df3.drop(["Unnamed: 0"], axis=1,index=None)

uuids2 = df4["uuid"].to_list()
newUuids2 = []
for x in uuids2:    
    newUuids2.append(str(x).split("&")[0])

df5 = df4.drop(["uuid"], axis=1,index=None)
df5["uuid"] = newUuids2
total2 = df5.drop_duplicates(subset=['uuid'], keep='first')

print("pd.concat([total1,total2])",)

pd.concat([total1,total2]).to_csv("./final.csv")

