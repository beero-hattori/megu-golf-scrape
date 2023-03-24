import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split
# import xgboost as xgb
# import plotly.express as px
# from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import random
import os
import uuid
from matplotlib.ticker import *
random.seed(0)

maleDf = pd.read_csv('./total-male.csv')
femaleDf = pd.read_csv('./total-female.csv')
maleDf = maleDf[maleDf['Par']=='72']
femaleDf = femaleDf[femaleDf['Par']=='72']
genderArray = []

# for i in range(5000):
#   if (i+1)%10 == 0:
#     genderArray.append(1)
#   else:
#     genderArray.append(0)

# ages = [0,1,2,3,4,5,6]
# maleProbability =  [1.1, 2.2, 10.0, 18.9, 27.8, 28.9, 11.1]
# femaleProbability = [0.01,
#                      0.02,
#                      0.17,
#                      0.25,
#                      0.26,
#                      0.24,
#                      0.05]

# averageScores = [0,1,2,3,4,5,6]

# averageScoreProbability = [0.036,0.263,0.434,0.199,0.048,0.019,0.001]


# for i in range(len(maleProbability)):
#   maleProbability[i]=round(maleProbability[i]/100,4)

# par = 72

# totalGrossScoreArray = []
# averageScoreArray = []

# userIdArray = [x+1 for x in range(5000)]
# ageArray = []

# for i in range(5000):
#   if genderArray[i] == 0:
#     p = random.choices(ages,k=1,weights=maleProbability)[0]
#     ageArray.append(p)
#     if p<6:
#       aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
#       averageScore = 72+aroundAverageScore*10+random.randint(0,9)
#       averageScoreArray.append(averageScore)
#     else:
#       aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
#       averageScore = random.randint(131,150)      
#       averageScoreArray.append(averageScore)
#   else:
#     p = random.choices(ages,k=1,weights=femaleProbability)[0]
#     ageArray.append(p)
#     if p<6:
#       aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
#       averageScore = 72+aroundAverageScore*10+random.randint(0,9)
#       averageScoreArray.append(averageScore)
#     else:
#       aroundAverageScore = random.choices(averageScores,k=1,weights=averageScoreProbability)[0]
#       averageScore = random.randint(131,150)      
#       averageScoreArray.append(averageScore)



# userDF = pd.DataFrame({
#         'userId':userIdArray,
#         'gender':genderArray,
#         'age':ageArray,
#         'averageScore':averageScoreArray,        
# })
# gettingDf  = pd.DataFrame({
#             'userId':[],
#         'gender':[],
#         'age':[],
#         'averageScore':[],
#         'grossScore':[],
#         'hiddenScore':[],
#         'netScore':[],
#         'handicap':[],
#         'prevNet':[],
#         'corseName':[],
#         'courseRating':[],
#         'corseType':[],
#         'slopeRating':[],
#         'weather':[]
# })


# dfArray = []
# df2Array = []

# rank = [x+1 for x in range(5000)]
# geddingArray = []

# for g in range(5000):
#   if g+1<=500:
#     geddingArray.append(1)
#   elif (g+1)%5 ==0 and (g+1)!=5000:
#     geddingArray.append(1)
#   elif g+1 == 4999:
#     geddingArray.append(1)
#   else:
#     geddingArray.append(0)

# def computeNetScore():
#   print('test')
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def get_integral_value_combination(list, target):
#     def a(idx, l, r, t):
#         if t == sum(l): r.append(l)
#         elif t < sum(l): return
#         for u in range(idx, len(list)):
#             a((u + 1), l + [list[u]], r, t)
#         return r
#     return a(0, [], [], target)


# print(get_integral_value_combination(list, 48))


# def courseLayoutDF(clubName,corseName):
#   courseLayout = f'./total-layout2/{clubName} {corseName}詳細.csv'

#   # f'/content/drive/MyDrive/golf/total-female.csv'
#   df = pd.read_csv(courseLayout)
#   # cols = [2,3,5,6,8,9]
#   # dropDF = df.drop(df.columns[cols],axis=1,inplace=True)
#   # afterDF = dropDF[dropDF.iloc[1].str.contains('PAR')]

#   # return afterDF
#   return df

folders = os.listdir('./total-layout2')

print('folders',folders)

# for _ in range(1):
#     userIdArray2 = []
#     genderArray2 = []
#     ageArray2 = []
#     averageScoreArray2 = []
#     hiddenScoreArray = []
#     grossScoreArray = []
#     netScoreArray = []
#     course = []
#     clubNameArray = []
#     corse1NameArray = []
#     corse2NameArray = []
#     courseRatingArray = []
#     slopeRatingArray = []
#     corseTypeArray = []
#     handicapArray = []
#     prevNetArray = []
#     weatherArray = []
#     slopeRateWeigthArray = []
#     weatherIndexWeigthArray = []
#     for i in range(len(userIdArray)):
#       weatherIndex = -1*random.choices([0,1,2],k=1,weights=[0.7,0.2,1])[0]
#       weatherArray.append(weatherIndex)
#       # slopeRateWeigthArray.append(slopeRateWeigth)   
#       # weatherIndexWeigthArray.append(weatherIndexWeigth)
#       userIdArray2.append(userIdArray[i])
#       genderArray2.append(genderArray[i])
#       ageArray2.append(ageArray[i])
#       averageScoreArray2.append(averageScoreArray[i])
#       if genderArray[i] == 0:
#         n = np.random.randint(0,len(maleDf))
#         clubName = maleDf.iloc[n]['Unnamed: 0.1']
#         clubNameArray.append(clubName)
#         corse1Name = maleDf.iloc[n]['コース１']
#         corse1NameArray.append(corse1Name)
#         corse2Name = maleDf.iloc[n]['コース2']
#         corse2NameArray.append(corse2Name)
#         courseRating = maleDf.iloc[n]['CourseRating']
#         courseRatingArray.append(courseRating)
#         slopeRating  = int(maleDf.iloc[n]['SlopeRating'])
#         slopeRatingArray.append(slopeRating)
#         corseType = maleDf.iloc[n]['コース１.2']
#         corseTypeArray.append(corseType)


#         corse1NameDF = courseLayoutDF(clubName,corse1Name)
#         # corse2NameDF = courseLayoutDF(clubName,corse2Name)
#         print('corse1NameDF',corse1NameDF)

#         p = userDF['age'][i]
#         # if p<6:
#         #   grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
#         #   hiddenScore = 48+np.random.randint(-2,10)
#         #   hiddenScoreArray.append(hiddenScore)
#         #   grossScoreArray.append(grossScore)
#         #   totalGrossScoreArray.append(grossScore)
#         #   handicap = (hiddenScore*1.5-par)*0.8
#         #   prevNetArray.append(grossScore-handicap)
          
#         #   # netScore = grossScore-handicap-(slopeRating-55)/10+weatherIndexWeigth*weatherIndex
#         #   handicapArray.append(-handicap-(slopeRating-55)/10+weatherIndex)
#         #   netScoreArray.append(netScore)
#         # else:     
#         #   grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
#         #   hiddenScore = 48+np.random.randint(-5,10)
#         #   hiddenScoreArray.append(hiddenScore)
#         #   grossScoreArray.append(grossScore)
#         #   totalGrossScoreArray.append(grossScore)
#         #   handicap = (hiddenScore*1.5-par)*0.8
#         #   prevNetArray.append(grossScore-handicap)
          
#         #   # netScore = grossScore-handicap-(slopeRating-55)/10+weatherIndexWeigth*weatherIndex
          
#         #   handicapArray.append(-handicap-(slopeRating-55)/10+weatherIndex)
#         #   netScoreArray.append(netScore)
#       else:
#         n = np.random.randint(0,len(femaleDf))
#         clubName = femaleDf.iloc[n]['Unnamed: 0']
#         clubNameArray.append(clubName)
#         corse1Name = femaleDf.iloc[n]['コース１']
#         corse1NameArray.append(corse1Name)
#         corse2Name = femaleDf.iloc[n]['コース2']
#         corse2NameArray.append(corse2Name)
#         courseRating = femaleDf.iloc[n]['CourseRating']
#         courseRatingArray.append(courseRating)
#         slopeRating  = int(femaleDf.iloc[n]['SlopeRating'])
#         slopeRatingArray.append(slopeRating)
#         corseType = femaleDf.iloc[n]['コース１.2']
#         corseTypeArray.append(corseType)
#         p = userDF['age'][i]
#         # if p<6:
#         #   grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
#         #   hiddenScore = 48+np.random.randint(-2,10)
#         #   hiddenScoreArray.append(hiddenScore)
#         #   grossScoreArray.append(grossScore)
#         #   totalGrossScoreArray.append(grossScore)
#         #   handicap = (hiddenScore*1.5-par)*0.8
#         #   prevNetArray.append(grossScore-handicap)
#         #   growth = grossScore-averageScore
#         #   # ここにパラメーターが来るように
#         #   growthArray = [-1,-2,-3]
#         #   if -10<=growth<0:
#         #     growth = growthArray[0]
#         #   elif -20<=growth<-10:
#         #     growth = growthArray[1]
#         #   elif  -30<=growth<-20:
#         #     growth = growthArray[2]
#         #   # ここにパラメーターが来るように
#         #   bunkerBonusProbability = []
#         #   OBBonusProbability = []
#         #   lostBallBonusProbability = []
#         #   bunkerBonus = 0
#         #   OBBonus = 0
#         #   lostBallBonus = 0
#         #   if random.choices([0,1],k=1,weights=bunkerBonusProbability)[0] ==1:
#         #     # 将来的におそらくここにもパラメーターがくる
#         #     bunkerBonus = -5
#         #   if random.choices([0,1],k=1,weights=OBBonusProbability)[0] ==1:
#         #     # 将来的におそらくここにもパラメーターがくる
#         #     OBBonus = -5
#         #   if random.choices([0,1],k=1,weights=lostBallBonusProbability)[0] ==1:
#         #     # 将来的におそらくここにもパラメーターがくる
#         #     lostBallBonus = -5
          
#         #   netScore = grossScore-handicap-(slopeRating-55)/10-weatherIndex+growth+bunkerBonus+OBBonus+lostBallBonus
          
#         #   handicapArray.append(-handicap-(slopeRating-55)/10-weatherIndex)
#         #   netScoreArray.append(netScore)
#         # else:
#         #   grossScore = userDF['averageScore'][i]+np.random.randint(-5,10)
#         #   hiddenScore = 48+np.random.randint(-5,10)
#         #   hiddenScoreArray.append(hiddenScore)
#         #   grossScoreArray.append(grossScore)
#         #   totalGrossScoreArray.append(grossScore)
#         #   handicap = (hiddenScore*1.5-par)*0.8
#         #   prevNetArray.append(grossScore-handicap)
#         #   # averageScoreと重みの積だとうまい人が納得しない。
#         #   # うまい人があんまりやらなくて下手な人がやる
#         #   # パット数、池ぽちゃ、バンカー率
#         #   # なので出場回数
#         #   # 使っているブランド。
#         #   # ユーザー情報＆どういう周り方をしたのかが必要かも
#         #   # カートに乗っている時に周り方の入力する。
#         #   # ボールの紛失
#         #   # netScore = grossScore-handicap-slopeRateWeigth*(slopeRating-55)/10-weatherIndexWeigth*weatherIndex
          
#         #   handicapArray.append(-handicap-(slopeRating-55)/10-weatherIndex)
#         #   netScoreArray.append(netScore)
#         ageArray.append(p)
#     userDF2 = pd.DataFrame({
#               'userId':userIdArray2,
#               'gender':genderArray2,
#               'age':ageArray2,
#               'averageScore':averageScoreArray2,
#               'grossScore':grossScoreArray,
#               'hiddenScore':hiddenScoreArray,
#               'netScore':netScoreArray,
#               'handicap':handicapArray,
#               'clubName':clubNameArray,
#               'corse1':corse1NameArray,
#               'corse2':corse2NameArray,
#               'courseRating':courseRatingArray,
#               'corseType':corseTypeArray,
#               'slopeRating':slopeRatingArray,
#               'slopeRateWeigth':slopeRateWeigthArray,
#               'weather':weatherArray,
#               'weatherIndexWeigth':weatherIndexWeigthArray
              
#               })
    
#     userDF3 = userDF2.sort_values("netScore")
#     userDF3['rank'] = rank
#     userDF3['getting'] = geddingArray
#     df2Array.append(userDF3)


# # dfdf = pd.concat(dfArray)
# totalDF = pd.concat(df2Array)

# df = totalDF.to_csv("/content/drive/MyDrive/golf/total6.csv")
