import pandas as pd


import os

path = "./total-layout2"

files = os.listdir(path)

dfArray = []


for f in files:
    df = pd.read_csv(path+'/'+f, names=('HOLE：A','HOLE：1.1','HOLE：1.2','HOLE：B','HOLE：2.1','HOLE：2.2','HOLE：C','HOLE：3.1','HOLE：3.2'))
    df['course'] = f
    
    dfArray.append(df)
    
totalDF = pd.concat(dfArray)

df = totalDF.to_csv('./totalCourse.csv', index=False)
