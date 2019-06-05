#!/usr/bin/env python
# coding: utf-8

# ### 1. Create a dictionary where each object contains a list of one float (Age) and one string (Family name) (at least 5 objects)
# 
# Example:
# `{Charles: [23.4, "Darwin"], Alan: [42.5, "Turing"]}`

# In[2]:


people = {"Charles": [23.4, "Darwin"], "Alan": [42.5, "Turing"], "Fred": [38.4, "Nietzsche"], "Maynard": [70.1, "Keynes"], "Phoebe":[38.8, "Wong"]}


# In[ ]:


print(people)


# In[7]:


people["Phoebe"][0]


# people = [{'Family Name': 'Darwin', 'Age': 23.4},{'Family Name': 'Turing', 'Age': 42.5}]

# ### 2. Delete one object from the dictionary

# In[3]:


people.pop('Phoebe')
print(people)


# ### 3. Replace the float number of one of your objects - we are changing a list entry inside a dictionary record! look at Darwin's new age
# 
# Example:
# `{Charles: [99.73, "Darwin"], Alan: [42.5, "Turing"]}`

# In[4]:


people["Charles"][0]=99.73
print(people)


# ### 4. write a for loop that goes through all records in the dictionary, prints the family name and assigns the float numbers into one merged list (see ages)
# 
# `ages = [23.4, 22.9, 552.9]`

# In[20]:


people['Charles'][0]


# In[24]:


age =[]
for p in people:
    print(people[p][1])
    age.append(people[p][0])
print(age)


# ### 5. Download your notebbok as a .py (regular python script) save it somewhere you know
# 
# ### 6. Go to terminal, navigate to the folder where you have saved the script and execute it through the terminal
# 
# `use commandds: 
# cd and 
# python your_script.py`
# 
# 
# ### [optional] Calculate with a for loop the median and mean of the ages list

# In[19]:


import statistics
age =[]
for p in people:
    age.append(people[p][0])
statistics.median(age)


# In[20]:


(42.5+70.1)/2


# In[18]:


sum=0
for p in people:
    sum += people[p][0]
print ("mean is " + str(round(sum/len(people),2)))


# In[21]:


age


# In[22]:


age.sort()
print(age)


# In[35]:


len(age)%2


# In[44]:


(round(age[3]))

a = round(5/2)
print(a)
# In[45]:


age[int(len(age)/2-1)]


# In[32]:


n= int(len(age)/2)
age[n]


# In[49]:


#v = 1
if False:
    print('yes')
else: 
    print('no')


# In[50]:


if True:
    print('yes')
else:
    print('no')





# In[61]:


def mymed(age):
    age.sort()
    if len(age)%2 == 0:
        med = (age[int(len(age)/2)]+age[int(len(age)/2-1)])/2
    else:    
        med = age[round(len(age)/2)]
    return "median is " + str(round(med,2))

print(mymed(age))
        
    


# In[58]:


age1 = [1,2,3,4,5]
mymed(age1)


# In[59]:


age2=[1,2,3,4]
mymed(age2)


# In[60]:


age3=[1,2,3,4,5,6]
mymed(age3)


# In[ ]:




