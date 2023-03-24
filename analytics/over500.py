# ５００位以上の人がもらえる確率
import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split
# import xgboost as xgb
# import plotly.express as px
# from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
totalDF = pd.read_csv("./total.csv")
over500TotalDF = totalDF[totalDF['rank']>500]

totalUserArray= list(over500TotalDF["userId"].unique())


userIdArray = []
nothingArray = []
getArray = []
genderArray = []
ageArray = [] 
averageScoreArray = []
averageRankArray = []

# for i in range(1):
for i in range(len(totalUserArray)):
    userId = totalUserArray[i]
    userIdArray.append(userId)
    userDF = totalDF.query(f'userId == {userId}')
    genderArray.append(userDF['gender'].iloc[0])
    ageArray.append(userDF['age'].iloc[0])
    averageScoreArray.append(userDF['averageScore'].iloc[0])
    averageRankArray.append(userDF['averageScore'].mean())

    nothingCount = userDF.query('getting == 0')['getting'].count()
    nothingArray.append(nothingCount)

    gettingCount = userDF.query('getting == 1')['getting'].count()
    getArray.append(gettingCount)



getNothingDF = pd.DataFrame({
    'userId':userIdArray,
    'nothing':nothingArray,
    'get':getArray,
    'gender':genderArray,
    'age':ageArray,
    'averageScore':averageScoreArray,
    'averageRank':averageRankArray

})

# getNothingDF.to_csv("/content/drive/MyDrive/golf/get.csv")
getDF = pd.read_csv("./over500Get.csv")
getDF.sort_values('get', ascending=False)
n, bins, _ = plt.hist(getDF['get'])
xs = (bins[:-1] + bins[1:])/2 
ys = n
for x, y in zip(xs, ys):
  plt.text(x, y, str(round((y/len(getDF['get']))*100,1)), horizontalalignment="center")

plt.xlabel("getting count")
plt.ylabel("How many people")
plt.show()