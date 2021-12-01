#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data= pd.read_csv("D:/5_Minute_Crafts.csv")


# In[2]:


print(data)


# In[3]:


data.head()


# In[7]:


data.isnull().values.any()


# In[9]:


data.isnull().sum().sum()


# In[4]:


data.nlargest(3,"duration_seconds")


# In[5]:


data.nlargest(3,"total_views")


# In[6]:


data.nlargest(3,'num_chars')


# In[10]:


data.nlargest(3,'num_words_uppercase')


# In[12]:


data.nlargest(3,'num_punctuation')


# In[13]:


data.nsmallest(3,'num_words_uppercase')


# In[14]:


data.nsmallest(3,'total_views')


# In[ ]:




