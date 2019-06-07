#!/usr/bin/env python
# coding: utf-8

# ### 1. Create a dictionary where each object contains a list of one float (Age) and one string (Family name) (at least 5 objects)
# 
# Example:
# `{Charles: [23.4, "Darwin"], Alan: [42.5, "Turing"]}`

# In[5]:


people = {"Charles": [23.4, "Darwin"], "Alan": [42.5, "Turing"], "Fred": [38.4, "Nietzsche"], "Maynard": [70.1, "Keynes"], "Phoebe":[38.8, "Wong"]}


# In[7]:


people["Phoebe"][0]


# people = [{'Family Name': 'Darwin', 'Age': 23.4},{'Family Name': 'Turing', 'Age': 42.5}]

# ### 2. Delete one object from the dictionary

# In[11]:


people.pop('Phoebe')
people


# ### 3. Replace the float number of one of your objects - we are changing a list entry inside a dictionary record! look at Darwin's new age
# 
# Example:
# `{Charles: [99.73, "Darwin"], Alan: [42.5, "Turing"]}`

# In[12]:


people["Charles"][0]=99.73
people


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

# In[ ]:




