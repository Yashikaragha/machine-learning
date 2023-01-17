#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv(r'D:\210970071\ml lab\data set\Bengaluru_House_Data.csv')


# In[5]:


df.shape


# In[6]:


df.isnull().sum()


# In[7]:


df.isnull().sum().sum()


# In[8]:


df1=df.fillna(value=0)


# In[9]:


df1


# In[10]:


df2=df.fillna(value=5)


# In[11]:


df2


# In[16]:


df3=df('society'.fillna(value=india))


# In[18]:


df4=df.fillna(method='pad')


# In[19]:


df4


# In[20]:


df5=df1.fillna(method='bfill')


# In[21]:


df5


# In[22]:


df6=df.fillna(method='pad',axis=1)


# In[23]:


df6


# In[24]:


df8=df.fillna({'society':'abcd':'balcony':'defg'})


# In[ ]:





# In[25]:


df9=df.fillna(value=df['balcony'].mean())


# In[26]:


df9


# In[60]:


df10=df.fillna(value=df['balcony'].max())


# In[61]:


df10


# In[62]:


df11=df.dropna()


# In[63]:


df11


# In[64]:


df13=df.dropna(how='any')


# In[65]:


df13


# In[66]:


df13=df.dropna(how='all')


# In[67]:


df13


# In[58]:


df11=df.fillna(value=df['balcony'].mean(skipna=True))


# In[ ]:





# In[59]:


df11


# In[27]:


df.notnull()


# In[30]:


df12=df['balcony'].notnull().count()


# In[31]:


df12


# In[41]:


dfwithoutnull=df[df['balcony'].notnull()]


# In[50]:


df['balcony'].notnull()


# In[51]:


m1=dfwithoutnull.mean()


# In[52]:


m1


# In[42]:


dfwithoutnull


# In[71]:


dfwithoutnull.count()


# In[43]:


count(dfwithoutnull)


# In[47]:


mean1=dfwithoutnull['balcony'].mean()


# In[48]:


mean1


# In[74]:


dfwithnull=df[df['balcony'].isnull()]


# In[45]:


dfwithnull


# In[73]:


dfwithtnull.count()


# In[54]:


mean2=df['balcony'].mean(skipna=True)


# In[55]:


mean2


# In[68]:


df14=df.replace(to_replace=3.0,value=5.0)


# In[69]:


df14


# In[ ]:




