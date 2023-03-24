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


winningDF = pd.read_csv("./winning2.csv")
totalDF = pd.read_csv("./total.csv")
over500TotalDF = totalDF[totalDF['rank']>500]

totalUserArray= list(over500TotalDF["userId"].unique())


userIdArray = []
nothingArray = []
getArray = []
for i in range(len(totalUserArray)):
    userId = totalUserArray[i]
    userIdArray.append(userIdArray)
    userDF = totalDF.query(f'userId == {userId}')

    nothingCount = userDF.query('getting == 0')['getting'].count()
    nothingArray.append(nothingCount)

    gettingCount = userDF.query('getting == 1')['getting'].count()
    getArray.append(gettingCount)


getNothingDF = pd.DataFrame({
    'userId':userIdArray,
    'nothing':nothingArray,
    'get':getArray

})

getNothingDF.to_csv('./get.csv')




