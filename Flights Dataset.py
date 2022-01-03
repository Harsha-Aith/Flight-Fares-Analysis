#!/usr/bin/env python
# coding: utf-8

# In[162]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[163]:


train_data = pd.read_excel(r'C:\Users\harsh\Downloads/Data_Train.xlsx')


# In[164]:


test_data = pd.read_excel(r'C:\Users\harsh\Downloads/Test_set.xlsx')


# In[165]:


train_data.head()


# In[166]:


#check for missing values
train_data.isnull().sum


# In[167]:


train_data.isna().sum()


# In[168]:


train_data.shape


# In[169]:


train_data.dropna(inplace = True)


# In[170]:


train_data.isna().sum()


# # Clean the Data for Modeling

# In[171]:


# function to change necessary columns from object to date time
def change_to_time(column):
    train_data[column] = pd.to_datetime(train_data[column])
    
    


# In[172]:


for i in ['Date_of_Journey', 'Dep_Time', 'Arrival_Time']:
    change_to_time(i)


# In[173]:


train_data.dtypes


# In[174]:


# create a new column to add a day of journey 
train_data['Journey_Day'] = train_data['Date_of_Journey'].dt.day


# In[175]:


# create a new column to add a month of journey 
train_data['Journey_Month'] = train_data['Date_of_Journey'].dt.month


# In[176]:


#function to get hour of departure or arrival time for each flight
def get_hour(df, col):
    df[col + '_hour'] = df[col].dt.hour
    #function to get hour of departure or arrival time for each flight
def get_min(df, col):
    df[col + '_min'] = df[col].dt.minute


# In[177]:


get_hour(train_data, 'Dep_Time')
get_min(train_data, 'Dep_Time')
train_data.drop('Dep_Time', axis = 1, inplace = True)


# In[178]:


get_hour(train_data, 'Arrival_Time')
get_min(train_data, 'Arrival_Time')
train_data.drop('Arrival_Time', axis = 1, inplace = True)


# In[ ]:





# In[179]:


# Split the duration into hour in minute
duration=list(train_data['Duration'])
for i in range(len(duration)):
    if len(duration[i].split(' '))==2:
        pass
    else:
        if 'h' in duration[i]: # Check if duration contains only hour
             duration[i]=duration[i] + ' 0m' # Adds 0 minute
        else:
             duration[i]='0h '+ duration[i]
    
    


# In[180]:


train_data['Duration'] = duration


# In[181]:


def hour(hr):
    return hr.split(' ')[0][0:-1]
def minute(hr):
    return hr.split(' ')[1][0:-1]


# In[182]:


# Creating new columns Duration Hr and Duration Min to create separate values 
train_data['Duration_Hour'] = train_data['Duration'].apply(hour)
train_data['Duration_Minute'] = train_data['Duration'].apply(minute)


# In[183]:


train_data.dtypes


# In[184]:


train_data.drop('Duration', axis = 1, inplace = True)


# In[189]:


train_data['Duration_Hour'] = train_data['Duration_Hour'].astype(str).astype(int)
train_data['Duration_Minute'] = train_data['Duration_Minute'].astype(str).astype(int)


# In[ ]:





# In[190]:


train_data.dtypes


# In[191]:


train_data.head()

