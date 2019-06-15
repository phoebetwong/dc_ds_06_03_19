#!/usr/bin/env python
# coding: utf-8

# # Pandas and numpy - pair-up
# ### Discussion session
# 
# 1. How will you read the following data into a pandas data frame ? 
#  ` ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt`

# In[94]:


import pandas as pd
import numpy as np
table = pd.read_csv("co2_2.csv", header=(None))
# decimal     average   interpolated    trend    #days
#             date                             (season corr)


# In[39]:


table.info()


# In[40]:


table.head()


#  
# 2. How would you pick columns 0,1,3 ?  
# `[[0, 1, 3]]`

# In[91]:


print(table.iloc[:,[0,1,3]])


# 3. Use a for loop to find all rows where 
# Co2 (column 3) enteries with the value -99.99 (these are missing values) and replace them with NaN values (try using np.nan - do you know what it is? )

# In[38]:


table[3].describe()


# In[100]:


table[3]= table[3].replace(-99.99, np.nan)
print(table.head())


# In[ ]:


#4. Change names of columns to year, month, and CO2 (use colnames)


# In[55]:


table.rename(columns={0: 'year',1:'month',3:'CO2'}, inplace=True)


# In[56]:


print(table.columns)


# In[ ]:


#5. Add a column 'Day' and specifiy the day 15 for all enteries


# In[57]:


table['day']=15
print(table.head())


# 6. Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it)) 

# In[62]:


table['date']=table['year'].map(str) + "-" + table['month'].map(str) + "-" + table['day'].map(str)


# In[90]:


table.date = pd.to_datetime(table.date)
print(table.date.head())


# In[75]:


table['year1']= table.date.dt.year
table.year1


# In[ ]:


#7. Drop the 'Day' column


# In[77]:


table.drop('day', axis=1, inplace=True)
print(table.head())


# In[ ]:


#8. use pandas groupby to print the yeaerly avg. of co2 per year. 


# In[80]:


print(table.groupby(['year'])['CO2'].mean())


# In[ ]:


#9. Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)


# In[81]:


yearnp = np.array(table['year'])


# In[82]:


print(yearnp)


# In[83]:


co2np = np.array(table['CO2'])


# In[84]:


print(co2np)


# In[ ]:


#10. repeat step (3) but this time using the np.where command. 


# In[89]:


co2np1= np.where(co2np == -99.99, np.nan, co2np)
print(co2np1)


# In[ ]:


#11. Download the notebook as .py script and run it from your terminal. 


# In[ ]:


#12. Create a branch in github repository called warm_up_draft   


# In[ ]:


#13. push the notebook with the name CO2 to your new branch on github.

