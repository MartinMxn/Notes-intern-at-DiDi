## Numpy
n-d array
```
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
b = np.array(data)
# array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
       
b.reshape([4, 2])
# array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
       
a[:2, 1:]
array([[2, 3],
       [5, 6]])
       
c = np.array([[0,1,0,1], [2,1,1,1]])
a - c
array([[1, 1, 3, 3],
       [3, 5, 6, 7]])
 
```

## Pandas
```
from pandas import DataFrame

df = DataFrame({
    'name': ['CS105', 'BA101', 'CS202', 'DS203'],
    'category': ['cs', 'ba', 'cs', 'ds']
})
df
  name	category
  0	CS105	cs
  1	BA101	ba
  2	CS202	cs
  3	DS203	ds
  
df.columns # not ()
Index(['name', 'category'], dtype='object')

df.iloc[1]
name        BA101
category       ba
Name: 1, dtype: object

df.iloc[1:2]
name	category
1	BA101	ba

df.iloc[1:, :1]
	name
1	BA101
2	CS202
3	DS203


import pandas as pd

df2 = DataFrame({
    'name': ['cs101', 'BA101', 'CS202'],
    'student_count': [10, 89, 100]
})

pd.merge(df, df2)

name	category	student_count
0	BA101	ba	89
1	CS202	cs	100

df.to_csv('data.csv', encoding='utf-8') #可以读很多格式数据
new_df = pd.read_csv('data.csv')
new_df
	Unnamed: 0	name	category
0	0	CS105	cs
1	1	BA101	ba
2	2	CS202	cs
3	3	DS203	ds

# 直接读网站数据！
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2019, 6, 28)
end = datetime.datetime(2019, 6, 29)

data = web.DataReader('GOOG', 'yahoo', start, end)

data
High	Low	Open	Close	Volume	Adj Close
Date						
2019-06-27	1087.099976	1075.290039	1084.000000	1076.010010	1004300	1076.010010
2019-06-28	1081.000000	1073.369995	1076.390015	1080.910034	1693200	1080.910034

data.High
Date
2019-06-27    1087.099976
2019-06-28    1081.000000
Name: High, dtype: float64

# 画图
import matplotlib.pylab as plt

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
y = np.random.randn(200, 6)
plt.plot(x, y)


```
