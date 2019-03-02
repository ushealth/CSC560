#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:17:15 2019

@author: Xue Xu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# read 4 different files
file1 = pd.read_csv('/Users/xuexu/Google Drive/Course/ITU/CSC-560/module4/chsi_dataset/MEASURESOFBIRTHANDDEATH.csv')
file2 = pd.read_csv('/Users/xuexu/Google Drive/Course/ITU/CSC-560/module4/chsi_dataset/VUNERABLEPOPSANDENVHEALTH.csv')
file3 = pd.read_csv('/Users/xuexu/Google Drive/Course/ITU/CSC-560/module4/chsi_dataset/DEMOGRAPHICS.csv')
file4 = pd.read_csv('/Users/xuexu/Google Drive/Course/ITU/CSC-560/module4/chsi_dataset/SUMMARYMEASURESOFHEALTH.csv')

# pick up selected columns from several files
newfile = file3[['CHSI_County_Name','CHSI_State_Name','Population_Size']]
print(newfile)
newfile[['Brst_Cancer','Col_Cancer','CHD','Lung_Cancer','MVA','Stroke','Suicide','Injury']] = file1[['Brst_Cancer','Col_Cancer','CHD','Lung_Cancer','MVA','Stroke','Suicide','Injury']]
newfile[['No_HS_Diploma','Unemployed','Sev_Work_Disabled','Major_Depression','Recent_Drug_Use']] = file2[['No_HS_Diploma','Unemployed','Sev_Work_Disabled','Major_Depression','Recent_Drug_Use']]
newfile[['All_Death']] = file4[['All_Death']]

# cut rows of setected states
df1=newfile.iloc[184:306]
df2=newfile.iloc[593:695]
df3=newfile.iloc[385:544]
newframe = [df1, df2, df3]
result = pd.concat(newframe)

# add a new column death rate

result['Death_Rate']= np.divide(result['All_Death'],result['Population_Size']) 

# drop rows with missing data

result = result.loc[:, :].replace(-1111.1, np.nan)
result = result.loc[:, :].replace(-2222.2, np.nan)
result = result.dropna()
print(result)

#write the new dataset to a file
result.to_csv("HealthDataset1.csv",index=False,sep=',')


