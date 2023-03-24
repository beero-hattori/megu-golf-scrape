import pandas as pd




df = pd.read_csv('./totalCourse.csv')


df2 = df[df['HOLE：A'].str.contains('PAR', na=False)]

df2.to_csv('./totalCourse2.csv', index=False)

