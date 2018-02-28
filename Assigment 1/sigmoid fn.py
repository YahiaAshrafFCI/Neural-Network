
# coding: utf-8

# In[1]:


import numpy as np
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))


# In[2]:


sigmoid(5)

