#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# matrix transformation


# In[132]:


import numpy as np


# In[133]:


thistuple=([12,14,15],[2,4,6],[16,18,19])


# In[134]:


print(thistuple)


# In[135]:


y=list(thistuple)


# In[136]:


print(y)


# In[137]:


thistuple1= ([[9, 8, 7], 
    [6, 5, 4],
    [3, 2, 1]])


# In[138]:


print(thistuple1)


# In[139]:


x=list(thistuple1)


# In[140]:


print(x)


# In[141]:


print(y+x)


# In[ ]:


# decision tree


# In[142]:


import numpy as np


# In[143]:


import matplotlib.pyplot as plt


# In[144]:


import pandas as pd


# In[145]:



dataset = np.array(
[['Asset Flip', 100, 1000],
['Text Based', 500, 3000],
['Visual Novel', 1500, 5000],
['2D Pixel Art', 3500, 8000],
['2D Vector Art', 5000, 6500],
['Strategy', 6000, 7000],
['First Person Shooter', 8000, 15000],
['Simulator', 9500, 20000],
['Racing', 12000, 21000],
['RPG', 14000, 25000],
['Sandbox', 15500, 27000],
['Open-World', 16500, 30000],
['MMOFPS', 25000, 52000],
['MMORPG', 30000, 80000]
])


# In[146]:


print(dataset)


# In[147]:


X = dataset[:, 1:2].astype(int)


# In[148]:


print(X)


# In[149]:


y = dataset[:, 2].astype(int)


# In[150]:


print(y)


# In[151]:


from sklearn.tree import DecisionTreeRegressor


# In[152]:


regressor = DecisionTreeRegressor(random_state = 0)


# In[153]:


regressor.fit(X, y)


# In[154]:


arr1 = [[3750],]
y_pred = regressor.predict(arr1)
y_pred


# In[155]:


X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Profit to Production Cost (Decision Tree Regression)')

plt.xlabel('Production Cost')
plt.ylabel('Profit')
plt.show()


# In[ ]:


from sklearn.tree import export_graphviz


# In[158]:


export_graphviz(regressor, out_file ='D:/tree.dot',
 feature_names =['Production Cost'])

