#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:52:43 2020

@author: anan
"""
import os
import pandas as pd
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import itertools
import tqdm
import xlwt,xlrd

os.chdir('/gpfs/share/home/1801111688/10_species/a_0.1/m_0') #change direction.
os.getcwd() #get current work direction.
data = pd.read_csv("10_species_rnorm.csv")


def LotkaVolterraModel(x, params):
    
    r1 = params["r1"] 
    r2 = params["r2"] 
    r3 = params["r3"] 
    r4 = params["r4"] 
    r5 = params["r5"] 
    r6 = params["r6"] 
    r7 = params["r7"] 
    r8 = params["r8"] 
    r9 = params["r9"] 
    r10 = params["r10"] 
    
    
    n1 = params["n1"]
    n2 = params["n2"] 
    n3 = params["n3"] 
    n4 = params["n4"] 
    n5 = params["n5"] 
    n6 = params["n6"] 
    n7 = params["n7"] 
    n8 = params["n8"] 
    n9 = params["n9"] 
    n10 = params["n10"] 
    
    
    m = params["m"] 
    imm = params["imm"] 
    
    a0102 = params["a0102"] 
    a0103 = params["a0103"] 
    a0104 = params["a0104"] 
    a0105 = params["a0105"] 
    a0106 = params["a0106"] 
    a0107 = params["a0107"] 
    a0108 = params["a0108"] 
    a0109 = params["a0109"] 
    a0110 = params["a0110"] 
    
    a0201 = params["a0201"] 
    a0203 = params["a0203"] 
    a0204 = params["a0204"] 
    a0205 = params["a0205"] 
    a0206 = params["a0206"] 
    a0207 = params["a0207"] 
    a0208 = params["a0208"] 
    a0209 = params["a0209"] 
    a0210 = params["a0210"] 
  
    
    a0301 = params["a0301"] 
    a0302 = params["a0302"] 
    a0304 = params["a0304"] 
    a0305 = params["a0305"] 
    a0306 = params["a0306"] 
    a0307 = params["a0307"] 
    a0308 = params["a0308"] 
    a0309 = params["a0309"] 
    a0310 = params["a0310"] 
   
    
    a0401 = params["a0401"] 
    a0402 = params["a0402"] 
    a0403 = params["a0403"] 
    a0405 = params["a0405"] 
    a0406 = params["a0406"] 
    a0407 = params["a0407"] 
    a0408 = params["a0408"] 
    a0409 = params["a0409"] 
    a0410 = params["a0410"] 
  
    
    a0501 = params["a0501"] 
    a0502 = params["a0502"] 
    a0503 = params["a0503"] 
    a0504 = params["a0504"]
    a0506 = params["a0506"] 
    a0507 = params["a0507"] 
    a0508 = params["a0508"] 
    a0509 = params["a0509"] 
    a0510 = params["a0510"] 

    
    a0601 = params["a0601"] 
    a0602 = params["a0602"] 
    a0603 = params["a0603"] 
    a0604 = params["a0604"] 
    a0605 = params["a0605"] 
    a0607 = params["a0607"] 
    a0608 = params["a0608"] 
    a0609 = params["a0609"] 
    a0610 = params["a0610"] 

    
    a0701 = params["a0701"] 
    a0702 = params["a0702"]
    a0703 = params["a0703"] 
    a0704 = params["a0704"] 
    a0705 = params["a0705"] 
    a0706 = params["a0706"] 
    a0708 = params["a0708"] 
    a0709 = params["a0709"] 
    a0710 = params["a0710"] 

    
    a0801 = params["a0801"] 
    a0802 = params["a0802"] 
    a0803 = params["a0803"] 
    a0804 = params["a0804"] 
    a0805 = params["a0805"] 
    a0806 = params["a0806"] 
    a0807 = params["a0807"] 
    a0809 = params["a0809"] 
    a0810 = params["a0810"] 
 
    
    a0901 = params["a0901"] 
    a0902 = params["a0902"] 
    a0903 = params["a0903"] 
    a0904 = params["a0904"] 
    a0905 = params["a0905"] 
    a0906 = params["a0906"] 
    a0907 = params["a0907"] 
    a0908 = params["a0908"] 
    a0910 = params["a0910"] 
  
    
    a1001 = params["a1001"] 
    a1002 = params["a1002"] 
    a1003 = params["a1003"] 
    a1004 = params["a1004"] 
    a1005 = params["a1005"] 
    a1006 = params["a1006"] 
    a1007 = params["a1007"] 
    a1008 = params["a1008"] 
    a1009 = params["a1009"] 
    
   
   
    xdot = np.array([
                     r1*x[0]*(1-x[0]/n1-a0102*x[1]/n1-a0103*x[2]/n1-a0104*x[3]/n1-
                              a0105*x[4]/n1-a0106*x[5]/n1-a0107*x[6]/n1-a0108*x[7]/n1-
                              a0109*x[8]/n1-a0110*x[9]/n1)-m*x[0]+imm,
        
                     
                     r2*x[1]*(1-x[1]/n2-a0201*x[0]/n2-a0203*x[2]/n2-a0204*x[3]/n2-
                              a0205*x[4]/n2-a0206*x[5]/n2-a0207*x[6]/n2-a0208*x[7]/n2-
                              a0209*x[8]/n2-a0210*x[9]/n2)-m*x[1]+imm,
                     
                     r3*x[2]*(1-x[2]/n3-a0301*x[0]/n3-a0302*x[1]/n3-a0304*x[3]/n3-
                              a0305*x[4]/n3-a0306*x[5]/n3-a0307*x[6]/n3-a0308*x[7]/n3-
                              a0309*x[8]/n3-a0310*x[9]/n3)-m*x[2]+imm,
                     
                     r4*x[3]*(1-x[3]/n4-a0401*x[0]/n4-a0402*x[1]/n4-a0403*x[2]/n4-
                              a0405*x[4]/n4-a0406*x[5]/n4-a0407*x[6]/n4-a0408*x[7]/n4-
                              a0409*x[8]/n4-a0410*x[9]/n4)-m*x[3]+imm,
                     
                     r5*x[4]*(1-x[4]/n5-a0501*x[0]/n5-a0502*x[1]/n5-a0503*x[2]/n5-
                              a0504*x[3]/n5-a0506*x[5]/n5-a0507*x[6]/n5-a0508*x[7]/n5-
                              a0509*x[8]/n5-a0510*x[9]/n5)-m*x[4]+imm,
                     
                     r6*x[5]*(1-x[5]/n6-a0601*x[0]/n6-a0602*x[1]/n6-a0603*x[2]/n6-
                              a0604*x[3]/n6-a0605*x[4]/n6-a0607*x[6]/n6-a0608*x[7]/n6-
                              a0609*x[8]/n6-a0610*x[9]/n6)-m*x[5]+imm,
                     
                     r7*x[6]*(1-x[6]/n7-a0701*x[0]/n7-a0702*x[1]/n7-a0703*x[2]/n7-
                              a0704*x[3]/n7-a0705*x[4]/n7-a0706*x[5]/n7-a0708*x[7]/n7-
                              a0709*x[8]/n7-a0710*x[9]/n7)-m*x[6]+imm,
                     
                      r8*x[7]*(1-x[7]/n8-a0801*x[0]/n8-a0802*x[1]/n8-a0803*x[2]/n8-
                              a0804*x[3]/n8-a0805*x[4]/n8-a0806*x[5]/n8-a0807*x[6]/n8-
                              a0809*x[8]/n8-a0810*x[9]/n8)-m*x[7]+imm,
                      
                       r9*x[8]*(1-x[8]/n9-a0901*x[0]/n9-a0902*x[1]/n9-a0903*x[2]/n9-
                              a0904*x[3]/n9-a0905*x[4]/n9-a0906*x[5]/n9-a0907*x[6]/n9-
                              a0908*x[7]/n9-a0910*x[9]/n9)-m*x[8]+imm,
                       
                       r10*x[9]*(1-x[9]/n10-a1001*x[0]/n10-a1002*x[1]/n10-a1003*x[2]/n10-
                              a1004*x[3]/n10-a1005*x[4]/n10-a1006*x[5]/n10-a1007*x[6]/n10-
                              a1008*x[7]/n10-a1009*x[8]/n10)-m*x[9]+imm
                     ])
                     
           

    return xdot

#RK4 Method
def RungeKutta4(f, x0, t0, tf, dt):#tf为终点时间
    
    t = np.arange(t0, tf, dt)
    nt = t.size
    
    nx = x0.size
    x = np.zeros((nx,nt))
    
    x[:,0] = x0
    
    for k in range(nt - 1):
        
        k1 = dt*f(t[k], x[:,k])
        k2 = dt*f(t[k] + dt/2, x[:,k] +k1/2)
        k3 = dt*f(t[k] + dt/2, x[:,k] +k2/2)
        k4 = dt*f(t[k] + dt, x[:,k] +k3)
        
        dx = (k1 + 2*k2 + 2*k3 + k4)/6
        
        x[:,k+1] =x[:,k] +dx
        
    return x, t
    


iter_list=data.values.tolist()
for i in tqdm.tqdm(iter_list):
   
    params = {"a0102":i[0],"a0103":i[1],"a0104":i[2],"a0105":i[3],"a0106":i[4],"a0107":i[5],"a0108":i[6],"a0109":i[7],
              "a0110":i[8],"a0201":i[9],"a0203":i[10],"a0204":i[11],"a0205":i[12],"a0206":i[13],"a0207":i[14],"a0208":i[15],
              "a0209":i[16],"a0210":i[17],
"a0301":i[18],"a0302":i[19],"a0304":i[20],"a0305":i[21],"a0306":i[22],"a0307":i[23],"a0308":i[24],"a0309":i[25],"a0310":i[26],
"a0401":i[27],"a0402":i[28],"a0403":i[29],"a0405":i[30],"a0406":i[31],"a0407":i[32],"a0408":i[33],"a0409":i[34],"a0410":i[35],
"a0501":i[36],"a0502":i[37],"a0503":i[38],"a0504":i[39],"a0506":i[40],"a0507":i[41],"a0508":i[42],"a0509":i[43],"a0510":i[44],
"a0601":i[45],"a0602":i[46],"a0603":i[47],"a0604":i[48],"a0605":i[49],"a0607":i[50],"a0608":i[51],"a0609":i[52],"a0610":i[53],
"a0701":i[54],"a0702":i[55],"a0703":i[56],"a0704":i[57],"a0705":i[58],"a0706":i[59],"a0708":i[60],"a0709":i[61],"a0710":i[62],
"a0801":i[63],"a0802":i[64],"a0803":i[65],"a0804":i[66],"a0805":i[67],"a0806":i[68],"a0807":i[69],"a0809":i[70],"a0810":i[71],
"a0901":i[72],"a0902":i[73],"a0903":i[74],"a0904":i[75],"a0905":i[76],"a0906":i[77],"a0907":i[78],"a0908":i[79],"a0910":i[80],
"a1001":i[81],"a1002":i[82],"a1003":i[83],"a1004":i[84],"a1005":i[85],"a1006":i[86],"a1007":i[87],"a1008":i[88],"a1009":i[89],
               "r1": i[90], "r2": i[91],"r3": i[92], "r4": i[93],"r5": i[94], "r6": i[95],"r7": i[96], "r8": i[97], "r9": i[98], "r10": i[99], 
               "n1": i[100], "n2": i[101],"n3": i[102], "n4": i[103],"n5": i[104], "n6": i[105],"n7": i[106], "n8": i[107],"n9": i[108], "n10": i[109], 
               "m": 0, "imm": 0.000001
          }
    f = lambda t, x : LotkaVolterraModel(x, params) 
    # initial biomass
    x0 = np.array([0.02,0.02,0.02,0.02,0.02, 0.02,0.02,0.02,0.02,0.02]) 

    # solve the diff.eq 
    
    t0 = 0
    #final time
    th = 3000
   
    dt = 1

    x, t = RungeKutta4(f, x0, t0, th, dt)

    # plot results
    plt.plot(t, x[0,:], color='#808080', label="N1")
    plt.plot(t, x[1,:], color='#c4c697', label="N2")
    plt.plot(t, x[2,:], color='#465d6b', label="N3")
    plt.plot(t, x[3,:], color='#87708c', label="N4")
    plt.plot(t, x[4,:], color='#ffc0cb', label="N5")
    plt.plot(t, x[5,:], color='#00ffff', label="N6")
    plt.plot(t, x[6,:], color='#d2691e', label="N7")
    plt.plot(t, x[7,:], color='#ffff00', label="N8")
    plt.plot(t, x[8,:], color='#322DFB', label="N9")
    plt.plot(t, x[9,:], color='#Ff2222', label="N10")

    plt.xlabel("time(t)") 
    plt.grid()
    plt.legend()

    plt.savefig("m_0-imm_0.000001/temp{}.pdf".format(i[110])) 
    plt.clf()
    #plt.show()    
    from pandas.core.frame import DataFrame
    x=DataFrame(x)
    #x['r_a']=[(i[2],i[0]),(i[3],i[1])]
    y=x.iloc[:,[2990]]  
    y.columns=['ab_2990']  
    df2=y['ab_2990'].sum(axis=0)
    y['re_2990']=y['ab_2990'].div(df2)
    y['re_2990_log']=-1*y['re_2990']*(np.log(y['re_2990']))
    y['shannon']=y['re_2990_log'].sum()  
    y.to_csv('m_0-imm_0.000001/temp{}.csv'.format(i[110]), sep=',', header=True, index=True)

  


