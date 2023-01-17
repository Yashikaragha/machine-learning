#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

plotdata=pd.DataFrame({
    "2018":[57,67,77,83],
    "2019":[68,73,80,79],
    "2020":[73,78,80,85]},
index=["django","gafur","yash","ragha"])


# In[10]:


plotdata.plot(kind="bar",figsize=(15,8))
plt.title("fifa ratings")
plt.xlabel("footballer")
plt.ylabel("ratings")


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

plotdata=pd.DataFrame({
    "2018":[57,67,77,83],
    "2019":[68,73,80,79],
    "2020":[73,78,80,85]},
index=["django","gafur","yash","ragha"])
plotdata.plot(kind="bar",stacked=True,figsize=(15,8))
plt.title("fifa ratings")
plt.xlabel("footballer")
plt.ylabel("ratings")


# In[ ]:




