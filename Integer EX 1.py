#!/usr/bin/env python
# coding: utf-8

# In[3]:


print(type(18/2))
print(type(18-2))
print(type(18+2))
print(type(18*2))


# In[6]:


row = 1
while row <= 12:
    num = 2 
    col  = 1 
    while col <= 12:
        print("%3dx%2d=%3d" % (num , row , num * row), end="")
        num +=1
        col   +=1
        
    print("")
    row +=1


# In[ ]:




