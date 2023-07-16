#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dates = ['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05']
data ={'Date':pd.to_datetime(dates),'Value':[10,15,8,12,20]}
df = pd.DataFrame(data)
df

