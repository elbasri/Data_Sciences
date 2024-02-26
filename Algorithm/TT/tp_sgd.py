# -*- coding: utf-8 -*-
"""TP_SGD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XKzRMqeY4P8BhJ2_FpdGbDtHOtcvsw6H
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dataset.csv',sep=";",header=None)
df.columns = ['x0','x1','y']

m = len(df)

indx = np.random.randint(0,m-1,3)
indx

def generateIndx(m,size):
    return np.random.randint(0,m-1,size)

generateIndx(m,5)

def dJ0(t0,t1,aleaIndx):
    s = 0
    for i in range(len(aleaIndx)):
        s += ((t0*df.x0[aleaIndx[i]] +t1*df.x1[aleaIndx[i]])-df.y[aleaIndx[i]])*df.x0[aleaIndx[i]]
    return s/m

def dJ1(t0,t1,aleaIndx):
    s = 0
    for i in range(len(aleaIndx)):
        s += ((t0*df.x0[aleaIndx[i]] +t1*df.x1[aleaIndx[i]])-df.y[aleaIndx[i]])*df.x1[aleaIndx[i]]
    return s/m

def MSE(t0,t1,m):
    mse = 0
    for i in range(m):
        mse += (t0+ t1*df.x1[i]- df.y[i])**2
    return mse/m

alpha, t0, t1 = 0.002, 1, 2
nbrIteration = 200
m=50
size = 3
mse_list=[]
for i in range(nbrIteration):
    aleaIndx = generateIndx(m,size)
    t0 = t0 - alpha*dJ0(t0,t1,aleaIndx)
    t1 = t1 - alpha*dJ1(t0,t1,aleaIndx)
    mse_list.append(MSE(t0,t1,m))
(t0,t1)

plt.plot(np.arange(nbrIteration),mse_list)
plt.grid()