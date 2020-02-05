#!/usr/bin/env python
# coding: utf-8

# In[84]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.linear_model
import sklearn.preprocessing 
import itertools
import scipy.misc


# In[30]:


with open("monedas.txt") as f:
    monedas = f.read()
data=list(monedas)


# In[42]:


P_H=1

prob=np.zeros(len(data))
for i in range(len(data)):
    if data[i]=='c':
        prob[i]=1


# In[92]:


H=np.linspace(0,1,1000)
N_c=len(np.where(prob==1)[0])
N_s=len(np.where(prob==0)[0])
def P_obs_H(N_c,N_s,H):
    return (H**N_c)*(1-H)**N_s

P_H_obs=P_obs_H(N_c,N_s,H)/(np.trapz(P_obs_H(N_c,N_s,H),H))
plt.plot(H,P_H_obs)
L=np.log(P_H_obs)
plt.savefig('P_obs_H.png')


# In[ ]:





# In[ ]:





# In[ ]:




