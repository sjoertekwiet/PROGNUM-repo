#!/usr/bin/env python
# coding: utf-8

# In[1]:


d=float(input("Enter day:"))
m=int(input("Enter month:"))
y=int(input("Enter year:"))
x1=367*y
x2=(7*(y+(m+9)//12))//4
x3=(3*((y+(m-9)//7)//100+1))//4
x4=(275*m)//9
date=x1-x2-x3+x4+d+1721029-0.5
print(f"The Julian date is: {date}")


# In[ ]:




