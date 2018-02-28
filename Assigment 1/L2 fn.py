
# coding: utf-8

# In[1]:


import numpy as np
def L2(yHat, y):
    return np.sum((yHat - y)**2)


# In[2]:


yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))


# In[3]:


y = np.array([.9, 0.2, 0.1, .4, .9])
yhat = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))

