# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:50:49 2021

@author: CXL
"""

import pandas as pd
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import itertools
import tqdm
import xlwt,xlrd
import glob
import pandas as pd


inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    

inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.00001/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.00001_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    
    

inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.0001/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.0001_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    

inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.0005/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.0005_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    
    
inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.001/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.001_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    

inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.003/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.003_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    

inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.005/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.005_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    
    
inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.008/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.008_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    

inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.01/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.01_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    
    
    
inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.03/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.03_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    


inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.05/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.05_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
    
    
inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.1/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.1_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')


inputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.5/*.csv"
print(inputfile)
outputfile =  r"/gpfs/share/home/1801111688/10_species/a_0.1/m_0-imm_0.5_total_shannon.csv" 
csv_list = glob.glob(inputfile)
filepath = csv_list[0]

df = pd.read_csv(filepath, encoding="gbk", low_memory=False)

df = df.to_csv(outputfile, encoding="gbk", index=False)
for i in range(1, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False)
    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')
