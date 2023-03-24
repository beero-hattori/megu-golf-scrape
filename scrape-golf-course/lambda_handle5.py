import io
import json
import boto3
import csv
from compute import possibilitiesAndValueCompute
import numpy as np
import random
from compute import mainFunc

# import pandas as pd

s3 = boto3.client('s3')


def lambda_handler(event, context):

    try:
        bucketName = 's3-rank-bucket'
        result = s3.list_objects_v2(Bucket=bucketName)

        files = [v["Key"] for v in result["Contents"]]
        SRC_FILE_ENCODING="utf-8"
        handicap = 0
        min = 0
        max = 0
        rangeObj = {}
        rangeArray = []
        pvCsv = ''
        value2Array = []
        header2 = ''
        mainBody = ''

        for object_key_name in files:
            body = s3.get_object(Bucket=bucketName,Key=object_key_name)['Body'].read().decode(SRC_FILE_ENCODING)
            st = io.StringIO()
            st.write(body)
            st.seek(0)
            csv_f =csv.reader(st)
            header = csv_f.__next__()  # ヘッダーの読み込み
            
            
            type = header[0]
            if type == 'PV':
                possibilitiesAndValueArray = []
                pvCsv = csv_f
                header2 = header
                mainBody = body
                # for row in csv_f:
                    
                #     testArray = []
                #     for i,v in enumerate(row):
                #         if i == 0:
                #             testArray.append(v)
                #         else:
                #             testArray.append(float(v.split('"')[0]))
                #     possibilitiesAndValueArray.append(testArray)
                # print('possibilitiesAndValueArray',possibilitiesAndValueArray)
                # for possibilitiesAndValue in possibilitiesAndValueArray:
                #     result = possibilitiesAndValueCompute(header,possibilitiesAndValue,120)
                #     if result == 1:
                #         handicap += float(possibilitiesAndValue[1])   
            if type == 'PV2':
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
                possibilitiesArray = []
                valueArray = []
                # print('possibilitiesAndValueArray',possibilitiesAndValueArray)
                for t in possibilitiesAndValueArray:
                    
                    possibilitiesArray.append(t[2])
                    valueArray.append(t[1])
                
                aaa = random.choices(valueArray,k=1,weights=possibilitiesArray)[0]
                handicap += aaa
            if type == 'value':
                possibilitiesAndValueArray = []
                obj = {}
                for row in csv_f:
                    obj[float(row[0])] = float(row[1])
                    possibilitiesAndValueArray.append(obj)
                value2Array.append(possibilitiesAndValueArray)
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
            if type == 'ranges':
                possibilitiesAndValueArray = []
                
                rangeObj = {}
                for row in csv_f:

                    rangeObj[float(row[0])] = [float(row[1].split('"')[0]),float(row[2])]
                    possibilitiesAndValueArray.append(rangeObj)
                rangeArray.append(rangeObj)
                # print('possibilitiesAndValueArray',possibilitiesAndValueArray)
        
        
        result = mainFunc(handicap,rangeArray,pvCsv,value2Array,header2,mainBody)        
        csv_buf = io.StringIO()
        result.to_csv(csv_buf, header=True, index=False)
        csv_buf.seek(0)
        s3.put_object(Bucket=bucketName, Body=csv_buf.getvalue(), Key='test.csv')

    except Exception as e:
        print(e)
        raise e
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }