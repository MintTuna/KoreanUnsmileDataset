import pandas as pd
import numpy as np 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

df = pd.read_csv('final.csv')
df.info()

print(df['여성/가족'].sum())
print(df['남성'].sum())
print(df['성소수자'].sum())
print(df['인종/국적'].sum())
print(df['연령'].sum())
print(df['지역'].sum())
print(df['종교'].sum())
print(df['기타 혐오'].sum())
print(df['악플/욕설'].sum())
print(df['clean'].sum())

column = [float(df['여성/가족'].sum()), float(df['남성'].sum()), float(df['성소수자'].sum()), float(df['인종/국적'].sum()), float(df['연령'].sum()), float(df['지역'].sum()), float(df['종교'].sum()), float(df['기타 혐오'].sum()), float(df['악플/욕설'].sum()), float(df['clean'].sum())]
row = ['여성/가족', '남성', '성소수자', '국적', '연령', '지역', '종교', '기타 혐오', '욕설', 'clean']

print(column)
print(row)
y = np.array(column)
x = np.array(row)
plt.bar(x, y)
plt.show()
