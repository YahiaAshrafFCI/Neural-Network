
# coding: utf-8

# In[9]:


import numpy as np
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    a vector of shape (length*height*depth, 1)
    """
    return image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1)


# In[10]:


image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])


# In[11]:


print ("image2vector(image) = " + str(image2vector(image)))
