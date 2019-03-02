#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# In[7]:


df = pd.read_csv('/Users/xuexu/Google Drive/Course/ITU/CSC-560/HealthDataset2.csv')
df.head()


# In[50]:


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.boxplot(y=df['Injury'], data=df)


# In[31]:


sns.boxplot(y=df['Death_Rate'], data=df)


# In[32]:


df.dtypes


# In[33]:


df['Death_Rate'] = df['Death_Rate'].astype('float64')


# In[42]:


sns.boxplot(x='CHSI_State_Name', y='All_Death', data=df)


# In[ ]:


#sns.pairplot(df, x="CHSI_State_Name", y = 'Brst_Cancer')


# In[1]:


from scipy import stats
g = sns.jointplot(y="Death_Rate", x="No_HS_Diploma", data=df, kind='reg', height=8)
g.annotate(stats.pearsonr)


# In[66]:


df = pd.read_csv('/Users/xuexu/Google Drive/Course/ITU/CSC-560/HealthDataset2.csv')
df.head()


# In[ ]:


#sns.regplot(advertising.TV, advertising.Sales, order=1, ci=None, scatter_kws={'color':'r', 's':9})
#plt.xlim(-10,310)
#plt.ylim(ymin=0);


# In[ ]:




