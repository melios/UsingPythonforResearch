
# coding: utf-8

# In[1]:

T = (1, 3, 5, 7)


# In[2]:

len(T)


# In[3]:

T + (9, 11)


# In[4]:

T[1]


# In[5]:

x = 12.23


# In[6]:

y = 23.34


# In[13]:

coordinate = (x, y) # packing a tuple or tuple packing


# In[14]:

type(coordinate)


# In[15]:

coordinate


# In[18]:

(c1, c2) = coordinate #unpacking a tuple


# In[19]:

c1


# In[20]:

c2


# In[22]:

coordinates = [(0,0),
              (1,1),
              (2,4),
              (3,9),
              (4,16),
              (5,25),
              (6,36),
              (7,49),
              (8,64),
              (9,81)]


# In[23]:

coordinates


# In[31]:

for (x,y) in coordinates: # use a parentesis to be clearer that you are dealing with a tuple
    print (x,y)


# In[30]:

for x,y in coordinates:
    print (x,y)


# In[32]:

c  = (3,2)


# In[33]:

type(c)


# In[34]:

c = (2)


# In[35]:

type(c)


# In[36]:

c = (2,)


# In[37]:

type(c)


# In[40]:

c = 2, 


# In[41]:

type(c)


# In[ ]:



