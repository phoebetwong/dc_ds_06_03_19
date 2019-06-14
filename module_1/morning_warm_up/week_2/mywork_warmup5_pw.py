#!/usr/bin/env python
# coding: utf-8

# In[5]:


## create your first simulation

### 1. Create a list with 32 names
names = []
for i in range(32):
    names.append(f"a{i}")
names 


# In[88]:


### 2. Loop through the list in pairs (pick two records at a time)

def pairs(n):
    pair=[]
    for i in range(len(n)):
        if i%2 == 0:
            pair.append([n[i],n[i+1]])
    return pair


# In[87]:


### 3. Use numpy random to throw a coin (virtual coin)
import numpy as np
a = int(np.random.randint(2, size=1))


# In[85]:


### 4. If heads delete first record, else delete the second record 
def winners(p):
    winners=[]
    coin = int(np.random.randint(2, size=1))
    for i in range(len(p)):
        if coin == 1:
            winners.append(p[i][0])
        else:
            winners.append(p[i][1])
    return winners


# In[90]:


### 5. Continue till there is one winner 
def final_winner(fw):
    pair_names = pairs(fw)
    winner_names = winners(pair_names)
    for i in range(len(fw)):
        if len(winner_names)>1:
            pair_names = pairs(winner_names)
            winner_names = winners(pair_names)
    return winner_names


# In[89]:


### 6. Print the winner's name 
print(final_winner(names))


# In[83]:


### 7. Execute from terminal


# In[ ]:




