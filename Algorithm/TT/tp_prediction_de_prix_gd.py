# -*- coding: utf-8 -*-
"""TP_prediction_de_prix_GD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w-i_PuYUnyz47GLzDIm1a7tkr9z1zBgD
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('house_price.csv')

df.head()

df.drop('Address',axis=1,inplace=True)
df.head()

df.info()

df.describe()

"""## Normalisation MinMax"""

def minmax(lst,x):
    mx, mn = lst.max(), lst.min()
    return (x-mn)/(mx-mn)

minmax(df['Avg. Area Income'], 18000)

newCol = ['x1','x2','x3','x4','x5','y']
df2 = pd.DataFrame()
i = 0
for col in df.columns:
    df2[newCol[i]] = df[col].apply(lambda x:minmax(df[col],x))
    i = i+1

df2.head()

df2.describe()

figs , axs = plt.subplots(1,5,figsize=(20,5))

axs[0].scatter(df2.x1,df2.y,c='r',marker='*')

axs[1].scatter(df2.x2,df2.y,c='r',marker='*')

axs[2].scatter(df2.x3,df2.y,c='r',marker='*')

axs[3].scatter(df2.x4,df2.y,c='r',marker='*')

axs[4].scatter(df2.x5,df2.y,c='r',marker='*')

df2['x0']=1
df2.head()

def dJ0(m,t0,t1,t2,t3,t4,t5):
    s = 0
    for i in range(m):
        s += ((t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i])-df2.y[i])*df2.x0[i]
    return s/m

def dJ1(m,t0,t1,t2,t3,t4,t5):
    s = 0
    for i in range(m):
        s += ((t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i])-df2.y[i])*df2.x1[i]
    return s/m

def dJ2(m,t0,t1,t2,t3,t4,t5):
    s = 0
    for i in range(m):
        s += ((t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i])-df2.y[i])*df2.x2[i]
    return s/m

def dJ3(m,t0,t1,t2,t3,t4,t5):
    s = 0
    for i in range(m):
        s += ((t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i])-df2.y[i])*df2.x3[i]
    return s/m

def dJ4(m,t0,t1,t2,t3,t4,t5):
    s = 0
    for i in range(m):
        s += ((t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i])-df2.y[i])*df2.x4[i]
    return s/m

def dJ5(m,t0,t1,t2,t3,t4,t5):
    s = 0
    for i in range(m):
        s += ((t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i])-df2.y[i])*df2.x5[i]
    return s/m

def MSE(t0,t1,t2,t3,t4,t5,m):
    mse = 0
    for i in range(m):
        mse += (t0*df2.x0[i] +t1*df2.x1[i]+t2*df2.x2[i] +t3*df2.x3[i]+t4*df2.x4[i]+t5*df2.x5[i]-df2.y[i])**2
    return mse/m

alpha,t0,t1,t2,t3,t4,t5 = 0.009, 1, 2,1,2,1,2
nbrIteration = 150
m=4000
mse_list=[]
for i in range(nbrIteration):
    t0 = t0 - alpha*dJ0(m,t0,t1,t2,t3,t4,t5)
    t1 = t1 - alpha*dJ1(m,t0,t1,t2,t3,t4,t5)
    t2 = t2 - alpha*dJ2(m,t0,t1,t2,t3,t4,t5)
    t3 = t3 - alpha*dJ3(m,t0,t1,t2,t3,t4,t5)
    t4 = t4 - alpha*dJ4(m,t0,t1,t2,t3,t4,t5)
    t5 = t5 - alpha*dJ5(m,t0,t1,t2,t3,t4,t5)
    mse_list.append(MSE(t0,t1,t2,t3,t4,t5,m))

(t0,t1,t2,t3,t4,t5)

plt.plot(np.arange(nbrIteration),mse_list)
plt.grid()
