
# coding: utf-8

# In[1]:

age = {}


# In[2]:

age = dict()


# In[5]:

age = {'Tim':25, 'Jim':31, 'Pam':21, 'Sam':35}


# In[6]:

age['Pam']


# In[7]:

age['Tim'] = age['Tim'] + 1 


# In[8]:

age['Tim'] += 1


# In[9]:

age['Tim']


# In[11]:

names = age.keys() #views object


# In[12]:

type(names)


# In[13]:

age['Tom'] = 50


# In[14]:

names


# In[15]:

ages = age.values()


# In[16]:

ages


# In[17]:

age['Nick'] = 31


# In[18]:

names


# In[19]:

ages


# In[20]:

'Tom' in age


# In[21]:

"Zofia" in age


# In[ ]:



