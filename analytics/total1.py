import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import random
import os
import uuid
from matplotlib.ticker import *
maleDf = pd.read_csv('./total-male.csv')
femaleDf = pd.read_csv('./total-female.csv')
drop_col = ['コース１','コース１.3','コース2','コース2.1','コース2.3']
maleDf.drop(drop_col,axis=1)
femaleDf.drop(drop_col,axis=1)
maleDf = maleDf[maleDf['Par']=='72']
femaleDf = femaleDf[femaleDf['Par']=='72']
genderArray = []
random.seed(0)

for i in range(5000):
  if (i+1)%10 == 0:
    genderArray.append(1)
  else:
    genderArray.append(0)

ages = [0,1,2,3,4,5,6]
maleProbability =  [1.1, 2.2, 10.0, 18.9, 27.8, 28.9, 11.1]
femaleProbability = [0.01,
                     0.02,
                     0.17,
                     0.25,
                     0.26,
                     0.24,
                     0.05]

averageScores = [0,1,2,3,4,5,6]

averageScoreProbability = [0.036,0.263,0.434,0.199,0.048,0.019,0.001]


for i in range(len(maleProbability)):
  maleProbability[i]=round(maleProbability[i]/100,4)

par = 72

totalGrossScoreArray = []
averageScoreArray = []

userIdArray = [x+1 for x in range(5000)]
ageArray = []

for i in range(5000):
  if genderArray[i] == 0:
    p = random.choices(ages,k=1,weights=maleProbability)[0]
    ageArray.append(p)
    if p<6:
      aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
      averageScore = 72+aroundAverageScore*10+random.randint(0,9)
      averageScoreArray.append(averageScore)
    else:
      aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
      averageScore = random.randint(131,150)      
      averageScoreArray.append(averageScore)
  else:
    p = random.choices(ages,k=1,weights=femaleProbability)[0]
    ageArray.append(p)
    if p<6:
      aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
      averageScore = 72+aroundAverageScore*10+random.randint(0,9)
      averageScoreArray.append(averageScore)
    else:
      aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
      averageScore = random.randint(131,150)      
      averageScoreArray.append(averageScore)



userDF = pd.DataFrame({
        'userId':userIdArray,
        'gender':genderArray,
        'age':ageArray,
        'averageScore':averageScoreArray,        
})
gettingDf  = pd.DataFrame({
            'userId':[],
        'gender':[],
        'age':[],
        'averageScore':[],
        'grossScore':[],
        'hiddenScore':[],
        'netScore':[],
        'handicap':[],
        'prevNet':[],
        'corseName':[],
        'courseRating':[],
        'corseType':[],
        'slopeRating':[],
        'weather':[]
})


dfArray = []
df2Array = []

rank = [x+1 for x in range(5000)]
geddingArray = []

for g in range(5000):
  if g+1<=500:
    geddingArray.append(1)
  elif (g+1)%5 ==0 and (g+1)!=5000:
    geddingArray.append(1)
  elif g+1 == 4999:
    geddingArray.append(1)
  else:
    geddingArray.append(0)



for slopeRateWeigth in range(1,101):
  for weatherIndexWeigth in range(1,3):
    for _ in range(100):
        userIdArray2 = []
        genderArray2 = []
        ageArray2 = []
        averageScoreArray2 = []
        hiddenScoreArray = []
        grossScoreArray = []
        netScoreArray = []
        course = []
        corseNameArray = []
        courseRatingArray = []
        slopeRatingArray = []
        corseTypeArray = []
        handicapArray = []
        prevNetArray = []
        weatherArray = []
        slopeRateWeigthArray = []
        weatherIndexWeigthArray = []
        for i in range(len(userIdArray)):
          weatherIndex = random.choices([0,1,2],k=1,weights=[0.7,0.2,1])[0]
          weatherArray.append(weatherIndex)
          slopeRateWeigthArray.append(slopeRateWeigth)   
          weatherIndexWeigthArray.append(weatherIndexWeigth)
          userIdArray2.append(userIdArray[i])
          genderArray2.append(genderArray[i])
          ageArray2.append(ageArray[i])
          averageScoreArray2.append(averageScoreArray[i])
          if genderArray[i] == 0:
            n = np.random.randint(0,len(maleDf))
            corseName = maleDf.iloc[n]['Unnamed: 0']
            corseNameArray.append(corseName)
            courseRating = maleDf.iloc[n]['CourseRating']
            courseRatingArray.append(courseRating)
            slopeRating  = int(maleDf.iloc[n]['SlopeRating'])
            slopeRatingArray.append(slopeRating)
            corseType = maleDf.iloc[n]['コース１.2']
            corseTypeArray.append(corseType)
            p = userDF['age'][i]
            if p<6:
              grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
              hiddenScore = 48+np.random.randint(-2,10)
              hiddenScoreArray.append(hiddenScore)
              grossScoreArray.append(grossScore)
              totalGrossScoreArray.append(grossScore)
              handicap = (hiddenScore*1.5-par)*0.8
              prevNetArray.append(grossScore-handicap)
              netScore = grossScore-handicap-slopeRateWeigth*(slopeRating-55)/10-weatherIndexWeigth*weatherIndex
              handicapArray.append(-handicap-(slopeRating-55)/10-weatherIndex)
              netScoreArray.append(netScore)
            else:     
              grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
              hiddenScore = 48+np.random.randint(-5,10)
              hiddenScoreArray.append(hiddenScore)
              grossScoreArray.append(grossScore)
              totalGrossScoreArray.append(grossScore)
              handicap = (hiddenScore*1.5-par)*0.8
              prevNetArray.append(grossScore-handicap)
              netScore = grossScore-handicap-slopeRateWeigth*(slopeRating-55)/10-weatherIndexWeigth*weatherIndex
              handicapArray.append(-handicap-(slopeRating-55)/10-weatherIndex)
              netScoreArray.append(netScore)
          else:
            n = np.random.randint(0,len(maleDf))
            corseName = femaleDf.iloc[n]['Unnamed: 0']
            corseNameArray.append(corseName)
            courseRating = femaleDf.iloc[n]['CourseRating']
            courseRatingArray.append(courseRating)
            slopeRating  = int(femaleDf.iloc[n]['SlopeRating'])
            slopeRatingArray.append(slopeRating)
            corseType = femaleDf.iloc[n]['コース１.2']
            corseTypeArray.append(corseType)
            p = userDF['age'][i]
            if p<6:
              grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
              hiddenScore = 48+np.random.randint(-2,10)
              hiddenScoreArray.append(hiddenScore)
              grossScoreArray.append(grossScore)
              totalGrossScoreArray.append(grossScore)
              handicap = (hiddenScore*1.5-par)*0.8
              prevNetArray.append(grossScore-handicap)
              netScore = grossScore-handicap-slopeRateWeigth*(slopeRating-55)/10-weatherIndexWeigth*weatherIndex
              handicapArray.append(-handicap-(slopeRating-55)/10-weatherIndex)
              netScoreArray.append(netScore)
            else:
              grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
              hiddenScore = 48+np.random.randint(-5,10)
              hiddenScoreArray.append(hiddenScore)
              grossScoreArray.append(grossScore)
              totalGrossScoreArray.append(grossScore)
              handicap = (hiddenScore*1.5-par)*0.8
              prevNetArray.append(grossScore-handicap)
              netScore = grossScore-handicap-slopeRateWeigth*(slopeRating-55)/10-weatherIndexWeigth*weatherIndex
              handicapArray.append(-handicap-(slopeRating-55)/10-weatherIndex)
              netScoreArray.append(netScore)
            ageArray.append(p)
        userDF2 = pd.DataFrame({
                  'userId':userIdArray2,
                  'gender':genderArray2,
                  'age':ageArray2,
                  'averageScore':averageScoreArray2,
                  'grossScore':grossScoreArray,
                  'hiddenScore':hiddenScoreArray,
                  'netScore':netScoreArray,
                  'handicap':handicapArray,
                  'corseName':corseNameArray,
                  'courseRating':courseRatingArray,
                  'corseType':corseTypeArray,
                  'slopeRating':slopeRatingArray,
                  'slopeRateWeigth':slopeRateWeigthArray,
                  'weather':weatherArray,
                  'weatherIndexWeigth':weatherIndexWeigthArray
                  
                  })
        
        userDF3 = userDF2.sort_values("netScore")
        userDF3['rank'] = rank
        userDF3['getting'] = geddingArray
        df2Array.append(userDF3)


# dfdf = pd.concat(dfArray)
totalDF = pd.concat(df2Array)

df = totalDF.to_csv("./total3.csv")
