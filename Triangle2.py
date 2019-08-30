#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
A=float(input("A SIDE LENGTH : "))
B=float(input("B SIDE LENGTH :"))
D=float(input("CORNER C :"))
C=D*math.pi/180
c=math.sqrt((A**2)+(B**2)-(2*A*B*math.cos(C)))
print("c = ",c, "cm.")


# In[ ]:





# In[ ]:




