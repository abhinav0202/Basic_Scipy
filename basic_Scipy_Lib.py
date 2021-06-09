#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy')


# # question 1

# In[2]:


import scipy.io as sio
import numpy as np

x = np.array([[1, 2, 3,4], 
              [5, 6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

sio.savemat('test.mat', {"f":x})
data = sio.loadmat('test.mat')
print(data)


# # question 2

# In[3]:


from scipy.special import cbrt

res = cbrt([27, 64, 891])
print(res)


# # question 3

# In[4]:


from scipy import linalg
import numpy as np

x = np.array([[4,5], 
              [3,2]])
y = linalg.det(x)

z = linalg.inv(x)

print(y)

print("\n")

print(z)


# # question 4

# In[5]:


import scipy.linalg as la
import numpy as np


x = np.array([[5,4], 
              [6,3]])

eigvals, eigvecs = la.eig(x)
print(eigvals)
print("\n")
print(eigvecs)


# # question 5

# In[6]:


from scipy.sparse import diags
from scipy import sparse
diagonals = [[1, 2, 3, 4], [1, 2, 3], [1, 2]]

A = diags(diagonals, [0, -1, 2]).toarray()
B = sparse.eye(3).toarray()

print(A)
print("\n")
print(B)

sparse.isspmatrix(A)
sparse.isspmatrix(B)


# In[ ]:




