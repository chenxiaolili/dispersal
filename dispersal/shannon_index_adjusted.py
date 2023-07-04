# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 22:19:23 2021

@author: CXL
"""
import pandas as pd
import numpy as np
import os

#change direction
os.chdir('/gpfs/share/home/1801111688/10_species/a_0.1')
os.getcwd()#get current work direction

#1
filepath = "m_0-imm_0_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))
df.to_csv('m_0-imm_0_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#2
filepath = "m_0-imm_0.00001_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")


col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.00001_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.00001_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#3
filepath = "m_0-imm_0.0001_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")


col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))
df.to_csv('m_0-imm_0.0001_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.0001_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#4
filepath = "m_0-imm_0.0005_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")


col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.0005_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.0005_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#5
filepath = "m_0-imm_0.001_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.001_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.001_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#6
filepath = "m_0-imm_0.003_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")


col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))
df.to_csv('m_0-imm_0.003_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.003_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#7
filepath = "m_0-imm_0.005_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")


col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.005_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.005_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#8
filepath = "m_0-imm_0.008_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.008_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.008_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#9
filepath = "m_0-imm_0.01_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.01_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.01_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


#10
filepath = "m_0-imm_0.03_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))#shannon
df.to_csv('m_0-imm_0.03_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.03_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)




#11
filepath = "m_0-imm_0.05_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))
df.to_csv('m_0-imm_0.05_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.05_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)

#12
filepath = "m_0-imm_0.1_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 #richness
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))
df.to_csv('m_0-imm_0.1_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.1_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


filepath = "m_0-imm_0.5_total_shannon.csv"
df = pd.read_csv(filepath, encoding="gbk")

col_name=df.columns.tolist()
col_name.insert(5, 'richeness')
df=df.reindex(columns=col_name)

for i in range(1, 10001):
    df.iloc[10*(i-1),5]=0
    for j in range(0, 10):
        if df.iloc[j+10*(i-1),1]>=0.02:
            df.iloc[10*(i-1),5]=df.iloc[10*(i-1),5]+1 
        else:
            df.iloc[j+10*(i-1),1]=0
            df.iloc[j+10*(i-1),2]=1
    df.iloc[10*(i-1),4]=0
    for j in range(0, 10):
        df.iloc[10*(i-1),4]=df.iloc[10*(i-1),4]+(-1*df.iloc[j+10*(i-1),2]*(np.log(df.iloc[j+10*(i-1),2])))
df.to_csv('m_0-imm_0.5_total_shannon-adjusted.csv', sep=',', header=True, index=False)

index = np.zeros(100000)
index = np.array(index,dtype=bool)
for i in range(0, 10000):
    if df.iloc[10*i,4]>=0:
        index[10*i] = True
#index = bool(index)
df_new = df[index]
df_new = df_new.iloc[:5000]
df_new.to_csv('m_0-imm_0.5_total_shannon-adjusted-1.csv', sep=',', header=True, index=False)


