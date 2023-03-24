import io
import json
import urllib.parse
import boto3
import csv
from compute import possibilitiesAndValueCompute
import numpy as np
# import pandas as pd

s3 = boto3.client('s3')


def lambda_handler(event, context):

    
    try:
        # print(pd.__version__)

        # TODO implement
        # buf = io.BytesIO()
        # df.to_csv(buf, index=False)
        # bucketName = event['Records'][0]['s3']['bucket']['name']
        bucketName = 's3-rank-bucket'
        # key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        object_key_name = "course.csv"
        # s3.put_object(Bucket=bucketName,Key=object_key_name,Body=json.dumps(json_data))
        SRC_FILE_ENCODING="utf-8"
        body = s3.get_object(Bucket=bucketName,Key=object_key_name)['Body'].read().decode(SRC_FILE_ENCODING)
        st = io.StringIO()
        st.write(body)
        st.seek(0)
        csv_f =csv.reader(st)
        header = csv_f.__next__()  # ヘッダーの読み込み
        type = header[0]
        handicap = 0
        if type == 'PV':
          possibilitiesAndValueArray = []
          for row in csv_f:
            testArray = []
            # possibilitiesAndValueArray
            for i,v in enumerate(row):
                if i == 0:
                    testArray.append(v)
                else:
                    testArray.append(float(v.split('"')[0]))
            possibilitiesAndValueArray.append(testArray)
          averageScore = 123
          l = [float(x) for x in list(str(averageScore))]
          averageScore2 = float(averageScore - l[-1])
          for possibilitiesAndValue in possibilitiesAndValueArray:
              
              result = possibilitiesAndValueCompute(header,possibilitiesAndValue,averageScore2)
              if result == 1:
                  
                  print(possibilitiesAndValue)
                  handicap += float(possibilitiesAndValue[1])
        print('handicap',handicap)

          # for r in result:
          #   if r =='value':
          #     continue
          #   else:
          #     print(r,result)
          
          

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# def possibilitiesAndValueCompute(header,row):
#   print('possibilities & value')

#   for i,h in enumerate(header):
#     obj = {}
#     try:
#       key = float(h)
#       if i == 0:
#         obj[key] = row[i]
#     except:
#       continue

#   print('obj',obj)
