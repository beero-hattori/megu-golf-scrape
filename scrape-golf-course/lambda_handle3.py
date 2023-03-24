import io
import json
import urllib.parse
import boto3
import csv
from compute import possibilitiesAndValueCompute
from compute import totalPossibilitiesAndValueCompute
import random

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
        object_key_name = "growth.csv"
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
        if type == 'V':
          possibilitiesAndValueArray = []
          obj = {}
          for row in csv_f:
            testArray = []
            # possibilitiesAndValueArray
            obj[float(row[0])] = float(row[1])
            # print('obj',obj)
            for i,v in enumerate(row):
                if i == 0:
                    testArray.append(v)
                else:
                    testArray.append(float(v.split('"')[0]))
            possibilitiesAndValueArray.append(testArray)
          print('obj',obj)

          

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
