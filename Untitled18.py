#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("D:/5_Minute_Crafts.csv")


# In[2]:


data.head()


# In[31]:


top_10=data.sort_values(by=['total_views'],ascending=False)


# In[32]:


print(top_10)


# In[54]:


data.sort_values(by=['num_chars'],ascending=False)


# In[70]:


top_10.plot.scatter(x='num_chars',y='total_views',rot=5, fontsize=12)


# In[53]:


data.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_chars',rot=5, fontsize=12)


# In[57]:


data.nlargest(10,'num_chars').plot.scatter(y='total_views', x='num_chars',rot=5, fontsize=12)


# In[55]:


data.sort_values(by=['num_words'],ascending=False)


# In[56]:


top_10.plot.scatter(y='total_views', x='num_words',rot=5, fontsize=12)


# In[58]:


data.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_words',rot=5, fontsize=12)


# In[62]:


data.nlargest(10,'num_words').plot.scatter(y='total_views', x='num_words',rot=5, fontsize=12)


# In[63]:


data.sort_values(by=['num_punctuation'],ascending=False)


# In[64]:


top_10.plot.scatter(y='total_views', x='num_punctuation',rot=5, fontsize=12)


# In[65]:


data.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_punctuation',rot=5, fontsize=12)


# In[74]:


data.nlargest(10,'num_punctuation').plot.scatter(y='total_views', x='num_punctuation',rot=5, fontsize=12)


# In[75]:


data.sort_values(by=['num_words_uppercase'],ascending=False)


# In[77]:


top_10.plot.scatter(y='total_views', x='num_words_uppercase',rot=5, fontsize=12)


# In[79]:


data.nlargest(10,'total_views').plot.scatter(y='total_views', x='num_words_uppercase',rot=5, fontsize=12)


# In[81]:


data.nlargest(10,'num_words_uppercase').plot.scatter(y='total_views', x='num_words_uppercase',rot=5, fontsize=12)


# In[ ]:




