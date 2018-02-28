
# coding: utf-8

# In[1]:


import numpy as np
def L1(yHat, y):
    return np.sum(np.absolute(yHat - y))


# In[2]:


yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))

