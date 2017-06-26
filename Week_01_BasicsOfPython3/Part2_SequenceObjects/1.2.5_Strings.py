
# coding: utf-8

# In[1]:

s = "Python"


# In[2]:

len(s)


# In[3]:

s[0]


# In[4]:

s[-1]


# In[6]:

s[0:3]


# In[8]:

s[-3:] #last 3 characters


# In[10]:

"y" in s


# In[11]:

"Y" in s


# In[12]:

12 + 12


# In[13]:

"hello " + "world"


# In[14]:

s = "Python"


# In[15]:

3 * s


# In[16]:

"eight equals " + 8


# In[17]:

"eight equals " + str(8)


# In[18]:

dir(str)


# In[20]:

get_ipython().magic('pinfo str.replace')


# In[ ]:

'''
Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      method_descriptor
'''


# In[21]:

name = "Tina Fey"


# In[22]:

name.replace('T', 't')


# In[23]:

new_name = name.replace('T', 't')


# In[24]:

new_name


# In[25]:

name


# In[28]:

names = name.split(" ")


# In[30]:

names


# In[31]:

type(names)


# In[32]:

len(names)


# In[33]:

names[0]


# In[35]:

names[1]


# In[36]:

type(names[0])


# In[37]:

names[0].upper()


# In[38]:

names[1].lower()


# In[ ]:



