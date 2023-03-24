import random
import pandas as pd
import boto3
import io
import numpy as np
import unicodedata
import csv

s3 = boto3.client('s3')

def bonusFunc(pvCsv,handicap,averageScore,header,userId):
  # 走ってる
  print('userId2開始',userId)
  
  br = 0
  possibilitiesAndValueArray = []
  result = []
  # 一回叩くだけ
  test = []
  l = [float(x) for x in list(str(averageScore))] 
  averageScore2 = float(float(averageScore)-l[-1])
  for row in pvCsv:
      # 一発目だけ走ってる
      print('userId2途中',userId)
      testArray = []
      for i,v in enumerate(row):
          if i == 0:
            testArray.append(v)
          else:
            testArray.append(float(v.split('"')[0]))
      possibilitiesAndValueArray.append(testArray)
  for possibilitiesAndValue in possibilitiesAndValueArray:
    # 一発目だけ走ってる
    print('userId2',userId)

    print('possibilitiesAndValueCompute',possibilitiesAndValueCompute(header,possibilitiesAndValue,averageScore2))
    

    if possibilitiesAndValueCompute(header,possibilitiesAndValue,averageScore2) == 1:
    # if 1 == 1:
      # 走ってる
      print('1です')
      print('possibilitiesAndValueArray',possibilitiesAndValueArray)
      # 走ってない
      br += possibilitiesAndValue[1]
      # 一発目だけ走ってる
      print(f'br:{userId}',br)
    else:
      # 走ってる
      print('0です')
      
  print(f'bonus result{userId}',float(br)+float(handicap))
  return float(br)+float(handicap)

def possibilitiesAndValueCompute(header,row,score):


  array = []
  obj = {}
  value = 0
  keyArray = []
  for i,h in enumerate(header):
    if i == 0:
      continue
    elif i == 1:
      obj['value'] = row[i]
    else:
      key = float(h.replace('"',''))
      keyArray.append(key)
      obj[key] = row[i]
  if score<keyArray[0]:
    score = keyArray[0]
  elif score>keyArray[-1]:
    score = keyArray[-1]
  value = random.choices([0,1],k=1,weights=[1-obj[score],obj[score]])[0]
  return value
  
def totalPossibilitiesAndValueCompute(header,row):


  array = []
  obj = {}
  value = 0
  for i,h in enumerate(header):
    if i == 0:
      continue
    elif i == 1:
      obj['value'] = row[i]
    else:
      key = float(h.replace('"',''))
      obj['p'] = row[i]

  # value = random.choices([0,1],k=1,weights=[1-obj[score],obj[score]])[0]
  return obj

def computeNetScore(obj):
  pvCsv = obj['pvCsv']
  handicap = float(obj['handicap'])
  averageScore = obj['averageScore']
  header = obj['header']
  min = obj['min']
  max = obj['max']
  totalCourse = obj['totalCourse']
  rangeArray = obj['rangeArray']
  slopeRating = obj['slopeRating']
  value2Array = obj['value2Array']
  average = (min+max)/2
  hiddenCourse = get_integral_value_combination(totalCourse, 48)
  npData = [round(p) for p in np.random.normal(average, 1, 18)]
  grossScore = sum(npData)+72
  hiddenCourseScore = 0
  t = 0
  isBonus = 0
  userId = obj['userId']
  for i,course in enumerate(totalCourse):
    t +=course+npData[i]
    if len(hiddenCourse) !=0 and hiddenCourse[0] == course:
      hiddenCourseScore+=course+npData[i]
      hiddenCourse.remove(course)
      if isBonus ==0:
        bonusResult = bonusFunc(pvCsv,handicap,averageScore,header,userId)
        # ちゃんと計算されてる
        print('bonusResult',bonusResult)
        handicap += bonusResult
        isBonus +=1 
        
  print('after userId',userId)
  print('after handicap',handicap)
  
  growth = 0
  par = 72

  
  
  growth = 0
  # growth =  averageScore-grossScore
  
  # growthObj = value2Array[0][0]
  # l = [float(x) for x in list(str(growth[i]))] 
  # growth = float(growth-l)
  # growthKeys = l.keys()
  # print('handicap',handicap)
  # if growthKeys[-1]>growth:
  #   growth = growthKeys[-1]
  # try:
  #   growthIndex = growthKeys.index(growth)
  #   growth = growthObj[growthKeys[growthIndex]]
  # except:
  #   print('no')
  
  # print(f'min:{min}',f'max:{max}')


  netScore = grossScore - (hiddenCourseScore*1.5-par)*0.8+ handicap -(slopeRating-55)/10+growth
  print('grossScore',grossScore)
  print('netScore',netScore)

  return {
    'netScore':netScore,
    'grossScore':grossScore,
    'hiddenCourseScore':hiddenCourseScore,
    'handicap':handicap,
    'growth':growth
    
  }
  

      


def get_integral_value_combination(value, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(value)):
            a((u + 1), l + [value[u]], r, t)
        return r
    return a(0, [], [], target)[0]

def courseLayoutDF(clubName,corseName):
  bucketName = 's3-genders'
  
  courseLayout = unicodedata.normalize('NFKD', f'total-layout2/{clubName}{corseName}詳細.csv')
  d = s3.get_object(Bucket=bucketName, Key=courseLayout)

  df = pd.read_csv(io.BytesIO(d['Body'].read()))
  cols = [2,3,5,6,8,9]
  dropDF = df.drop(df.columns[cols],axis=1)
  afterDF = ''
  try:
    afterDF = dropDF[dropDF["HOLE：1"].str.contains("PAR：", na=False)]
  except:
    afterDF = dropDF[dropDF["HOLE：10"].str.contains("PAR：", na=False)]

  afterArray = afterDF.values
  resultArray = []
  for v in range(len(afterDF.values)):
    for i in range(len(afterArray[v])-1):
      resultArray.append(int(afterArray[v][i+1].split('：')[1]))
  return list(resultArray)


def mainFunc(handicap,rangeArray,pvCsv,value2Array,header2,mainBody):
  st = io.StringIO()
  st.write(mainBody)
  st.seek(0)
  csv_f =csv.reader(st)
  header = csv_f.__next__()  # ヘッダーの読み込み
  content = [row for row in csv_f]  # 各年のデータを要素とするリスト

  
  
  
  
  rArray  = rangeArray[0]
  genderArray = []
  userIdArray = [x+1 for x in range(1000)]
  ages = [0,1,2,3,4,5,6]
  maleProbability =  [1.1, 2.2, 10.0, 18.9, 27.8, 28.9, 11.1]
  femaleProbability = [0.01,0.02,0.17,0.25,0.26,0.24,0.05]
  
  averageScores = [0,1,2,3,4,5,6]
  
  averageScoreProbability = [0.036,0.263,0.434,0.199,0.048,0.019,0.001]
  
  for i in range(1000):
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
  
  userIdArray = [x+1 for x in range(1000)]
  ageArray = []
  
  for i in range(1000):
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
  
  rank = [x+1 for x in range(1000)]
  geddingArray = []
  
  for g in range(1000):
    if g+1<=100:
      geddingArray.append(1)
    elif (g+1)%5 ==0 and (g+1)!=1000:
      geddingArray.append(1)
    elif g+1 == 999:
      geddingArray.append(1)
    else:
      geddingArray.append(0)


  bucketName = 's3-genders'
  maleObj = s3.get_object(Bucket=bucketName, Key='final-male.csv')
  maleDf = pd.read_csv(io.BytesIO(maleObj['Body'].read()))

  femaleObj = s3.get_object(Bucket=bucketName, Key='final-female.csv')
  femaleDf = pd.read_csv(io.BytesIO(femaleObj['Body'].read()))
  
  maleDf = maleDf.query('Par == 72')
  femaleDf = femaleDf.query('Par == 72')
  
  genderArray = []
  
  for i in range(1000):
    if (i+1)%10 == 0:
      genderArray.append(1)
    else:
      genderArray.append(0)
  
  ages = [0,1,2,3,4,5,6]
  maleProbability =  [1.1, 2.2, 10.0, 18.9, 27.8, 28.9, 11.1]
  femaleProbability = [0.01,0.02,0.17,0.25,0.26,0.24,0.05]
  
  averageScores = [0,1,2,3,4,5,6]
  
  averageScoreProbability = [0.036,0.263,0.434,0.199,0.048,0.019,0.001]
  
  
  for i in range(len(maleProbability)):
    maleProbability[i]=round(maleProbability[i]/100,4)
  
  par = 72
  
  totalGrossScoreArray = []
  averageScoreArray = []
  
  userIdArray = [x+1 for x in range(1000)]
  ageArray = []
  

  for i in range(1000):
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
  
  rank = [x+1 for x in range(1000)]
  geddingArray = []
  
  for g in range(1000):
    if g+1<=100:
      geddingArray.append(1)
    elif (g+1)%5 ==0 and (g+1)!=1000:
      geddingArray.append(1)
    elif g+1 == 999:
      geddingArray.append(1)
    else:
      geddingArray.append(0)
  for _ in range(1):
      userIdArray2 = []
      genderArray2 = []
      ageArray2 = []
      averageScoreArray2 = []
      hiddenScoreArray = []
      grossScoreArray = []
      netScoreArray = []
      course = []
      clubNameArray = []
      corse1NameArray = []
      corse2NameArray = []
      courseRatingArray = []
      slopeRatingArray = []
      corseTypeArray = []
      handicapArray = []
      prevNetArray = []
      weatherArray = []
      slopeRateWeigthArray = []
      weatherIndexWeigthArray = []
      growthArray = []
      for i in range(len(userIdArray)):
        weatherIndex = -1*random.choices([0,1,2],k=1,weights=[0.7,0.2,1])[0]
        weatherArray.append(weatherIndex)
        # slopeRateWeigthArray.append(slopeRateWeigth)   
        # weatherIndexWeigthArray.append(weatherIndexWeigth)
        userIdArray2.append(userIdArray[i])
        genderArray2.append(genderArray[i])
        ageArray2.append(ageArray[i])
        averageScoreArray2.append(averageScoreArray[i])
        obj = {}
        # text = [row for row in reader]
        # print('text',text)
        if genderArray[i] == 0:
          n = np.random.randint(0,len(maleDf))
          clubName = maleDf.iloc[n]['Unnamed: 0.1.1.1']
          clubNameArray.append(clubName)
          corse1Name = maleDf.iloc[n]['コース１']
          corse1NameArray.append(corse1Name)
          corse2Name = maleDf.iloc[n]['コース2']
          corse2NameArray.append(corse2Name)
          courseRating = maleDf.iloc[n]['CourseRating']
          courseRatingArray.append(courseRating)
          slopeRating  = int(maleDf.iloc[n]['SlopeRating'])
          slopeRatingArray.append(slopeRating)
          corseType = maleDf.iloc[n]['コース１.2']
          corseTypeArray.append(corseType)
          corse1Name = courseLayoutDF(clubName,corse1Name)
          corse2Name = courseLayoutDF(clubName,corse2Name)
          totalCourse = corse2Name+corse1Name
          

          l = [float(x) for x in list(str(averageScoreArray[i]))]
          averageScore2 = float(averageScoreArray[i] - l[-1])
          if averageScore2<70:
            averageScore2 = 70
          elif averageScore2>140:
            averageScore2 = 140
          testObj = {}
          
          min = 0
          max = 0
          try:
            min = rArray[averageScore2][0]
            max = rArray[averageScore2][1]
          except:
            print('no')
          obj['min'] = min
          obj['max'] = max
          obj['totalCourse'] = totalCourse
          obj['averageScore'] = averageScoreArray[i]
          obj['rangeArray'] = rangeArray
          obj['pvCsv'] = content
          obj['handicap'] = handicap
          obj['slopeRating'] = slopeRating
          obj['value2Array'] = value2Array
          obj['header'] = header2
          obj['userId'] = i
          result = computeNetScore(obj)
          result['userId'] = i
          netScoreArray.append(result['netScore'])
          grossScoreArray.append(result['grossScore'])
          hiddenScoreArray.append(result['hiddenCourseScore'])
          handicapArray.append(result['handicap'])
          # growthArray.append(result['growth'])
        else:
          n = np.random.randint(0,len(maleDf))
          clubName = maleDf.iloc[n]['Unnamed: 0.1.1.1']
          clubNameArray.append(clubName)
          corse1Name = maleDf.iloc[n]['コース１']
          corse1NameArray.append(corse1Name)
          corse2Name = maleDf.iloc[n]['コース2']
          corse2NameArray.append(corse2Name)
          courseRating = maleDf.iloc[n]['CourseRating']
          courseRatingArray.append(courseRating)
          slopeRating  = int(maleDf.iloc[n]['SlopeRating'])
          slopeRatingArray.append(slopeRating)
          corseType = maleDf.iloc[n]['コース１.2']
          corseTypeArray.append(corseType)
  
  
          corse1Name = courseLayoutDF(clubName,corse1Name)
          corse2Name = courseLayoutDF(clubName,corse2Name)
          totalCourse = corse2Name+corse1Name

          l = [float(x) for x in list(str(averageScoreArray[i]))]
          averageScore2 = float(averageScoreArray[i] - l[-1])
          if averageScore2<70:
            averageScore2 = 70
          elif averageScore2>140:
            averageScore2 = 140
          testObj = {}
          
          min = 0
          max = 0
          try:
            min = rArray[averageScore2][0]
            max = rArray[averageScore2][1]
          except:
            print('no')
          obj['min'] = min
          obj['max'] = max
          obj['totalCourse'] = totalCourse
          obj['averageScore'] = averageScoreArray[i]
          obj['rangeArray'] = rangeArray
          obj['pvCsv'] = content
          obj['handicap'] = handicap
          obj['slopeRating'] = slopeRating
          obj['value2Array'] = value2Array
          obj['header'] = header2
          obj['userId'] = i
          print('before userId',i)
          result = computeNetScore(obj)
          print('female result',result)
          netScoreArray.append(result['netScore'])
          grossScoreArray.append(result['grossScore'])
          hiddenScoreArray.append(result['hiddenCourseScore'])
          handicapArray.append(result['handicap'])
          # growthArray.append(result['growth'])
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
                'clubName':clubNameArray,
                'corse1':corse1NameArray,
                'corse2':corse2NameArray,
                'courseRating':courseRatingArray,
                'corseType':corseTypeArray,
                'slopeRating':slopeRatingArray,
                'weather':weatherArray,
                # 'growth':growthArray,
                # 'slopeRateWeigth':slopeRateWeigthArray,
                # 'weatherIndexWeigth':weatherIndexWeigthArray
                
                })
      
      userDF3 = userDF2.sort_values("netScore")
      userDF3['rank'] = rank
      userDF3['getting'] = geddingArray
      df2Array.append(userDF3)
  
  
  totalDF = pd.concat(df2Array)
  return totalDF
  
  # df = totalDF.to_csv("/content/drive/MyDrive/golf/total6.csv")
  
  