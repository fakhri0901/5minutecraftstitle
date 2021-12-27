#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("D:/5_Minute_Crafts.csv")


# In[3]:


data.head()


# In[4]:


data.isnull().values.any()


# In[5]:


data.isnull().sum().sum()


# In[43]:


data.describe()


# In[12]:


views=data.sort_values(by=['total_views'],ascending=False)


# In[13]:


views.head()


# In[15]:


chars=data[["video_id","total_views","num_chars"]]
chars.head()


# In[16]:


chars.sort_values(by=['num_chars'],ascending=False)


# In[17]:


views.plot.scatter(x='num_chars',y='total_views',rot=5, fontsize=12)


# In[20]:


chars.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_chars',rot=5, fontsize=12)


# In[21]:


chars.nlargest(10,'num_chars').plot.scatter(y='total_views', x='num_chars',rot=5, fontsize=12)


# In[24]:


words=data[["video_id","total_views","num_words"]]
words.head()


# In[25]:


words.sort_values(by=['num_words'],ascending=False)


# In[26]:


views.plot.scatter(y='total_views', x='num_words',rot=5, fontsize=12)


# In[27]:


words.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_words',rot=5, fontsize=12)


# In[28]:


words.nlargest(10,'num_words').plot.scatter(y='total_views', x='num_words',rot=5, fontsize=12)


# In[29]:


punctuation=data[["video_id","total_views","num_punctuation"]]
punctuation.head()


# In[30]:


punctuation.sort_values(by=['num_punctuation'],ascending=False)


# In[31]:


views.plot.scatter(y='total_views', x='num_punctuation',rot=5, fontsize=12)


# In[32]:


punctuation.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_punctuation',rot=5, fontsize=12)


# In[33]:


punctuation.nlargest(10,'num_punctuation').plot.scatter(y='total_views', x='num_punctuation',rot=5, fontsize=12)


# In[34]:


uppercase=data[["video_id","total_views","num_words_uppercase"]]
uppercase.head()


# In[35]:


uppercase.sort_values(by=['num_words_uppercase'],ascending=False)


# In[36]:


views.plot.scatter(y='total_views', x='num_words_uppercase',rot=5, fontsize=12)


# In[37]:


uppercase.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_words_uppercase',rot=5, fontsize=12)


# In[38]:


uppercase.nlargest(10,'num_words_uppercase').plot.scatter(y='total_views', x='num_words_uppercase',rot=5, fontsize=12)


# In[ ]:




