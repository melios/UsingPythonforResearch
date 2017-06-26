
# coding: utf-8

# In[1]:

ids = set()


# In[2]:

ids = set([1,2,3,4,5,6,7,8,9])


# In[3]:

len(ids)


# In[4]:

ids.add(10)


# In[5]:

ids


# In[6]:

ids.add(2)


# In[7]:

ids


# In[8]:

ids.pop()


# In[9]:

ids.pop()


# In[10]:

ids.pop()


# In[11]:

ids.pop()


# In[12]:

ids.pop()


# In[13]:

ids


# In[15]:

ids = set(range(10))


# In[16]:

ids


# In[17]:

males = set([1,3,5,6,7])


# In[18]:

females = ids - males


# In[19]:

type(females)


# In[20]:

females


# In[21]:

males


# In[22]:

everyone = males | females


# In[23]:

everyone


# In[24]:

everyone & set([1,2,3])


# In[25]:

_


# In[26]:

word = 'antidisestablishmentarianism'


# In[27]:

letters = set(word)


# In[28]:

len(letters)


# In[ ]:



